# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 213)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 216))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 8, 1, 1, 1)
        self.widget_lineedit_movement_variance = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.widget_lineedit_movement_variance.setObjectName("widget_lineedit_movement_variance")
        self.gridLayout.addWidget(self.widget_lineedit_movement_variance, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.widget_lineedit_movement_speed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.widget_lineedit_movement_speed.setObjectName("widget_lineedit_movement_speed")
        self.gridLayout.addWidget(self.widget_lineedit_movement_speed, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.widget_lineedit_run_frequency = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.widget_lineedit_run_frequency.setObjectName("widget_lineedit_run_frequency")
        self.gridLayout.addWidget(self.widget_lineedit_run_frequency, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.widget_lineedit_click_speed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.widget_lineedit_click_speed.setObjectName("widget_lineedit_click_speed")
        self.gridLayout.addWidget(self.widget_lineedit_click_speed, 4, 1, 1, 1)
        self.widget_lineedit_click_variance = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.widget_lineedit_click_variance.setObjectName("widget_lineedit_click_variance")
        self.gridLayout.addWidget(self.widget_lineedit_click_variance, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "click variance"))
        self.label_2.setText(_translate("Dialog", "movement variance"))
        self.label_3.setText(_translate("Dialog", "click speed"))
        self.label.setText(_translate("Dialog", "movement speed"))
        self.label_5.setText(_translate("Dialog", "run frequency"))

