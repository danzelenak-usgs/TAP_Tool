# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MAIN.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pkg_resources

class Ui_MainWindow_tap(object):
    def setupUi(self, MainWindow_tap):
        MainWindow_tap.setObjectName("MainWindow_tap")
        MainWindow_tap.resize(612, 597)

        icon = QtGui.QIcon(QtGui.QPixmap(pkg_resources.resource_filename("lcmap_tap",
                                                                         "/".join(("Auxiliary", "icon.PNG")))))

        MainWindow_tap.setWindowIcon(icon)
        MainWindow_tap.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow_tap)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GridLayout_coordinates = QtWidgets.QGridLayout()
        self.GridLayout_coordinates.setObjectName("GridLayout_coordinates")
        self.LineEdit_y1 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_y1.setMinimumSize(QtCore.QSize(85, 0))
        self.LineEdit_y1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineEdit_y1.setMaxLength(16)
        self.LineEdit_y1.setObjectName("LineEdit_y1")
        self.GridLayout_coordinates.addWidget(self.LineEdit_y1, 1, 1, 1, 1)
        self.Label_x1 = QtWidgets.QLabel(self.centralwidget)
        self.Label_x1.setMaximumSize(QtCore.QSize(125, 16777215))
        self.Label_x1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Label_x1.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_x1.setObjectName("Label_x1")
        self.GridLayout_coordinates.addWidget(self.Label_x1, 0, 0, 1, 1)
        self.ComboBox_units = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboBox_units.sizePolicy().hasHeightForWidth())
        self.ComboBox_units.setSizePolicy(sizePolicy)
        self.ComboBox_units.setMaximumSize(QtCore.QSize(300, 16777215))
        self.ComboBox_units.setObjectName("ComboBox_units")
        self.ComboBox_units.addItem("")
        self.ComboBox_units.addItem("")
        self.GridLayout_coordinates.addWidget(self.ComboBox_units, 1, 2, 1, 1)
        self.LineEdit_x2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_x2.setEnabled(True)
        self.LineEdit_x2.setMinimumSize(QtCore.QSize(85, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.LineEdit_x2.setPalette(palette)
        self.LineEdit_x2.setAutoFillBackground(False)
        self.LineEdit_x2.setDragEnabled(False)
        self.LineEdit_x2.setReadOnly(True)
        self.LineEdit_x2.setObjectName("LineEdit_x2")
        self.GridLayout_coordinates.addWidget(self.LineEdit_x2, 3, 0, 1, 1)
        self.Label_y2 = QtWidgets.QLabel(self.centralwidget)
        self.Label_y2.setObjectName("Label_y2")
        self.GridLayout_coordinates.addWidget(self.Label_y2, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.LineEdit_x1 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_x1.setMinimumSize(QtCore.QSize(85, 0))
        self.LineEdit_x1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LineEdit_x1.setMaxLength(16)
        self.LineEdit_x1.setObjectName("LineEdit_x1")
        self.GridLayout_coordinates.addWidget(self.LineEdit_x1, 1, 0, 1, 1)
        self.Label_convertedUnits = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        self.Label_convertedUnits.setPalette(palette)
        self.Label_convertedUnits.setObjectName("Label_convertedUnits")
        self.GridLayout_coordinates.addWidget(self.Label_convertedUnits, 3, 2, 1, 1)
        self.Label_x2 = QtWidgets.QLabel(self.centralwidget)
        self.Label_x2.setObjectName("Label_x2")
        self.GridLayout_coordinates.addWidget(self.Label_x2, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Label_units = QtWidgets.QLabel(self.centralwidget)
        self.Label_units.setObjectName("Label_units")
        self.GridLayout_coordinates.addWidget(self.Label_units, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.Label_y1 = QtWidgets.QLabel(self.centralwidget)
        self.Label_y1.setMaximumSize(QtCore.QSize(125, 16777215))
        self.Label_y1.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_y1.setObjectName("Label_y1")
        self.GridLayout_coordinates.addWidget(self.Label_y1, 0, 1, 1, 1)
        self.LineEdit_y2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_y2.setEnabled(True)
        self.LineEdit_y2.setMinimumSize(QtCore.QSize(85, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.LineEdit_y2.setPalette(palette)
        self.LineEdit_y2.setReadOnly(True)
        self.LineEdit_y2.setObjectName("LineEdit_y2")
        self.GridLayout_coordinates.addWidget(self.LineEdit_y2, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.GridLayout_coordinates, 0, 0, 1, 1)
        self.HBoxLayout_buttons = QtWidgets.QHBoxLayout()
        self.HBoxLayout_buttons.setObjectName("HBoxLayout_buttons")
        self.PushButton_locator = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton_locator.sizePolicy().hasHeightForWidth())
        self.PushButton_locator.setSizePolicy(sizePolicy)
        self.PushButton_locator.setMinimumSize(QtCore.QSize(75, 0))
        self.PushButton_locator.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PushButton_locator.setObjectName("PushButton_locator")
        self.HBoxLayout_buttons.addWidget(self.PushButton_locator)
        self.PushButton_plot = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_plot.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton_plot.sizePolicy().hasHeightForWidth())
        self.PushButton_plot.setSizePolicy(sizePolicy)
        self.PushButton_plot.setMinimumSize(QtCore.QSize(75, 0))
        self.PushButton_plot.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PushButton_plot.setObjectName("PushButton_plot")
        self.HBoxLayout_buttons.addWidget(self.PushButton_plot)
        self.PushButton_saveFigure = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_saveFigure.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton_saveFigure.sizePolicy().hasHeightForWidth())
        self.PushButton_saveFigure.setSizePolicy(sizePolicy)
        self.PushButton_saveFigure.setMinimumSize(QtCore.QSize(75, 0))
        self.PushButton_saveFigure.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PushButton_saveFigure.setObjectName("PushButton_saveFigure")
        self.HBoxLayout_buttons.addWidget(self.PushButton_saveFigure)
        self.PushButton_export = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_export.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton_export.sizePolicy().hasHeightForWidth())
        self.PushButton_export.setSizePolicy(sizePolicy)
        self.PushButton_export.setMinimumSize(QtCore.QSize(75, 0))
        self.PushButton_export.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PushButton_export.setObjectName("PushButton_export")
        self.HBoxLayout_buttons.addWidget(self.PushButton_export)
        self.PushButton_savesession = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_savesession.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton_savesession.sizePolicy().hasHeightForWidth())
        self.PushButton_savesession.setSizePolicy(sizePolicy)
        self.PushButton_savesession.setMinimumSize(QtCore.QSize(90, 0))
        self.PushButton_savesession.setMaximumSize(QtCore.QSize(90, 16777215))
        self.PushButton_savesession.setObjectName("PushButton_savesession")
        self.HBoxLayout_buttons.addWidget(self.PushButton_savesession)
        self.PushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_clear.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton_clear.sizePolicy().hasHeightForWidth())
        self.PushButton_clear.setSizePolicy(sizePolicy)
        self.PushButton_clear.setMinimumSize(QtCore.QSize(75, 0))
        self.PushButton_clear.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PushButton_clear.setObjectName("PushButton_clear")
        self.HBoxLayout_buttons.addWidget(self.PushButton_clear)
        self.PushButton_close = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton_close.sizePolicy().hasHeightForWidth())
        self.PushButton_close.setSizePolicy(sizePolicy)
        self.PushButton_close.setMinimumSize(QtCore.QSize(75, 0))
        self.PushButton_close.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PushButton_close.setObjectName("PushButton_close")
        self.HBoxLayout_buttons.addWidget(self.PushButton_close)
        self.gridLayout_3.addLayout(self.HBoxLayout_buttons, 5, 0, 1, 1)
        self.VBoxLayout_main = QtWidgets.QVBoxLayout()
        self.VBoxLayout_main.setObjectName("VBoxLayout_main")
        self.Label_outputDir = QtWidgets.QLabel(self.centralwidget)
        self.Label_outputDir.setObjectName("Label_outputDir")
        self.VBoxLayout_main.addWidget(self.Label_outputDir)
        self.HBoxLayout_outputDir = QtWidgets.QHBoxLayout()
        self.HBoxLayout_outputDir.setObjectName("HBoxLayout_outputDir")
        self.LineEdit_outputDir = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_outputDir.setObjectName("LineEdit_outputDir")
        self.HBoxLayout_outputDir.addWidget(self.LineEdit_outputDir)
        self.PushButton_outputDir = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_outputDir.setMinimumSize(QtCore.QSize(35, 0))
        self.PushButton_outputDir.setMaximumSize(QtCore.QSize(25, 16777215))
        self.PushButton_outputDir.setObjectName("PushButton_outputDir")
        self.HBoxLayout_outputDir.addWidget(self.PushButton_outputDir)
        self.VBoxLayout_main.addLayout(self.HBoxLayout_outputDir)
        self.ListWidget_items = QtWidgets.QListWidget(self.centralwidget)
        self.ListWidget_items.setAlternatingRowColors(False)
        self.ListWidget_items.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.ListWidget_items.setObjectName("ListWidget_items")
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ListWidget_items.addItem(item)
        self.VBoxLayout_main.addWidget(self.ListWidget_items)
        self.Label_results = QtWidgets.QLabel(self.centralwidget)
        self.Label_results.setObjectName("Label_results")
        self.VBoxLayout_main.addWidget(self.Label_results)
        self.PlainTextEdit_results = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.PlainTextEdit_results.setReadOnly(True)
        self.PlainTextEdit_results.setObjectName("PlainTextEdit_results")
        self.VBoxLayout_main.addWidget(self.PlainTextEdit_results)
        self.Label_selected = QtWidgets.QLabel(self.centralwidget)
        self.Label_selected.setObjectName("Label_selected")
        self.VBoxLayout_main.addWidget(self.Label_selected)
        self.ListWidget_selected = QtWidgets.QListWidget(self.centralwidget)
        self.ListWidget_selected.setAlternatingRowColors(True)
        self.ListWidget_selected.setObjectName("ListWidget_selected")
        self.VBoxLayout_main.addWidget(self.ListWidget_selected)
        self.gridLayout_3.addLayout(self.VBoxLayout_main, 4, 0, 1, 1)
        MainWindow_tap.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_tap)
        self.statusbar.setObjectName("statusbar")
        MainWindow_tap.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_tap)
        self.ComboBox_units.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_tap)
        MainWindow_tap.setTabOrder(self.LineEdit_x1, self.LineEdit_y1)
        MainWindow_tap.setTabOrder(self.LineEdit_y1, self.ComboBox_units)
        MainWindow_tap.setTabOrder(self.ComboBox_units, self.LineEdit_outputDir)
        MainWindow_tap.setTabOrder(self.LineEdit_outputDir, self.PushButton_outputDir)
        MainWindow_tap.setTabOrder(self.PushButton_outputDir, self.PushButton_plot)
        MainWindow_tap.setTabOrder(self.PushButton_plot, self.PushButton_saveFigure)
        MainWindow_tap.setTabOrder(self.PushButton_saveFigure, self.ListWidget_selected)
        MainWindow_tap.setTabOrder(self.ListWidget_selected, self.PlainTextEdit_results)
        MainWindow_tap.setTabOrder(self.PlainTextEdit_results, self.LineEdit_y2)
        MainWindow_tap.setTabOrder(self.LineEdit_y2, self.LineEdit_x2)

    def retranslateUi(self, MainWindow_tap):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_tap.setWindowTitle(_translate("MainWindow_tap", "Time Series Analysis and Plotting Tool"))
        self.Label_x1.setText(_translate("MainWindow_tap", "X (meters)"))
        self.ComboBox_units.setCurrentText(_translate("MainWindow_tap", "Projected Meters - Albers CONUS WGS 84"))
        self.ComboBox_units.setItemText(0, _translate("MainWindow_tap", "Projected Meters - Albers CONUS WGS 84"))
        self.ComboBox_units.setItemText(1, _translate("MainWindow_tap", "Geographic Lat/Long - Decimal Degrees WGS 84"))
        self.Label_y2.setText(_translate("MainWindow_tap", "Lat (dec. deg.)"))
        self.Label_convertedUnits.setText(_translate("MainWindow_tap", "Geographic  Lat/Long - Decimal Degrees WGS 84"))
        self.Label_x2.setText(_translate("MainWindow_tap", "Long (dec. deg.)"))
        self.Label_units.setText(_translate("MainWindow_tap", "Units"))
        self.Label_y1.setText(_translate("MainWindow_tap", "Y (meters)"))
        self.PushButton_locator.setText(_translate("MainWindow_tap", "Locator Map"))
        self.PushButton_plot.setText(_translate("MainWindow_tap", "Plot"))
        self.PushButton_saveFigure.setText(_translate("MainWindow_tap", "Save Figure"))
        self.PushButton_export.setText(_translate("MainWindow_tap", "Export"))
        self.PushButton_savesession.setText(_translate("MainWindow_tap", "Save Session"))
        self.PushButton_clear.setText(_translate("MainWindow_tap", "Clear"))
        self.PushButton_close.setText(_translate("MainWindow_tap", "Close"))
        self.Label_outputDir.setText(_translate("MainWindow_tap", "Specify working directory:"))
        self.PushButton_outputDir.setText(_translate("MainWindow_tap", "..."))
        __sortingEnabled = self.ListWidget_items.isSortingEnabled()
        self.ListWidget_items.setSortingEnabled(False)
        item = self.ListWidget_items.item(0)
        item.setText(_translate("MainWindow_tap", "All Spectral Bands"))
        item = self.ListWidget_items.item(1)
        item.setText(_translate("MainWindow_tap", "All Indices"))
        item = self.ListWidget_items.item(2)
        item.setText(_translate("MainWindow_tap", "Blue"))
        item = self.ListWidget_items.item(3)
        item.setText(_translate("MainWindow_tap", "Green"))
        item = self.ListWidget_items.item(4)
        item.setText(_translate("MainWindow_tap", "Red"))
        item = self.ListWidget_items.item(5)
        item.setText(_translate("MainWindow_tap", "NIR"))
        item = self.ListWidget_items.item(6)
        item.setText(_translate("MainWindow_tap", "SWIR-1"))
        item = self.ListWidget_items.item(7)
        item.setText(_translate("MainWindow_tap", "SWIR-2"))
        item = self.ListWidget_items.item(8)
        item.setText(_translate("MainWindow_tap", "Thermal"))
        item = self.ListWidget_items.item(9)
        item.setText(_translate("MainWindow_tap", "NDVI"))
        item = self.ListWidget_items.item(10)
        item.setText(_translate("MainWindow_tap", "MSAVI"))
        item = self.ListWidget_items.item(11)
        item.setText(_translate("MainWindow_tap", "EVI"))
        item = self.ListWidget_items.item(12)
        item.setText(_translate("MainWindow_tap", "SAVI"))
        item = self.ListWidget_items.item(13)
        item.setText(_translate("MainWindow_tap", "NDMI"))
        item = self.ListWidget_items.item(14)
        item.setText(_translate("MainWindow_tap", "NBR"))
        item = self.ListWidget_items.item(15)
        item.setText(_translate("MainWindow_tap", "NBR-2"))
        self.ListWidget_items.setSortingEnabled(__sortingEnabled)
        self.Label_results.setText(_translate("MainWindow_tap", "Model Results:"))
        self.Label_selected.setText(_translate("MainWindow_tap", "Selected Observations:"))

