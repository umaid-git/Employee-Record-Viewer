from PyQt5 import QtWidgets
from addWindow import AddWindowUI
from editWindow import EditWindowUI
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QTableWidget, QMenuBar, QStatusBar, QLineEdit, QApplication, QGridLayout
from PyQt5 import uic
import sqlite3
import sys

class MainWindowUI(QMainWindow):
    def __init__(self):
        super(MainWindowUI,self).__init__()

        #load the ui file
        uic.loadUi("mainWindow.ui",self)

        #define our widgets
        self.displayQueryTable = self.findChild(QTableWidget, "displaySqlQueryTable")
        self.addButtonMainWindow = self.findChild(QPushButton, "addPushButton" )
        self.deleteButtonMainWindow = self.findChild(QPushButton, "deletePushButton" )
        self.editButtonMainWindow = self.findChild(QPushButton, "editPushButton" )
        self.queryButtonMainWindow = self.findChild(QPushButton, "queryPushButton" )
        self.refreshButtonMainWindow = self.findChild(QPushButton, "refreshPushButton" )

        #calls the function when the respective buttons are clicked
        self.addButtonMainWindow.clicked.connect(self.openAddWindow)
        self.editButtonMainWindow.clicked.connect(self.openEditWindow)
        self.refreshButtonMainWindow.clicked.connect(self.loadDataBase)
        # self.clearScreenbutton.clicked.connect(self.clearScreen)

        #show the app
        self.show()

    #open the AddWindow after clicking the Add button
    def openAddWindow(self):
        self.addWindow = QtWidgets.QMainWindow()
        self.addWindowUI = AddWindowUI()
        self.addWindowUI.getTreeWidgetFromMain = self.displayQueryTable
        # self.addWindow.show()

    #open the editWindow after clicking the edit button
    def openEditWindow(self):
        self.editWindow = QtWidgets.QMainWindow()
        self.editWindowUI = EditWindowUI()
        # self.editWindow.show()

    def loadDataBase(self):
        dataBaseConnection = sqlite3.connect('employee.db') #create or connect to already created database
        cursor = dataBaseConnection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Employee (
	                      first_name TEXT,
	                      last_name TEXT,
                          addrress TEXT,
	                      email TEXT,
                          phone_no  TEXT,
                          job_title  TEXT,
                          salary  TEXT
                        )""")

        sqlQuery = "SELECT * FROM Employee"
        tableRow = 0

        for record in cursor.execute(sqlQuery):
            self.displayQueryTable.setRowCount(tableRow+1)
            # print(record)
            for column in range (len(record)):
                self.displayQueryTable.setItem(tableRow, column+1, QtWidgets.QTableWidgetItem(record[column]))
            tableRow += 1
        
        # Commit our command
        dataBaseConnection.commit()
	    # close the database
        dataBaseConnection.close()


if __name__ == "__main__":
#initialize the APP
    app = QApplication(sys.argv)
    MainUIWindow = MainWindowUI()
    MainUIWindow.loadDataBase()
    app.exec_()
