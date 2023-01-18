from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMenuBar, QStatusBar, QLineEdit, QApplication, QGridLayout
from PyQt5 import uic
import sys

class EditWindowUI(QMainWindow):
    def __init__(self):
        super(EditWindowUI,self).__init__()

        #load the ui file
        uic.loadUi("editWindow.ui",self)

        #define our widgets
        # self.displaySqlQueryTable = self.findChild(QTableWidget, "displaySqlQueryTable")
        # self.addButtonMainWindow = self.findChild(QPushButton, "addPushButton" )
        # self.deleteButtonMainWindow = self.findChild(QPushButton, "deletePushButton" )
        # self.editButtonMainWindow = self.findChild(QPushButton, "editPushButton" )
        # self.queryButtonMainWindow = self.findChild(QPushButton, "queryPushButton" )

        #Do something
        # self.button.clicked.connect(self.clicker)
        # self.clearScreenbutton.clicked.connect(self.clearScreen)

        #show the app
        self.show()

    # def clearScreen(self):
    #     self.label.setText(f"Enter your name below! ")
    #     self.textedit.setPlainText("")

    # def clicker(self):
    #     self.label.setText(f"Hello There {self.textedit.toPlainText()}")
    #     self.textedit.setPlainText("")


if __name__ == "__main__":
    #initialize the APP
    app = QApplication(sys.argv)
    editUIWindow = EditWindowUI()
    sys.exit(app.exec_())
