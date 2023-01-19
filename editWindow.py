from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMenuBar, QStatusBar, QLineEdit, QApplication, QGridLayout
from PyQt5 import uic
import sqlite3
import sys

class EditWindowUI(QMainWindow):
    def __init__(self):
        super(EditWindowUI,self).__init__()

        #load the ui file
        uic.loadUi("editWindow.ui",self)

        #define our widgets
        self.employee_ID_Line_Edit_editWindow  = self.findChild(QLineEdit, "employeeIDLineEdit")
        self.first_Name_Line_Edit_editWindow  = self.findChild(QLineEdit, "firstNameLineEdit")
        self.last_Name_Line_Edit_editWindow  = self.findChild(QLineEdit, "lastNameLineEdit")
        self.address_Line_Edit_editWindow  = self.findChild(QLineEdit, "addressLineEdit")
        self.email_Line_Edit_editWindow  = self.findChild(QLineEdit, "emailLineEdit")
        self.phone_No_Line_Edit_editWindow  = self.findChild(QLineEdit, "phoneNoLineEdit")
        self.job_Title_Line_Edit_editWindow  = self.findChild(QLineEdit, "jobTitleLineEdit")
        self.salary_Line_Edit_editWindow  = self.findChild(QLineEdit, "salaryLineEdit")
        self.done_Button_editWindow = self.findChild(QPushButton, "donePushButton" )
        self.cancel_Button_editWindow = self.findChild(QPushButton, "cancelPushButton" )

        self.cancel_Button_editWindow.clicked.connect(self.closeEditWindow)
        self.done_Button_editWindow.clicked.connect(self.getDataFromDataField)

        #show the app
        self.show()

    def closeEditWindow(self):
        self.close()

    def getDataFromDataField(self):
        employee_ID = self.employee_ID_Line_Edit_editWindow.text()
        firstName = self.first_Name_Line_Edit_editWindow.text()
        lastName = self.last_Name_Line_Edit_editWindow.text()
        address = self.address_Line_Edit_editWindow.text()
        email = self.email_Line_Edit_editWindow.text()
        phoneNo = self.phone_No_Line_Edit_editWindow.text()
        jobTitle = self.job_Title_Line_Edit_editWindow.text()
        salary= self.salary_Line_Edit_editWindow.text()

        self.items = (employee_ID,firstName,lastName,address,email,phoneNo,jobTitle,salary)  # store the data as a tuple
        # print(items)

        self.employee_ID_Line_Edit_editWindow.setText("")
        self.first_Name_Line_Edit_editWindow.setText("")
        self.last_Name_Line_Edit_editWindow.setText("")
        self.address_Line_Edit_editWindow.setText("")
        self.email_Line_Edit_editWindow.setText("")
        self.phone_No_Line_Edit_editWindow.setText("")
        self.job_Title_Line_Edit_editWindow.setText("")
        self.salary_Line_Edit_editWindow.setText("")

        # return items

    # generate the sql query for the field that is filled in the edit window
    # If the field is empty it means it doens't need to be updated. 
    def getSqlQuery(self):
        dataBaseConnection = sqlite3.connect('employee.db') #create or connect to already created database
        cursor = dataBaseConnection.cursor()

        cursor.execute("PRAGMA table_info(Employee)")
        attributeNameTuple = cursor.fetchall()

        query = "UPDATE Employee SET "

        for column in range (len(attributeNameTuple)):
            # print(attributeNameTuple[attributeName][1], "from edit window")

            #column+1 because the first tuple contains employee Id
            if self.items[column+1] != "":
                query += f"{attributeNameTuple[column][1]} = '{self.items[column+1]}' , "

        query = query[:-2] + f"WHERE rowid = {self.items[0]}"   #adds employeeID to the query string
        # print (query)
        return query



if __name__ == "__main__":
    #initialize the APP
    app = QApplication(sys.argv)
    editUIWindow = EditWindowUI()
    sys.exit(app.exec_())
