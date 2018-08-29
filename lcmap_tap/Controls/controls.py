"""
Establish the main GUI Window using PyQt, provide the main interactions with child widgets
"""
# Import the main GUI built in QTDesigner, compiled into python with pyuic5.bat
from lcmap_tap.UserInterface import ui_main
from lcmap_tap.Controls import units
from lcmap_tap.RetrieveData.retrieve_ard import ARDData, get_image_ids
from lcmap_tap.RetrieveData.retrieve_ccd import CCDReader
from lcmap_tap.RetrieveData.retrieve_geo import GeoInfo
from lcmap_tap.RetrieveData.retrieve_classes import SegmentClasses
from lcmap_tap.RetrieveData.ard_info import ARDInfo
from lcmap_tap.PlotFrame.plotwindow import PlotWindow
from lcmap_tap.Plotting import make_plots
from lcmap_tap.Plotting.plot_specs import PlotSpecs
from lcmap_tap.Auxiliary import projections
from lcmap_tap.Visualization.ard_viewer_qpixelmap import ARDViewerX
from lcmap_tap.Visualization.maps_viewer import MapsViewer
from lcmap_tap.MapCanvas.mapcanvas import MapCanvas
# from lcmap_tap.RetrieveData import lcmaphttp
from lcmap_tap.logger import log, exc_handler, QtHandler
from lcmap_tap.Auxiliary.caching import read_cache, save_cache, update_cache

import datetime as dt
import os
import sys
import time
import traceback
import matplotlib
import matplotlib.pyplot as plt
import yaml
from osgeo import ogr, osr
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QThread

# Tell matplotlib to use the QT5Agg Backend
matplotlib.use('Qt5Agg')

# Can be used to quickly load paths on start-up for debugging
if os.path.exists('helper.yaml'):
    helper = yaml.load(open('helper.yaml', 'r'))

else:
    helper = None

sys.excepthook = exc_handler


