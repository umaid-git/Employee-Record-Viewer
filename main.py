from PyQt5 import QtWidgets
from addWindow import AddWindowUI
from editWindow import EditWindowUI
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QTableWidget, QMenuBar, QStatusBar, QLineEdit, QApplication, QGridLayout
from PyQt5 import uic
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

        #calls the function when the respective buttons are clicked
        self.addButtonMainWindow.clicked.connect(self.openAddWindow)
        self.editButtonMainWindow.clicked.connect(self.openEditWindow)
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


if __name__ == "__main__":
#initialize the APP
    app = QApplication(sys.argv)
    MainUIWindow = MainWindowUI()
    app.exec_()
