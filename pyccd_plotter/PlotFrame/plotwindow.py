
import datetime as dt

import matplotlib
import numpy as np
from PyQt5 import QtWidgets

matplotlib.use("Qt5Agg")

from matplotlib.collections import PathCollection

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class MplCanvas(FigureCanvas):
    def __init__(self, fig):
        self.fig = fig

        FigureCanvas.__init__(self, self.fig)

        if len(fig.axes) >= 3:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        FigureCanvas.setSizePolicy(self, sizePolicy)

        FigureCanvas.updateGeometry(self)


class PlotWindow(QtWidgets.QMainWindow):
    def __init__(self, fig, artist_map, lines_map, gui, scenes, parent=None):

        super(PlotWindow, self).__init__(parent)

        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
        self.widget.layout().setSpacing(0)

        self.fig = fig
        self.canvas = MplCanvas(fig=self.fig)
        self.canvas.draw()

        # Create a mutable object to contain the information pulled by the point_pick method
        self.value_holder = {}

        # Define a picker method to grab data off of the plot wherever the mouse cursor is when clicked
        def point_pick(event):
            """
            Return the x_data and y_data for the selected artist using a mouse click event
            :param event:
            :return:
            """
            # References useful information about the pick location
            mouseevent = event.mouseevent

            # This references which object on the plot was hit by the pick
            artist = event.artist

            # Only works using left-click (event.mouseevent.button==1)
            # and on any of the scatter point series (PathCollection artists)
            if isinstance(artist, PathCollection) and mouseevent.button == 1:
                # Return the index value of the artist (i.e. which data point in the series was hit)
                ind = event.ind

                # Retrieve the appropriate data series based on the clicked artist
                x = artist_map[artist][0]
                y = artist_map[artist][1]
                b = artist_map[artist][2]

                try:
                    # Grab the date value at the clicked point
                    click_x = dt.datetime.fromordinal(int(mouseevent.xdata))

                    point_clicked = [click_x, mouseevent.ydata]

                    # Retrieve the x-y data for the plotted point within a set tolerance to the
                    # clicked point if there is one
                    nearest_x = dt.datetime.fromordinal(int(np.take(x, ind)))
                    nearest_y = np.take(y, ind)

                    artist_data = [nearest_x, nearest_y]

                    print("point clicked: {}\n\
                          nearest artist: {}\n\
                          subplot: {}".format(point_clicked, self.value_holder, b))

                    self.value_holder["temp"] = [point_clicked, artist_data]

                    test_str = "{:%Y%m%d}".format(self.value_holder["temp"][1][0])

                    # Look through the scene IDs to find which one corresponds to the selected obs. date
                    for id in scenes:
                        if test_str in id:
                            self.value_holder["temp"].append(id)

                            gui.ui.plainTextEdit_click.appendPlainText("Scene ID: {}".format(id))

                    # Show the picked information in a text box on the GUI
                    gui.ui.plainTextEdit_click.appendPlainText(
                        "Obs. Date: {:%Y-%b-%d} \n{}-Value: {}\n".format(self.value_holder['temp'][1][0],
                                                                         b,
                                                                         self.value_holder['temp'][1][1][0]))

                # I think the TypeError might occur when more than a single data point is returned with one click,
                # but need to investigate further.
                except TypeError:
                    pass

            else:
                # Do this so nothing happens when the other mouse buttons are clicked while over a plot
                return False, dict()

        # Define a picker method that allows toggling lines on/off by clicking the legend
        def leg_pick(event):
            """

            :param event:
            :return:
            """
            mouseevent = event.mouseevent

            # Only want this to work if the left mouse button is clicked
            if mouseevent.button == 1:

                try:
                    legline = event.artist

                    # The origlines is a list of lines mapped to the legline for that particular subplot
                    origlines = lines_map[legline]

                    for l in origlines:

                        # Reference the opposite of the line's current visibility
                        vis = not l.get_visible()

                        # Make it so
                        l.set_visible(vis)

                        # Change the transparency of the picked object in the legend so the user can see explicitly
                        # which items are turned on/off.  This doesn't work for the points in the legend currently.
                        if vis:
                            legline.set_alpha(1.0)

                        else:
                            legline.set_alpha(0.2)

                    # Redraw the canvas with the line or points turned on/off
                    self.canvas.draw()

                except KeyError:
                    return False, dict()

            else:
                return False, dict()

        self.nav = NavigationToolbar(self.canvas, self.widget)

        self.widget.layout().addWidget(self.nav)

        self.widget.layout().addWidget(self.canvas)

        self.scroll = QtWidgets.QScrollArea(self.widget)
        self.scroll.setWidgetResizable(True)

        self.scroll.setWidget(self.canvas)

        self.widget.layout().addWidget(self.scroll)

        self.canvas.mpl_connect("pick_event", point_pick)

        self.canvas.mpl_connect("pick_event", leg_pick)

        self.show()