class MainControls(QMainWindow):
    def __init__(self):

        super().__init__()

        # Create an instance of a class that builds the user-interface, created in QT Designer and compiled with pyuic5
        self.ui = ui_main.Ui_TAPTool()

        # Call the method that adds all of the widgets to the GUI
        self.ui.setupUi(self)

        # Display log output to the QPlainTextEdit on the main GUI
        # self.qt_handler = QtHandler(self.ui.plainTextEdit_results)

        self.thread = QThread()

        self.cache_data = dict()
        self.config = None
        self.plot_window = None
        self.maps_window = None
        self.ard_specs = None
        self.ard = None
        self.fig = None
        self.current_view = None
        self.tile = None
        self.version = None
        self.item_list = None
        self.highlighted = None
        self.artist_map = None
        self.lines_map = None
        self.axes = None
        self.geo_info = None  # container for geographic info derived from the input coordinates
        self.ard_observations = None  # container for the ARD stack at the pixel
        self.ccd_results = None  # container for PyCCD results at the pixel
        self.class_results = None  # container for classification results at the pixel
        self.plot_specs = None  # container for plotting data
        self.begin = dt.date(year=1982, month=1, day=1)
        self.end = dt.date(year=2015, month=12, day=31)

        self.qt_handler = QtHandler(self.ui.plainTextEdit_results)

        self.leaflet_map = MapCanvas(self)

        self.selected_units = self.ui.comboBoxUnits.currentText()

        self.drive_letter = self.ui.driveLetter_comboBox.currentText()

        self.connect_widgets()

        self.show()

    def connect_widgets(self):
        """
        Connect the various widgets to the methods they interact with

        Returns:
            None
        """
        if helper:
            """For testing, use some preset values if helper.yaml is found"""
            self.ui.browseoutputline.setText(helper['test_output'])
            self.ui.browsejsonline.setText(helper['test_json'])
            self.ui.browseARDline.setText(helper['ard_dir'])
            self.ui.x1line.setText(helper['test_x'])
            self.ui.y1line.setText(helper['test_y'])

            self.check_values()

        # *** Connect the various widgets to the methods they interact with ***
        self.ui.x1line.textChanged.connect(self.set_units)

        self.ui.x1line.textChanged.connect(self.get_version)

        self.ui.x1line.textChanged.connect(self.assemble_paths)

        self.ui.x1line.textChanged.connect(self.check_values)

        self.ui.y1line.textChanged.connect(self.set_units)

        self.ui.y1line.textChanged.connect(self.get_version)

        self.ui.y1line.textChanged.connect(self.assemble_paths)

        self.ui.y1line.textChanged.connect(self.check_values)

        self.ui.comboBoxUnits.currentIndexChanged.connect(self.set_units)

        self.ui.comboBoxUnits.currentIndexChanged.connect(self.get_version)

        # Call the activated signal when the user clicks on any item (new or old) in the comboBox
        # [str] calls the overloaded signal that passes the Qstring, not the index of the item
        self.ui.version_comboBox.activated[str].connect(self.set_version)

        self.ui.driveLetter_comboBox.currentIndexChanged.connect(self.get_drive_letter)

        self.ui.browsejsonbutton.clicked.connect(self.browse_json)

        self.ui.browseoutputbutton.clicked.connect(self.browse_output)

        self.ui.browseardbutton.clicked.connect(self.browse_ard)

        self.ui.browseclassbutton.clicked.connect(self.browse_class)

        self.ui.browsejsonline.textChanged.connect(self.check_values)

        self.ui.browseARDline.textChanged.connect(self.check_values)

        self.ui.browseoutputline.textChanged.connect(self.check_values)

        self.ui.plotbutton.clicked.connect(self.plot)

        self.ui.plotbutton.clicked.connect(self.close_ard)

        self.ui.clearpushButton.clicked.connect(self.clear)

        self.ui.savefigpushButton.clicked.connect(self.save_fig)

        self.ui.exitbutton.clicked.connect(self.exit_plot)

        self.ui.clicked_listWidget.itemClicked.connect(self.show_ard)

        self.ui.mapButton.clicked.connect(self.show_maps)

        self.ui.pushLocator.clicked.connect(self.show_locator_map)

    def show_locator_map(self):
        """
        Open the Leaflet map for selecting a coordinate for plotting

        """
        self.leaflet_map.show()

    def get_drive_letter(self):
        """
        Obtain the drive letter that points to the eval server

        """
        self.drive_letter = self.ui.driveLetter_comboBox.currentText()

        log.info("Selected Drive Letter: %s" % self.drive_letter)

        # Assemble the paths to the required datasets with the version provided
        self.assemble_paths()

        # Get the PyCCD Versions now that the appropriate drive letter has been selected
        self.get_version()

        # Assemble the paths to the required datasets with the version provided
        self.assemble_paths()

        # Check that the fields are populated and activate the Plot button
        self.check_values()

    def get_version(self):
        """
        Make a list of available PyCCD versions that exist for the current point and add them to the version_comboBox

        """
        # Remove previous versions since they may not exist for the current coordinate
        self.ui.version_comboBox.clear()

        try:
            path = os.path.join(self.drive_letter + os.sep, 'bulk', 'tiles', self.tile, 'change')

            log.info("Looking for versions in %s" % path)

            versions_present = [c for c in os.listdir(path) if os.path.isdir(os.path.join(path, c))]

            log.info("PyCCD versions found: %s" % str(versions_present))

            for version in versions_present:
                self.ui.version_comboBox.addItem(version)

            self.version = self.ui.version_comboBox.currentText()

        except (FileNotFoundError, TypeError):

            pass

    def set_version(self, version):
        """
        Set the PyCCD version for creating a path to the JSON files and automatically update the path to the
        JSON directory with the selected version

        Args:
            version <QString> the text sent automatically

        """
        self.version = self.ui.version_comboBox.currentText()

        # Update the browsejsonline field with the selected version
        self.ui.browsejsonline.setText(os.path.join(self.drive_letter + os.sep,
                                                    'bulk', 'tiles', self.tile, 'change', str(version), 'json'))

        if str(self.version) == 'n-compare':
            self.end = dt.date(year=2017, month=12, day=31)

        else:
            self.end = dt.date(year=2015, month=12, day=31)

        log.debug("PyCCD Version=%s" % self.version)
        log.debug("End Date=%s" % self.end)

    def clear(self):
        """
        Clear the the list of clicked observations

        """
        self.ui.clicked_listWidget.clear()

    @staticmethod
    def get_time():
        """
        Return the current time stamp

        Returns:
            A formatted string containing the current date and time

        """
        return time.strftime("%Y%m%d-%I%M%S")

    def set_units(self):
        """
        Change the unit labels if the units are changed on the GUI, display the converted units if values are entered

        """
        self.selected_units = self.ui.comboBoxUnits.currentText()

        self.ui.label_x1.setText(units[self.selected_units]["label_x1"])

        self.ui.label_y1.setText(units[self.selected_units]["label_y1"])

        self.ui.label_x2.setText(units[self.selected_units]["label_x2"])

        self.ui.label_y2.setText(units[self.selected_units]["label_y2"])

        self.ui.label_units2.setText(units[self.selected_units]["label_unit2"])

        if len(self.ui.x1line.text()) > 0 and len(self.ui.y1line.text()) > 0:
            # <GeoCoordinate> containing the converted coordinates to display
            temp = GeoInfo.unit_conversion(coord=GeoInfo.get_geocoordinate(xstring=self.ui.x1line.text(),
                                                                           ystring=self.ui.y1line.text()),
                                           src=units[self.selected_units]["unit"],
                                           dest=units[self.ui.label_units2.text()]["unit"])

            self.ui.x2line.setText(str(temp.x))

            self.ui.y2line.setText(str(temp.y))

            if units[self.selected_units]["unit"] == "meters":
                geocoord = GeoInfo.get_geocoordinate(xstring=self.ui.x1line.text(),
                                                     ystring=self.ui.y1line.text())

            else:
                geocoord = GeoInfo.get_geocoordinate(xstring=self.ui.x2line.text(),
                                                     ystring=self.ui.y2line.text())

            h, v = GeoInfo.get_hv(geocoord.x, geocoord.y)

            self.tile = "h{:02}v{:02}".format(h, v)

    def fname_generator(self, ext=".png"):
        """
        Generate a string for an output file

        Args:
            ext: <str> The output file extension, default is .png

        Returns:
            <str> The full path to the output file name

        """
        return "{outdir}{sep}H{h}V{v}_{xy}_{t}{ext}".format(outdir=self.ui.browseoutputline.text(),
                                                            sep=os.sep,
                                                            h=self.geo_info.H,
                                                            v=self.geo_info.V,
                                                            xy=self.ui.x1line.text() + "_" + self.ui.y1line.text(),
                                                            t=self.get_time(),
                                                            ext=ext)

    def save_fig(self):
        """
        Save the current matplotlib figure to a PNG file

        """
        if not os.path.exists(self.ui.browseoutputline.text()):
            os.makedirs(self.ui.browseoutputline.text())

        fname = self.fname_generator()

        # Overwrite the .png if it already exists
        if os.path.exists(fname):
            try:
                os.remove(fname)

            except IOError:
                pass

        plt.savefig(fname, bbox_inches="tight", dpi=150)

        log.debug("Plot figure saved to file {}".format(fname))

    def assemble_paths(self):
        """
        Generate the paths to the various required data

        """
        try:
            self.ui.browseARDline.setText(os.path.join(self.drive_letter + os.sep, 'perf', 'production', self.tile))

            self.ui.browseclassline.setText(os.path.join(self.drive_letter + os.sep, 'bulk', 'tiles', self.tile,
                                                         'class', 'eval', 'pickles'))

            self.config = os.path.join(self.drive_letter + os.sep, 'bulk', 'lcmap_tap_config', 'config.yaml')

        except (FileNotFoundError, TypeError):
            pass

    def check_values(self):
        """
        Check to make sure all of the required parameters have been entered before enabling Plot

        """
        # <int> A container to keep track of how many parameters have been entered
        counter = 0

        # <list> List containing the text() values from each of the input widgets
        checks = [self.ui.browsejsonline.text(),
                  self.ui.browseardbutton.text(),
                  self.ui.browseclassline.text(),
                  self.ui.x1line.text(),
                  self.ui.y1line.text(),
                  self.ui.browseoutputline.text()]

        # Parse through the checks list to check for entered text
        for check in checks:
            if check == "":
                self.ui.plotbutton.setEnabled(False)

                self.ui.clearpushButton.setEnabled(False)

                self.ui.savefigpushButton.setEnabled(False)

            else:
                counter += 1

        # If all parameters are entered and valid, enable the plot button
        if counter == len(checks):
            self.ui.plotbutton.setEnabled(True)

    @staticmethod
    def check_path(name, path):
        """
        Check if the input path exists
        Args:
            name <str>: The path category (e.g. cache, json, ard)
            path <str>: A path on the system

        Returns:
            <bool>

        """
        if not os.path.exists(path):
            log.warning("The %s path %s cannot be found" % (name, path))

            return False

        else:
            return True

    def browse_ard(self):
        """
        Open QFileDialog to manually browse to the directory containing ARD tarballs

        """
        ard_directory = QFileDialog.getExistingDirectory(self)

        self.ui.browseARDline.setText(ard_directory)

    def browse_class(self):
        """
        Open a QFileDialog to manually browse to the directory containing class pickle files

        """
        class_dir = QFileDialog.getExistingDirectory(self)

        self.ui.browseclassline.setText(class_dir)

    def browse_json(self):
        """
        Open a QFileDialog to manually browse to and retrieve the full path to the PyCCD results directory

        """
        # <str> Full path to the directory containing PyCCD results (.json files)
        jsondir = QFileDialog.getExistingDirectory(self)

        self.ui.browsejsonline.setText(jsondir)

    def browse_output(self):
        """
        Open a QFileDialog to manually browse to and retrieve the full path to the output directory

        """
        # <str> Full path to the output directory, used for saving plot images
        output_dir = QFileDialog.getExistingDirectory(self)

        self.ui.browseoutputline.setText(output_dir)

    def show_model_params(self, results, geo):
        """
        Print the model results out to the GUI QPlainTextEdit widget

        Args:
            results: Class instance containing change model results and parameters
            geo: Class instance containing geographic info

        """
        # TODO Possibly add all logging output to QPlainTextEditor
        # self.ui.plainTextEdit_results.clear()

        log.info("Plotting for tile H{:02}V{:02} at point ({}, {}) meters".format(geo.H, geo.V,
                                                                                  geo.coord.x,
                                                                                  geo.coord.y))

        try:
            self.ui.plainTextEdit_results.appendPlainText("\n\nBegin Date: {}".format(results.begin))
            log.info("Begin Date: {}".format(results.begin))

            self.ui.plainTextEdit_results.appendPlainText("End Date: {}\n".format(results.end))
            log.info("End Date: {}".format(results.end))

            for num, result in enumerate(results.results["change_models"]):
                self.ui.plainTextEdit_results.appendPlainText("Result: {}".format(num + 1))
                log.info("Result: {}".format(num + 1))

                self.ui.plainTextEdit_results.appendPlainText(
                    "Start Date: {}".format(dt.datetime.fromordinal(result["start_day"])))
                log.info("Start Date: {}".format(dt.datetime.fromordinal(result["start_day"])))

                self.ui.plainTextEdit_results.appendPlainText(
                    "End Date: {}".format(dt.datetime.fromordinal(result["end_day"])))
                log.info("End Date: {}".format(dt.datetime.fromordinal(result["end_day"])))

                self.ui.plainTextEdit_results.appendPlainText(
                    "Break Date: {}".format(dt.datetime.fromordinal(result["break_day"])))
                log.info("Break Date: {}".format(dt.datetime.fromordinal(result["break_day"])))

                self.ui.plainTextEdit_results.appendPlainText("QA: {}".format(result["curve_qa"]))
                log.info("QA: {}".format(result["curve_qa"]))

                self.ui.plainTextEdit_results.appendPlainText("Change prob: {}\n".format(result["change_probability"]))
                log.info("Change prob: {}".format(result["change_probability"]))

        except ValueError:
            pass

    def plot(self):
        """
        TODO: Add descriptive information

        """
        self.dirs = {"json": self.ui.browsejsonline.text(),
                     "ard": self.ui.browseARDline.text(),
                     "class": self.ui.browseclassline.text()}

        for key, value in self.dirs.items():
            if not self.check_path(key, value):
                return None

        if self.plot_window:
            self.plot_window.close()

        # <list> The bands and/or indices selected for plotting
        self.item_list = [str(i.text()) for i in self.ui.listitems.selectedItems()]

        # If there is a problem with any of the parameters, the first erroneous parameter
        # will cause an exception to occur which will be displayed in the GUI for the user, but the tool won't close.
        try:
            self.geo_info = GeoInfo(x=self.ui.x1line.text(),
                                    y=self.ui.y1line.text(),
                                    units=units[self.selected_units]["unit"])

            self.cache_data = read_cache(self.geo_info, self.cache_data)

            self.qt_handler.set_active(True)

            self.ard_observations = ARDData(geo=self.geo_info,
                                            config=self.config,
                                            items=self.item_list,
                                            cache=self.cache_data,
                                            controls=self)

            self.qt_handler.set_active(False)

            self.cache_data = update_cache(self.cache_data, self.ard_observations.cache, self.ard_observations.key)

            self.ccd_results = CCDReader(tile=self.geo_info.tile,
                                         chip_coord=self.geo_info.chip_coord,
                                         pixel_coord=self.geo_info.pixel_coord,
                                         json_dir=self.dirs["json"])

            self.class_results = SegmentClasses(chip_coord=self.geo_info.chip_coord,
                                                class_dir=self.dirs["class"],
                                                rc=self.geo_info.chip_pixel_rowcol,
                                                tile=self.geo_info.tile)

            self.plot_specs = PlotSpecs(ard=self.ard_observations.pixel_ard,
                                        change=self.ccd_results.results,
                                        segs=self.class_results.results,
                                        begin=self.begin,
                                        end=self.end)

            # self.ard_http = lcmaphttp.LCMAPHTTP(self.config)

        except (IndexError, AttributeError, TypeError, ValueError) as e:
            # Clear the results window
            self.ui.plainTextEdit_results.clear()

            # Show which exception was raised
            self.ui.plainTextEdit_results.appendPlainText("***Plotting Error***\
                                                          \n\nType of Exception: {}\
                                                          \nException Value: {}\
                                                          \nTraceback Info: {}".format(sys.exc_info()[0],
                                                                                       sys.exc_info()[1],
                                                                                       traceback.print_tb(
                                                                                           sys.exc_info()[2])))

            log.error("Plotting Raised Exception: ")
            log.error(e, exc_info=True)

            return None

        self.ard_specs = ARDInfo(root=self.ui.browseARDline.text(),
                                 h=self.geo_info.H,
                                 v=self.geo_info.V)

        # Display change model information for the entered coordinates
        self.show_model_params(results=self.plot_specs, geo=self.geo_info)

        """
        fig <matplotlib.figure> Matplotlib figure object containing all of the artists
        
        artist_map <dict> mapping of each specific PathCollection artist to it's underlying dataset
        
        lines_map <dict> mapping of artist lines and points to the legend lines
        
        axes <ndarray> 2D array of matplotlib.axes.Axes objects
        """
        self.fig, self.artist_map, self.lines_map, self.axes = make_plots.draw_figure(data=self.plot_specs,
                                                                                      items=self.item_list)

        if not os.path.exists(self.ui.browseoutputline.text()):
            os.makedirs(self.ui.browseoutputline.text())

        # <bool> If True, generate a point shapefile for the entered coordinates
        shp_on = self.ui.radioshp.isChecked()

        # Generate the ESRI point shapefile
        if shp_on is True:
            temp_shp = self.fname_generator(ext=".shp")
            root, name = os.path.split(temp_shp)
            root = root + os.sep + "shp"

            self.get_shp(coords=self.geo_info.coord,
                         out_shp="{}{}{}".format(root, os.sep, name))

        # Show the figure in an interactive window
        self.plot_window = PlotWindow(fig=self.fig,
                                      axes=self.axes,
                                      artist_map=self.artist_map,
                                      lines_map=self.lines_map,
                                      gui=self,
                                      scenes=get_image_ids(path=self.dirs["ard"]))

        # Make these buttons available once a figure has been created
        self.ui.clearpushButton.setEnabled(True)

        self.ui.savefigpushButton.setEnabled(True)

        self.ui.mapButton.setEnabled(True)

    @staticmethod
    def get_shp(coords, out_shp):
        """
        Create a point shapefile at the (x, y) coordinates
        Args:
            coords: <GeoCoordinate> 
            out_shp: <str> Contains a root path and filename for the output shapefile

        """
        if not os.path.exists(os.path.split(out_shp)[0]):
            try:
                os.makedirs(os.path.split(out_shp)[0])

            except PermissionError as e:

                log.warning("Generating shapefile raised exception: ")
                log.warning(e, exc_info=True)

                return None

        layer_name = os.path.splitext(os.path.split(out_shp)[-1])[0]

        # Set up driver
        driver = ogr.GetDriverByName("ESRI Shapefile")

        # Create data source
        data_source = driver.CreateDataSource(out_shp)

        # Create a SpatialReference() object and import the pre-defined well-known text
        srs = osr.SpatialReference()
        srs.ImportFromWkt(projections.AEA_WKT)

        # Create layer, add fields to contain x and y coordinates
        layer = data_source.CreateLayer(layer_name, srs)
        layer.CreateField(ogr.FieldDefn("X", ogr.OFTReal))
        layer.CreateField(ogr.FieldDefn("Y", ogr.OFTReal))

        # Create feature, populate X and Y fields
        feature = ogr.Feature(layer.GetLayerDefn())
        feature.SetField("X", coords.x)
        feature.SetField("Y", coords.y)

        # Create the Well Known Text containing the point feature location
        wkt = "POINT(%f %f)" % (coords.x, coords.y)

        # Create a point from the Well Known Text
        point = ogr.CreateGeometryFromWkt(wkt)

        # Set feature geometry to point-type
        feature.SetGeometry(point)

        # Create the feature in the layer
        layer.CreateFeature(feature)

    def show_ard(self, clicked_item):
        """
        Display the ARD image clicked on the plot

        Args:
            clicked_item: <QListWidgetItem> Passed automatically by the itemClicked method of the QListWidget

        Returns:
            None
        """
        try:
            # Don't include the processing date in the scene ID
            sceneID = clicked_item.text().split()[2][:23]

            scene_files = self.ard_specs.vsipaths[sceneID]

            sensor = self.ard_specs.get_sensor(sceneID)

            if not self.ard:
                self.ard = ARDViewerX(ard_file=scene_files[0:7],
                                      geo=self.geo_info,
                                      sensor=sensor,
                                      gui=self,  # Provide backwards interactions with the main GUI
                                      # Send the previous view rectangle to the new image
                                      # current_view=self.current_view
                                      )

            else:
                self.ard.ard_file = scene_files[0:7]

                self.ard.sensor = sensor

                self.ard.read_data()

                self.ard.get_rgb()

                self.ard.display_img()

        except (AttributeError, IndexError) as e:
            log.warning("Display ARD raised an exception: ")
            log.warning(e, exc_info=True)

    def close_ard(self):
        """
        If plotting for a new HV tile, close the previous ARD Viewer window if one was previously opened

        Returns:
            None

        """
        try:
            self.ard.exit()

        except AttributeError:
            pass

    def show_maps(self):
        """
        Display the mapped products viewer

        """
        path = os.path.join(self.drive_letter + os.sep, 'bulk', 'tiles', self.tile, 'eval')

        if self.ard_specs:
            self.maps_window = MapsViewer(tile=self.ard_specs.tile_name, root=path, geo=self.geo_info,
                                          version=self.version)

    def exit_plot(self):
        """
        Close all TAP tool windows and exit the program

        """
        save_cache(self.cache_data)

        log.info("Exiting TAP Tool")

        sys.exit(0)

    def closeEvent(self, event):
        """
        Override method if the GUI is closed but 'Close' button is not used

        Args:
            event:

        Returns:

        """
        self.exit_plot()
