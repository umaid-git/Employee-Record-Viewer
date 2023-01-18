from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMenuBar, QStatusBar, QLineEdit, QApplication, QGridLayout
from PyQt5 import QtWidgets
from PyQt5 import uic
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
        self.count = 1

    def addDataToDB(self):
        firstName = self.first_Name_Line_Edit_AddWindow.text()
        lastName = self.last_Name_Line_Edit_AddWindow.text()
        address = self.address_Line_Edit_AddWindow.text()
        email = self.email_Line_Edit_AddWindow.text()
        phoneNo = self.phone_No_Line_Edit_AddWindow.text()
        jobTitle = self.job_Title_Line_Edit_AddWindow.text()
        salary= self.salary_Line_Edit_AddWindow.text()

        #print(self.getTreeWidgetFromMain)

        items = (firstName,lastName,address,email,phoneNo,jobTitle,salary)
        self.getTreeWidgetFromMain.setRowCount(self.count)
        
        for i in range (len(items)):
            self.getTreeWidgetFromMain.setItem(self.count-1,i, QtWidgets.QTableWidgetItem(items[i]))
        
        self.count += 1
        # print(firstName)

    def closeAddWindow(self):
        self.close()


    # def clicker(self):
    #     self.label.setText(f"Hello There {self.textedit.toPlainText()}")
    #     self.textedit.setPlainText("")


if __name__ == "__main__":
    #initialize the APP
    app = QApplication(sys.argv)
    addUIWindow = AddWindowUI()
    sys.exit(app.exec_())
