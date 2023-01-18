from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMenuBar, QStatusBar, QLineEdit, QApplication, QGridLayout
from PyQt5 import QtWidgets
from PyQt5 import uic
import sqlite3
import sys

class AddWindowUI(QMainWindow):
    def __init__(self):
        super(AddWindowUI,self).__init__()

        #load the ui file
        uic.loadUi("addWindow.ui",self)

        #define our widgets
        self.first_Name_Line_Edit_AddWindow  = self.findChild(QLineEdit, "firstNameLineEdit")
        self.last_Name_Line_Edit_AddWindow  = self.findChild(QLineEdit, "lastNameLineEdit")
        self.address_Line_Edit_AddWindow  = self.findChild(QLineEdit, "addressLineEdit")
        self.email_Line_Edit_AddWindow  = self.findChild(QLineEdit, "emailLineEdit")
        self.phone_No_Line_Edit_AddWindow  = self.findChild(QLineEdit, "phoneNoLineEdit")
        self.job_Title_Line_Edit_AddWindow  = self.findChild(QLineEdit, "jobTitleLineEdit")
        self.salary_Line_Edit_AddWindow  = self.findChild(QLineEdit, "salaryLineEdit")
        self.done_Button_AddWindow = self.findChild(QPushButton, "donePushButton" )
        self.cancel_Button_AddWindow = self.findChild(QPushButton, "cancelPushButton" )

        self.getTreeWidgetFromMain = None

        #calls the function when the respective buttons are clicked
        self.done_Button_AddWindow.clicked.connect(self.addDataToDB)
        self.cancel_Button_AddWindow.clicked.connect(self.closeAddWindow)
        # self.clearScreenbutton.clicked.connect(self.clearScreen)

        #show the app
        self.show()
        self.sqlTableRow = 1

    #get the data from add window
    def getDataFromForm(self):
        # Stores the data from fields in add window
        firstName = self.first_Name_Line_Edit_AddWindow.text()
        lastName = self.last_Name_Line_Edit_AddWindow.text()
        address = self.address_Line_Edit_AddWindow.text()
        email = self.email_Line_Edit_AddWindow.text()
        phoneNo = self.phone_No_Line_Edit_AddWindow.text()
        jobTitle = self.job_Title_Line_Edit_AddWindow.text()
        salary= self.salary_Line_Edit_AddWindow.text()

        items = (firstName,lastName,address,email,phoneNo,jobTitle,salary)  # store the data as a tuple

        # print(firstName)

        return items


    # Add Data to the database
    def addDataToDB(self):
        #print(self.getTreeWidgetFromMain)
        dataBaseConnection = sqlite3.connect('employee.db') 
        cursor = dataBaseConnection.cursor()

        items = [self.getDataFromForm()]
        sqlQuery = "INSERT INTO Employee VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.executemany(sqlQuery, items)
        dataBaseConnection.commit()
        dataBaseConnection.close()

        # self.getTreeWidgetFromMain.setRowCount(self.sqlTableRow)    #every time data is added it sets the row in the table
        
        # for sqlTableColumn in range (len(items)):
        #     self.getTreeWidgetFromMain.setItem(self.sqlTableRow-1, sqlTableColumn+1, QtWidgets.QTableWidgetItem(items[sqlTableColumn]))   # display the data on the table
        
        # self.sqlTableRow += 1   # increments the row by 1 so the data can be displayed

    def closeAddWindow(self):
        self.close()


if __name__ == "__main__":
    #initialize the APP
    app = QApplication(sys.argv)
    addUIWindow = AddWindowUI()
    sys.exit(app.exec_())
