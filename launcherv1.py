#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, platform, subprocess, logging, sqlite3, ctypes
from re import split, sub, findall
from PyQt4 import QtCore, QtGui
from launcher_ui import Ui_window_main

class MainW(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent, (QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowMaximizeButtonHint))
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('WindowsVista'))
        QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())
        self.ui = Ui_window_main()
        self.ui.setupUi(self)
        #PREPARATIONS
        self.setWindowTitle('Launcher')
        self.setWindowIcon(QtGui.QIcon('rsc/app.ico'))
        self.ui.menu_exit.setIcon(QtGui.QIcon('rsc/exit.ico'))
        self.ui.menu_addGroup.setIcon(QtGui.QIcon('rsc/addgroup.ico'))
        self.ui.menu_deleteGroup.setIcon(QtGui.QIcon('rsc/deletegroup.ico'))
        self.ui.menu_changeOrder.setIcon(QtGui.QIcon('rsc/editgroup.ico'))
        self.ui.menu_aboutqt.setIcon(QtGui.QIcon('rsc/qt.png'))
        self.font = QtGui.QFont()
        self.trayInit()
        #DB CONNECT/CREATE
        self.start()
        #LOAD TABLES AND THEN ITEMS
        self.loadTables()
        self.saveDB()
        #SLOTS
        QtCore.QObject.connect(self.ui.menu_aboutqt, QtCore.SIGNAL("triggered()"), QtGui.qApp.aboutQt)
        QtCore.QObject.connect(self.trayIcon, QtCore.SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), self.trayControl)
        QtCore.QObject.connect(self.ui.menu_exit, QtCore.SIGNAL("triggered()"), self.windowLeave)
        QtCore.QObject.connect(self.ui.widget_applist, QtCore.SIGNAL("itemPressed(QTreeWidgetItem*,int)"), self.itemClicked)
        QtCore.QObject.connect(self.ui.button_selectall, QtCore.SIGNAL("clicked()"), self.selectAll)
        QtCore.QObject.connect(self.ui.button_selectnone, QtCore.SIGNAL("released()"), self.selectNone)
        QtCore.QObject.connect(self.ui.button_invert, QtCore.SIGNAL("clicked()"), self.selectInvert)
        QtCore.QObject.connect(self.ui.button_editorder, QtCore.SIGNAL("clicked()"), self.editOrder)
        QtCore.QObject.connect(self.ui.button_launch, QtCore.SIGNAL("clicked()"), self.launchItem)
        QtCore.QObject.connect(self.ui.button_additem, QtCore.SIGNAL("clicked()"), self.addItem)
        QtCore.QObject.connect(self.ui.button_deleteitem, QtCore.SIGNAL("clicked()"), self.deleteItem)
        QtCore.QObject.connect(self.ui.button_savedb, QtCore.SIGNAL("clicked()"), self.saveDB)
        QtCore.QObject.connect(self.ui.button_revert, QtCore.SIGNAL("clicked()"), self.revertItems)
        QtCore.QObject.connect(self.ui.combobox_groups, QtCore.SIGNAL("activated(int)"), self.switchTable)
        QtCore.QObject.connect(self.ui.menu_addGroup, QtCore.SIGNAL("triggered()"), self.addTable)
        QtCore.QObject.connect(self.ui.menu_deleteGroup, QtCore.SIGNAL("triggered()"), self.deleteTable)

    #DATABASE CONTROL
    def start(self):
        if not os.path.isfile(DB_FILE):
            self.app_db = DbCursor(DB_FILE)
            table, qok = QtGui.QInputDialog.getText(self, 'Group Name', 'Enter Initial Application Group: ')
            self.table = str(table)
            if qok:
                self.app_db.initialise('Tables')
                self.app_db.initialise(self.table)
                self.app_db.write_row('Tables', self.table, '', '')
                self.app_db.commit()
                log_this('New table created: "' + self.table + '"', 'info')
            else:
                self.app_db.shutdown()
                del self.app_db
                os.remove(DB_FILE)
                leave_now(1)
        else:
            self.app_db = DbCursor(DB_FILE)

    def saveDB(self):
        self.app_db.drop_table(self.table)
        self.app_db.initialise(self.table)
        for item in self.item_list.keys():
            self.app_db.write_row(self.table, self.item_list[item][0], self.item_list[item][1], self.item_list[item][2])
        self.app_db.commit()
        self.dbState('saved')
        self.loadTables()

    #TABLE CONTROL
    def loadTables(self):
        self.table_list = {}
        self.ui.combobox_groups.clear()
        tablelist = self.app_db.fetch_all('Tables')
        for index in range(len(tablelist)):
            table = str(tablelist[index][0])
            self.ui.combobox_groups.addItem(table)
            self.table_list[index] = table
        try:
            self.table
        except:
            self.table = self.table_list[0]
        for index in self.table_list.keys():
            if self.table == self.table_list[index]:
                self.ui.combobox_groups.setCurrentIndex(index)
        self.loadItems()

    def addTable(self):
        proceed = True
        if not self.ui.button_savedb.isEnabled():
            table, qok = QtGui.QInputDialog.getText(self, 'Group Name', 'Enter New Group Name: ')
            table = str(table)
            if qok:
                for index in self.table_list:
                    if self.table_list[index] == table:
                        proceed = False
                if proceed:
                    self.ui.combobox_groups.addItem(table)
                    self.app_db.write_row('Tables', table, '', '')
                    self.app_db.initialise(table)
                    self.app_db.commit()
                    self.table = table
                    self.ui.combobox_groups.setCurrentIndex(self.ui.combobox_groups.count() - 1)
                    self.loadTables()
        else:
            reply = QtGui.QMessageBox.information(self, 'Message', 'Current Group "' + self.table + '" is not saved, proceed?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.dbState('saved')
                self.addTable()

    def switchTable(self):
        if not self.ui.button_savedb.isEnabled():
            for index in range(len(self.table_list)):
                if self.ui.combobox_groups.currentText() == self.table_list[index]:
                    self.table = self.table_list[index]
                    break
            self.loadTables()
        else:
            reply = QtGui.QMessageBox.information(self, 'Message', 'Current Group "' + self.table + '" is not saved, proceed?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.dbState('saved')
                self.switchTable()
            else:
                for index in self.table_list.keys():
                    if self.table == self.table_list[index]:
                        self.ui.combobox_groups.setCurrentIndex(index)
                        break

    def deleteTable(self):
        reply = QtGui.QMessageBox.critical(self, 'Message', 'Are you sure you want to remove the whole group\n\n  ' + self.table, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.app_db.delete_row('Tables', self.table)
            self.app_db.drop_table(self.table)
            self.app_db.commit()
            del self.table_list[self.ui.combobox_groups.currentIndex()]
            del self.table
            if len(self.table_list) == 0:
                self.app_db.shutdown()
                del self.app_db
                os.remove(DB_FILE)
                self.start()
                self.loadTables()
            else:
                self.loadTables()

    #ITEM CONTROL
    def loadItems(self):
        self.item_list = {}
        self.ui.widget_applist.clear()
        applist = self.app_db.fetch_all(self.table)
        for line in range(len(applist)):
            self.insertItem(applist[line][0], applist[line][1], applist[line][2])
        self.ui.widget_applist.sortByColumn(1)
        self.dbState('saved')
        self.selectAll()

    def insertItem(self, app, order, path):
        path = sub(r'[ ]{2,}', ' ', path).strip()
        item = QtGui.QTreeWidgetItem(self.ui.widget_applist)
        self.item_list[item] = [app, order, path]
        self.font.setPointSize(12)
        item.setFont(0, self.font)
        self.font.setPointSize(10)
        item.setFont(1, self.font); item.setFont(2, self.font)
        item.setText(0, app)
        item.setText(1, order)
        item.setText(2, path)
        item.setCheckState(0, QtCore.Qt.Unchecked)
        item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.ui.widget_applist.resizeColumnToContents(0)
        self.ui.widget_applist.resizeColumnToContents(1)

    def itemClicked(self):
        if self.ui.widget_applist.currentItem().checkState(0) == 0:
            self.ui.widget_applist.currentItem().setCheckState(0, QtCore.Qt.Checked)
        else:
            self.ui.widget_applist.currentItem().setCheckState(0, QtCore.Qt.Unchecked)

    def revertItems(self):
        reply = QtGui.QMessageBox.warning(self, 'Message', 'You will loose changes, proceed?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.loadTables()

    #BUTTON CONTROL
    def selectAll(self):
        for key in self.item_list.keys():
            key.setCheckState(0, QtCore.Qt.Checked)

    def selectNone(self):
        for key in self.item_list.keys():
            key.setCheckState(0, QtCore.Qt.Unchecked)

    def selectInvert(self):
        for item in self.item_list.keys():
            if item.checkState(0) == 2:
                item.setCheckState(0, QtCore.Qt.Unchecked)
            else:
                item.setCheckState(0, QtCore.Qt.Checked)

    def editOrder(self):
        for item in self.item_list.keys():
            if item.checkState(0) == 2:
                order, orderok = QtGui.QInputDialog.getText(self, 'Order', 'Item Order for "' + self.item_list[item][0] + '": ')
                if orderok:
                    item.setText(1, order)
                    self.item_list[item][1] = str(order)
                    if not self.ui.button_savedb.isEnabled():
                        self.dbState('changed')

    def launchItem(self):
        for item in self.item_list.keys():
            if item.checkState(0) == 2:
                cmd = split(r' ', self.item_list[item][2])
                subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, stdin = subprocess.PIPE)

    def addItem(self):
        app, appok = QtGui.QInputDialog.getText(self, 'Application', 'Application Name: ')
        order, orderok = QtGui.QInputDialog.getText(self, 'Order', 'Item Order (xxx): ')
        path, pathok = QtGui.QInputDialog.getText(self, 'Path', 'Application Path: ')
        if appok and pathok and orderok:
            log_this('Item Created: ' + app + ' - ' + order + ' - ' + path, 'crit')
            self.insertItem(str(app), str(order), str(path))
        self.dbState('changed')

    def deleteItem(self):
        for item in self.item_list.keys():
            if item.checkState(0) == 2:
                reply = QtGui.QMessageBox.critical(self, 'Message', "Are you sure you want to delete\n\n   " + self.item_list[item][0], QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    item.setHidden(True)
                    del self.item_list[item]
                    if not self.ui.button_savedb.isEnabled():
                        self.dbState('changed')

    def dbState(self, state):
        if state == 'saved': #Grey out buttons
            self.ui.button_savedb.setEnabled(False); self.ui.button_savedb.setStyleSheet('color: rgb(122, 122, 122);')
            self.ui.button_revert.setEnabled(False); self.ui.button_revert.setStyleSheet('color: rgb(122, 122, 122);')
        else:
            self.ui.button_savedb.setEnabled(True); self.ui.button_savedb.setStyleSheet('color: rgb(0, 170, 0);')
            self.ui.button_revert.setEnabled(True); self.ui.button_revert.setStyleSheet('color: rgb(0, 170, 0);')

    #SYSTEM CONTROL
    def trayInit(self):
        self.trayIcon = QtGui.QSystemTrayIcon()
        self.trayIcon.setIcon(QtGui.QIcon('rsc/app.ico'))
        self.trayMenu = QtGui.QMenu()
        self.trayMenu.addAction("Exit", self.windowLeave)
        self.trayIcon.setContextMenu(self.trayMenu)
        if self.trayIcon.isSystemTrayAvailable():
            self.trayIcon.show()

    def trayControl(self, event):
        if event == 3: #RIGHT, DOUBLE, LEFT, MIDDLE
            if self.isHidden() or self.isMinimized():
                self.showNormal()
                self.show()
            else:
                self.hide()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def windowLeave(self):
        if self.ui.button_savedb.isEnabled():
            reply = QtGui.QMessageBox.warning(self, 'Message', "Are you sure?\nData has changed.", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.No:
                pass
            else:
                self.app_db.shutdown()
                leave_now(0)
        else:
            self.app_db.shutdown()
            leave_now(0)

class DbCursor(sqlite3.Cursor):
    """Hold the database open for R/W"""
    def __init__(self, db_):
        self.db_gate = sqlite3.connect(db_)
        sqlite3.Cursor.__init__(self, self.db_gate)

    def initialise(self, table_name):
        if table_name == 'Tables':
            cmd = '''create table ''' + table_name + ''' ('GroupName')'''
        else:
            cmd = '''create table ''' + table_name + ''' ('Application','Order','Path')'''
        self.execute(cmd)

    def fetch_all(self, table_name):
        cmd = '''select * from ''' + table_name
        self.execute(cmd)
        return self.fetchall()

    def delete_row(self, table_name, col_1):
        if table_name == 'Tables':
            cmd = '''delete from ''' + table_name + ''' where GroupName="''' + col_1 + '''"'''
        else:
            cmd = '''delete from ''' + table_name + ''' where Application="''' + col_1 + '''"'''
        self.execute(cmd)

    def write_row(self, table_name, col_1, col_2, col_3):
        if table_name == 'Tables':
            cmd = '''insert into ''' + table_name + ''' values ("''' + col_1 + '''")'''
        else:
            cmd = '''insert into ''' + table_name + ''' values ("''' + col_1 + '''","''' + col_2 + '''","''' + col_3 + '''")'''
        self.execute(cmd)

    def drop_table(self, table_name):
        cmd = '''drop table ''' + table_name
        self.execute(cmd)

    def commit(self):
        self.db_gate.commit()

    def shutdown(self):
        self.db_gate.commit()
        self.close()

def startup():
    """Statup Checks"""
    msg = BASE_NAME + ' Initiated';log_this(msg.center(45, '-'), 'info')
    #PID PROCESSING
    if os.path.isfile(PID_FILE) == True:
        old_instance = open(PID_FILE).readlines()[0].strip()
        os.remove(PID_FILE)
        if int(old_instance) != PID_NUM:
            try:
                os.kill(int(old_instance), 9)
                log_this('Old PID file found and killed. Old PID: ' + old_instance + ' Cur PID: ' + str(PID_NUM), 'warn')
            except:
                log_this('Old PID file found, process was not running. Old PID: ' + old_instance + ' Cur PID: ' + str(PID_NUM), 'warn')
        else:
            log_this('PID file contains current PID, something is very wrong!', 'crit')
            leave_now(1)
    pid_gate = open(PID_FILE, 'wb')
    pid_gate.write(str(PID_NUM))
    pid_gate.close()

def log_this(log_string, severity):
    """Log a string. Sevs: debug, info, warn, crit"""
    logging.info(log_string)
    print log_string

def leave_now(exit_code):
    """Exit procedures"""
    os.remove(PID_FILE)
    msg = BASE_NAME + ' Exited (' + str(exit_code) + ')';log_this(msg.center(45, '-'), 'info')
    sys.exit(exit_code)

if __name__ == '__main__':
    #GLOBALS
    PLATFORM = str(findall(r'^.*?\-.{1}', platform.platform())[0])
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    BASE_NAME = split(r'\..*$', os.path.basename(os.path.realpath(__file__)))[0]
    PID_NUM = os.getpid()
    PID_FILE = os.path.join(BASE_DIR, BASE_NAME + '.pid')
    LOG_FILE = os.path.join(BASE_DIR, BASE_NAME + '.log')
    DB_FILE = os.path.join(BASE_DIR, BASE_NAME + '.sqlite')
    logging.basicConfig(filename = LOG_FILE, format = '%(asctime)s,%(name)s,%(levelname)s,%(message)s', datefmt = '%d/%m/%Y,%H:%M:%S', level = logging.DEBUG)
    #START CHECKS
    startup()
    #START GUI
    if PLATFORM == 'Windows-7':
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('u3z05en.launcher')
    Application = QtGui.QApplication(sys.argv)
    launch_GUI = MainW()
    launch_GUI.show()
    sys.exit(Application.exec_())
