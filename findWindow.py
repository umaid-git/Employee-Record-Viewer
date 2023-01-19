from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMenuBar, QStatusBar, QLineEdit, QApplication, QGridLayout
from PyQt5 import QtWidgets
from PyQt5 import uic
import sqlite3
import sys

class FindWindowUI(QMainWindow):
    def __init__(self):
        super(FindWindowUI,self).__init__()

        #load the ui file
        uic.loadUi("findWindow.ui",self)

        #define our widgets
        self.employee_ID_Line_Edit_findWindow  = self.findChild(QLineEdit, "employeeIDLineEdit")
        self.first_Name_Line_Edit_findWindow  = self.findChild(QLineEdit, "firstNameLineEdit")
        self.last_Name_Line_Edit_findWindow  = self.findChild(QLineEdit, "lastNameLineEdit")
        self.job_Title_Line_Edit_findWindow  = self.findChild(QLineEdit, "jobTitleLineEdit")
        self.salary_Less_Than_Line_Edit_findWindow  = self.findChild(QLineEdit, "salaryLessThanLineEdit")
        self.salary_Greater_Than_Line_Edit_findWindow  = self.findChild(QLineEdit, "salaryGreatorThanLineEdit")
        self.search_Button_findWindow = self.findChild(QPushButton, "searchPushButton" )

        self.search_Button_findWindow.clicked.connect(self.getDataFromDataField)

        #show the app
        self.show()

    def setTreeWidget(self, treeWidget):
        self.getTreeWidgetFromMain = treeWidget

    def closefindWindow(self):
        self.close()

    def getDataFromDataField(self):
        employee_ID = self.employee_ID_Line_Edit_findWindow.text()
        firstName = self.first_Name_Line_Edit_findWindow.text()
        lastName = self.last_Name_Line_Edit_findWindow.text()
        jobTitle = self.job_Title_Line_Edit_findWindow.text()
        salaryLessThan= self.salary_Less_Than_Line_Edit_findWindow.text()
        salaryGreatorThan= self.salary_Greater_Than_Line_Edit_findWindow.text()

        self.items = (firstName,lastName,employee_ID,jobTitle,salaryLessThan,salaryGreatorThan)  # store the data as a tuple
        #print(self.items)

        self.employee_ID_Line_Edit_findWindow.setText("")
        self.first_Name_Line_Edit_findWindow.setText("")
        self.last_Name_Line_Edit_findWindow.setText("")
        self.job_Title_Line_Edit_findWindow.setText("")
        self.salary_Less_Than_Line_Edit_findWindow.setText("")
        self.salary_Greater_Than_Line_Edit_findWindow.setText("")
        
        
        self.getSqlQuery()

        
        # return resultFromQuery

        # return items

    # generate the sql query for the field that is filled in the edit window
    # If the field is empty it means it doens't need to be updated. 
    def getSqlQuery(self):
        dataField = self.items
        dataBaseConnection = sqlite3.connect('employee.db') #create or connect to already created database
        cursor = dataBaseConnection.cursor()

        query = "SELECT rowid,* FROM Employee WHERE "

        if(dataField[0] != ''):
            query += f"first_name = '{dataField[0]}' AND "
        
        if(dataField[1] != ''):
            query += f"last_name = '{dataField[1]}' AND "

        if(dataField[2] != ''):
            query += f"rowid = '{dataField[2]}' AND "

        if(dataField[3] != ''):
            query += f"job_title = '{dataField[3]}' AND "
        

        
        query = query[0:-4]
        # print(query)

        cursor.execute(query)
        resultFromQuery = cursor.fetchall()
        # print(resultFromQuery)

        if(dataField[4] != '' and dataField[5] != ''):
            self.row = 0
            for records in resultFromQuery:
                if ((int (records[7])) <= (int (dataField[4])) and ((int (records[7])) >= (int (dataField[5]))) ) :
                    print(records)
                    self.displaySalaryResult(records)
            print("==================================================")


        elif(dataField[4] != ''):
            self.row = 0
            for records in resultFromQuery:
                if ((int (records[7])) <= (int (dataField[4]))) :
                    print(records)
                    self.displaySalaryResult(records)
            print("==================================================")

        
        elif(dataField[5] != ''):
            self.row = 0
            for records in resultFromQuery:
                if ((int (records[7])) >= (int (dataField[5]))) :
                    print(records)
                    self.displaySalaryResult(records)
            print("==================================================")

        self.displayFindResult(resultFromQuery)
        
        # self.row = 0
        # for records in resultFromQuery:
        #     if ((int (records[7])) >= (int (dataField[5]))) :
        #         print(records)
        #         self.displaySalaryResult(records)
        # print("==================================================")

        #self.displayFindResult(resultFromQuery)
 
        # print(resultFromQuery)
        

        
        # return resultFromQuery
        # print (query)
        # return query
    def displayFindResult(self, resultFromQuery):
        self.getTreeWidgetFromMain.setRowCount(len(resultFromQuery))

        for record in resultFromQuery:
            row = 0
            for column in range (len(resultFromQuery)):
                # print(column, record[column])
                #column zero have rowId which is unique and act as a primary key. rowID is int so need to cast it to str to display
                if(column == 0):
                    self.getTreeWidgetFromMain.setItem(row, column, QtWidgets.QTableWidgetItem(str(record[column])))
                    # print(f"{resultFromQuery[column]}", end="-")    
                else:
                    self.getTreeWidgetFromMain.setItem(row, column, QtWidgets.QTableWidgetItem(record[column]))
                    # print(f"{resultFromQuery[column]}", end="-")    
            row += 1

    def displaySalaryResult(self, resultFromQuery):
        # self.getTreeWidgetFromMain.setRowCount(self.row+1)

        # for record in resultFromQuery:
        #    row = 0
        for column in range (len(resultFromQuery)):
            self.getTreeWidgetFromMain.setRowCount(self.row+1)
            # print(column, record[column])
            #column zero have rowId which is unique and act as a primary key. rowID is int so need to cast it to str to display
            if(column == 0):
                self.getTreeWidgetFromMain.setItem(self.row, column, QtWidgets.QTableWidgetItem(str(resultFromQuery[column])))
                # print(f"{resultFromQuery[column]}", end="-")    
            else:
                self.getTreeWidgetFromMain.setItem(self.row, column, QtWidgets.QTableWidgetItem(resultFromQuery[column]))
                # print(f"{resultFromQuery[column]}", end="-")    
        self.row += 1
        

if __name__ == "__main__":
    #initialize the APP
    app = QApplication(sys.argv)
    editUIWindow = FindWindowUI()
    sys.exit(app.exec_())
