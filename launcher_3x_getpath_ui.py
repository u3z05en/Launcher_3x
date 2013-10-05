# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher_3x_getpath.ui'
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

class Ui_getPath(object):
    def setupUi(self, getPath):
        getPath.setObjectName(_fromUtf8("getPath"))
        getPath.setWindowModality(QtCore.Qt.ApplicationModal)
        getPath.resize(429, 443)
        getPath.setMouseTracking(True)
        getPath.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.gridLayout = QtGui.QGridLayout(getPath)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_locate = QtGui.QPushButton(getPath)
        self.button_locate.setObjectName(_fromUtf8("button_locate"))
        self.gridLayout.addWidget(self.button_locate, 1, 3, 1, 1)
        self.button_cancel = QtGui.QPushButton(getPath)
        self.button_cancel.setObjectName(_fromUtf8("button_cancel"))
        self.gridLayout.addWidget(self.button_cancel, 3, 3, 1, 1)
        self.label = QtGui.QLabel(getPath)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.button_ok = QtGui.QPushButton(getPath)
        self.button_ok.setObjectName(_fromUtf8("button_ok"))
        self.gridLayout.addWidget(self.button_ok, 3, 2, 1, 1)
        self.edit_path = QtGui.QLineEdit(getPath)
        self.edit_path.setMinimumSize(QtCore.QSize(300, 0))
        self.edit_path.setObjectName(_fromUtf8("edit_path"))
        self.gridLayout.addWidget(self.edit_path, 1, 0, 1, 3)
        self.tabWidget_examples = QtGui.QTabWidget(getPath)
        self.tabWidget_examples.setObjectName(_fromUtf8("tabWidget_examples"))
        self.tab_windows = QtGui.QWidget()
        self.tab_windows.setObjectName(_fromUtf8("tab_windows"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_windows)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_windows)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_2.addWidget(self.pushButton_5, 5, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.tab_windows)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_2.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.pushButton_1 = QtGui.QPushButton(self.tab_windows)
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.gridLayout_2.addWidget(self.pushButton_1, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab_windows)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.tab_windows)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.tab_windows)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab_windows)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.tabWidget_examples.addTab(self.tab_windows, _fromUtf8(""))
        self.tab_linux = QtGui.QWidget()
        self.tab_linux.setObjectName(_fromUtf8("tab_linux"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_linux)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_06 = QtGui.QPushButton(self.tab_linux)
        self.pushButton_06.setObjectName(_fromUtf8("pushButton_06"))
        self.gridLayout_3.addWidget(self.pushButton_06, 6, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_linux)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton_03 = QtGui.QPushButton(self.tab_linux)
        self.pushButton_03.setObjectName(_fromUtf8("pushButton_03"))
        self.gridLayout_3.addWidget(self.pushButton_03, 3, 0, 1, 1)
        self.pushButton_01 = QtGui.QPushButton(self.tab_linux)
        self.pushButton_01.setObjectName(_fromUtf8("pushButton_01"))
        self.gridLayout_3.addWidget(self.pushButton_01, 1, 0, 1, 1)
        self.pushButton_04 = QtGui.QPushButton(self.tab_linux)
        self.pushButton_04.setObjectName(_fromUtf8("pushButton_04"))
        self.gridLayout_3.addWidget(self.pushButton_04, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 7, 0, 1, 1)
        self.pushButton_02 = QtGui.QPushButton(self.tab_linux)
        self.pushButton_02.setObjectName(_fromUtf8("pushButton_02"))
        self.gridLayout_3.addWidget(self.pushButton_02, 2, 0, 1, 1)
        self.pushButton_05 = QtGui.QPushButton(self.tab_linux)
        self.pushButton_05.setObjectName(_fromUtf8("pushButton_05"))
        self.gridLayout_3.addWidget(self.pushButton_05, 5, 0, 1, 1)
        self.tabWidget_examples.addTab(self.tab_linux, _fromUtf8(""))
        self.tab_mac = QtGui.QWidget()
        self.tab_mac.setObjectName(_fromUtf8("tab_mac"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_mac)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_3 = QtGui.QLabel(self.tab_mac)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.tabWidget_examples.addTab(self.tab_mac, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget_examples, 4, 0, 1, 4)
        self.button_examples = QtGui.QPushButton(getPath)
        self.button_examples.setMinimumSize(QtCore.QSize(113, 0))
        self.button_examples.setStyleSheet(_fromUtf8("color: rgb(75, 75, 75);"))
        self.button_examples.setCheckable(True)
        self.button_examples.setObjectName(_fromUtf8("button_examples"))
        self.gridLayout.addWidget(self.button_examples, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)

        self.retranslateUi(getPath)
        self.tabWidget_examples.setCurrentIndex(0)
        QtCore.QObject.connect(self.button_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), getPath.close)
        QtCore.QMetaObject.connectSlotsByName(getPath)
        getPath.setTabOrder(self.edit_path, self.button_ok)
        getPath.setTabOrder(self.button_ok, self.button_locate)
        getPath.setTabOrder(self.button_locate, self.button_cancel)
        getPath.setTabOrder(self.button_cancel, self.button_examples)
        getPath.setTabOrder(self.button_examples, self.tabWidget_examples)
        getPath.setTabOrder(self.tabWidget_examples, self.pushButton_1)
        getPath.setTabOrder(self.pushButton_1, self.pushButton_2)
        getPath.setTabOrder(self.pushButton_2, self.pushButton_3)
        getPath.setTabOrder(self.pushButton_3, self.pushButton_4)
        getPath.setTabOrder(self.pushButton_4, self.pushButton_5)

    def retranslateUi(self, getPath):
        getPath.setWindowTitle(_translate("getPath", "Application Path", None))
        self.button_locate.setText(_translate("getPath", "Find it!", None))
        self.button_cancel.setText(_translate("getPath", "Cancel", None))
        self.label.setText(_translate("getPath", "<html><head/><body><p>Enter the execution path.</p><p>See the examples below for ideas.</p><p>If this is a filler and should not be executed, use only dashes (-) e.g. -----</p></body></html>", None))
        self.button_ok.setText(_translate("getPath", "Ok", None))
        self.pushButton_5.setText(_translate("getPath", "Mouse", None))
        self.pushButton_4.setText(_translate("getPath", "Java File", None))
        self.pushButton_1.setText(_translate("getPath", "Notepad (hosts file)", None))
        self.label_4.setText(_translate("getPath", "<html><head/><body><p><span style=\" color:#a6a6a6;\">Any existing Windows shortcut can be used including anything in the start menu.<br/>Right click on it and select Properties. Then copy the link here.</span></p><p><span style=\" color:#a6a6a6;\">A lot of files will launch by simply adding &quot;explorer.exe &quot; at the start.</span></p><p><span style=\" color:#a6a6a6;\">Useful tool for finding files: </span><a href=\"http://www.voidtools.com/download.php\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.voidtools.com/download.php</span></a><span style=\" color:#a6a6a6;\">.</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("getPath", "Network Connections", None))
        self.pushButton_3.setText(_translate("getPath", "Shutdown  (will do what it says!)", None))
        self.label_5.setText(_translate("getPath", "<html><head/><body><p><span style=\" color:#636363;\">Click any button below to reveal the path...<br/>Note: There are sample databases available for import in the main directory.</span></p></body></html>", None))
        self.tabWidget_examples.setTabText(self.tabWidget_examples.indexOf(self.tab_windows), _translate("getPath", "Windows", None))
        self.pushButton_06.setText(_translate("getPath", "Shutdown (will do what it says)", None))
        self.label_2.setText(_translate("getPath", "<html><head/><body><p><span style=\" color:#636363;\">Click any button below to reveal the path...<br/>Note: There are sample databases available for import in the main directory.</span></p></body></html>", None))
        self.pushButton_03.setText(_translate("getPath", "Gnome System Monitor", None))
        self.pushButton_01.setText(_translate("getPath", "LibreOffice Writer", None))
        self.pushButton_04.setText(_translate("getPath", "Google Chrome", None))
        self.pushButton_02.setText(_translate("getPath", "Gnome Terminal", None))
        self.pushButton_05.setText(_translate("getPath", "Disk Usage Analyser", None))
        self.tabWidget_examples.setTabText(self.tabWidget_examples.indexOf(self.tab_linux), _translate("getPath", "Linux", None))
        self.label_3.setText(_translate("getPath", "<html><head/><body><p><span style=\" font-size:16pt; color:#a6a6a6;\">Examples Coming Later</span></p></body></html>", None))
        self.tabWidget_examples.setTabText(self.tabWidget_examples.indexOf(self.tab_mac), _translate("getPath", "Mac", None))
        self.button_examples.setText(_translate("getPath", "Tips and Examples", None))


class getPath(QtGui.QWidget, Ui_getPath):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

