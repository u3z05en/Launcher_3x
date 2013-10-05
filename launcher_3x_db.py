# -*- coding: utf-8 -*-

from sqlite3 import Cursor, connect
from re import split
from launcher_3x_resource import schema, get_tables

class DbCursor(Cursor):
    """Hold the database open for R/W"""
    def __init__(self, db_):
        self.db_gate = connect(db_)
        Cursor.__init__(self, self.db_gate)

    def build(self):
        cmds = split(r';', schema.decode('base64', 'strict').strip())
        for line in range(len(cmds) - 1):
            self.execute(cmds[line].strip())

    def getTable(self, table_name):
        cmd = 'SELECT * FROM "%s"' % table_name
        self.execute(cmd)
        return self.fetchall()

    def getApps(self, groupID):
        cmd = get_tables.decode('base64', 'strict') % groupID
        self.execute(cmd)
        return self.fetchall()

    def getAllApps(self):
        self.execute("SELECT * FROM item")
        return self.fetchall()

    def findApp(self, path):
        self.execute("SELECT iditem FROM item WHERE path == ?", [path])
        return self.fetchall()

    def add_group(self, index, name, seq, date):
        self.execute("INSERT INTO itemgroup VALUES (?,?,?,?)", (index, name, seq, date))

    def add_app(self, index, name, path, date):
        self.execute("INSERT INTO item VALUES (?,?,?,?)", (index, name, path, date))

    def add_app_link(self, appID, groupID, seqInGroup):
        self.execute("INSERT INTO itemgroup_has_item VALUES (?,?,?)", (appID, groupID, seqInGroup))

    def deleteAllRows(self, table_name):
        cmd = 'DELETE FROM %s' % table_name
        self.execute(cmd)

    def deleteGroup(self, groupID):
        self.execute("DELETE FROM itemgroup WHERE iditemgroup = ?", [groupID])

    def deleteGroupLink(self, groupID):
        self.execute("DELETE FROM itemgroup_has_item WHERE itemgroup_iditemgroup = ?", [groupID])

    def deleteSingleAppLink(self, groupID, itemID):
        self.execute("DELETE FROM itemgroup_has_item WHERE itemgroup_iditemgroup=? AND item_iditem = ?", (groupID, itemID))

    def deleteAllAppLinks(self, appID):
        self.execute("DELETE FROM itemgroup_has_item WHERE item_iditem = ?", [appID])

    def deleteApp(self, appID):
        self.execute("DELETE FROM item WHERE iditem = ?", [appID])

    def renameApp(self, app_name, appID):
        self.execute("UPDATE item SET name=? WHERE iditem = ?", (str(app_name), appID))

    def renameGroup(self, group_name, groupID):
        self.execute("UPDATE itemgroup SET name=? WHERE iditemgroup=?", (str(group_name), groupID))

    def changePath(self, path_name, appID):
        self.execute("UPDATE item SET path = ? WHERE iditem = ?", (str(path_name), appID))

    def fr_appname(self, find_text, replace_text):
        self.execute("UPDATE item SET name = REPLACE(name,?,?)", (str(find_text), str(replace_text)))

    def fr_apppath(self, find_text, replace_text):
        self.execute("UPDATE item SET path = REPLACE(path,?,?)", (str(find_text), str(replace_text)))

    def fr_groupname(self, find_text, replace_text):
        self.execute("UPDATE itemgroup SET name = REPLACE(name,?,?)", (str(find_text), str(replace_text)))

    def commit(self):
        self.db_gate.commit()

    def shutdown(self):
        self.db_gate.commit()
        self.close()
