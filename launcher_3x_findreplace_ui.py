# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher_3x_findreplace.ui'
#
# Created: Sat May 11 19:03:48 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_findReplace(object):
    def setupUi(self, findReplace):
        findReplace.setObjectName(_fromUtf8("findReplace"))
        findReplace.resize(300, 135)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(findReplace.sizePolicy().hasHeightForWidth())
        findReplace.setSizePolicy(sizePolicy)
        findReplace.setMinimumSize(QtCore.QSize(300, 135))
        findReplace.setMaximumSize(QtCore.QSize(500, 135))
        self.gridLayout = QtGui.QGridLayout(findReplace)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(findReplace)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(findReplace)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtGui.QLabel(findReplace)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.fr_ok = QtGui.QPushButton(findReplace)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_ok.sizePolicy().hasHeightForWidth())
        self.fr_ok.setSizePolicy(sizePolicy)
        self.fr_ok.setObjectName(_fromUtf8("fr_ok"))
        self.gridLayout.addWidget(self.fr_ok, 4, 2, 1, 1)
        self.fr_replace = QtGui.QLineEdit(findReplace)
        self.fr_replace.setObjectName(_fromUtf8("fr_replace"))
        self.gridLayout.addWidget(self.fr_replace, 3, 1, 1, 3)
        self.fr_cancel = QtGui.QPushButton(findReplace)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_cancel.sizePolicy().hasHeightForWidth())
        self.fr_cancel.setSizePolicy(sizePolicy)
        self.fr_cancel.setObjectName(_fromUtf8("fr_cancel"))
        self.gridLayout.addWidget(self.fr_cancel, 4, 3, 1, 1)
        self.fr_type = QtGui.QComboBox(findReplace)
        self.fr_type.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fr_type.setObjectName(_fromUtf8("fr_type"))
        self.fr_type.addItem(_fromUtf8(""))
        self.fr_type.addItem(_fromUtf8(""))
        self.fr_type.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.fr_type, 0, 1, 1, 2)
        self.fr_find = QtGui.QLineEdit(findReplace)
        self.fr_find.setObjectName(_fromUtf8("fr_find"))
        self.gridLayout.addWidget(self.fr_find, 1, 1, 1, 3)

        self.retranslateUi(findReplace)
        QtCore.QObject.connect(self.fr_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), findReplace.close)
        QtCore.QMetaObject.connectSlotsByName(findReplace)
        findReplace.setTabOrder(self.fr_type, self.fr_find)
        findReplace.setTabOrder(self.fr_find, self.fr_replace)
        findReplace.setTabOrder(self.fr_replace, self.fr_ok)
        findReplace.setTabOrder(self.fr_ok, self.fr_cancel)

    def retranslateUi(self, findReplace):
        findReplace.setWindowTitle(_translate("findReplace", "Database Find/Replace", None))
        self.label_3.setText(_translate("findReplace", "Data Column:", None))
        self.label_2.setText(_translate("findReplace", "Replace with:", None))
        self.label.setText(_translate("findReplace", "Find what:", None))
        self.fr_ok.setText(_translate("findReplace", "OK", None))
        self.fr_cancel.setText(_translate("findReplace", "Cancel", None))
        self.fr_type.setItemText(0, _translate("findReplace", "App Path", None))
        self.fr_type.setItemText(1, _translate("findReplace", "App Name", None))
        self.fr_type.setItemText(2, _translate("findReplace", "Group Name", None))


class findReplace(QtGui.QWidget, Ui_findReplace):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

