from PyQt5 import QtWidgets
from addWindow import AddWindowUI
from editWindow import EditWindowUI
from findWindow import FindWindowUI
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
        self.findButtonMainWindow = self.findChild(QPushButton, "findPushButton" )
        self.refreshButtonMainWindow = self.findChild(QPushButton, "refreshPushButton" )

        #calls the function when the respective buttons are clicked
        self.addButtonMainWindow.clicked.connect(self.openAddWindow)
        self.deleteButtonMainWindow.clicked.connect(self.deleteRecordFromDB)
        self.editButtonMainWindow.clicked.connect(self.openEditWindow)
        self.findButtonMainWindow.clicked.connect(self.openFindWindow)
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
        self.editWindowUI.done_Button_editWindow.clicked.connect(self.editDatabase)
        # self.editWindow.show()

    # Open the find windowd after clicking the find button
    def openFindWindow(self):
        self.findWindow = QtWidgets.QMainWindow()
        self.findWindowUI = FindWindowUI()
        self.findWindowUI.setTreeWidget(self.displayQueryTable)    

    #edit the database based on the sql query received
    def editDatabase(self):
        query = self.editWindowUI.getSqlQuery() # get the sql query based on the data from edit window
        # print(record, " from main window")
        self.runSqlQueries(query)   # run the sql query

    #Loads the data when the main window starts or refresh button is clicked
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

        sqlQuery = "SELECT rowid,* FROM Employee"

        tableRow = 0

        for record in cursor.execute(sqlQuery):
            self.displayQueryTable.setRowCount(tableRow+1)
            # print(record)

            for column in range (len(record)):
                # print(column, record[column])

                #column zero have rowId which is unique and act as a primary key. rowID is int so need to cast it to str to display
                if(column == 0):
                    self.displayQueryTable.setItem(tableRow, column, QtWidgets.QTableWidgetItem(str(record[column])))    
                else:
                    self.displayQueryTable.setItem(tableRow, column, QtWidgets.QTableWidgetItem(record[column]))
            tableRow += 1
                
        # Commit any changes
        dataBaseConnection.commit()
	    # close the database
        dataBaseConnection.close()

    def runSqlQueries(self, sqlQuery):
        dataBaseConnection = sqlite3.connect('employee.db') #connect to already created database
        cursor = dataBaseConnection.cursor()
        cursor.execute(sqlQuery)
        print(sqlQuery)

        # Commit any changes
        dataBaseConnection.commit()
	    # close the database
        dataBaseConnection.close()


    #Deltes the record from the database
    def deleteRecordFromDB(self):
        #Grab the selected record or current row on the screen using mouse pointer
        selectedRow = self.displayQueryTable.currentRow()
        cell_val = self.displayQueryTable.item(selectedRow,0).text()

        # print(cell_val)

        #delete selected record from the screen
        for column in range (8):
            self.displayQueryTable.takeItem(selectedRow,column)

        #delete selected record from database have to press refresh afterwards
        query = f"DELETE FROM Employee WHERE rowid={cell_val}"
        self.runSqlQueries(query)


if __name__ == "__main__":
#initialize the APP
    app = QApplication(sys.argv)
    MainUIWindow = MainWindowUI()
    MainUIWindow.loadDataBase()
    app.exec_()
