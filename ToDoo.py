# Coded af Frank Simens kontakt frank@simens.dk

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit



class Ui_MainWindow(object):

    def tilfoej(self):
        item = self.lineEdit.text()
        self.todolist.addItem(item)
        self.lineEdit.setText("")
    def slet(self):
        markeret = self.todolist.currentRow()
        self.todolist.takeItem(markeret)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 424)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 371, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.todolist = QtWidgets.QListWidget(self.verticalLayoutWidget, clicked=self.slet)
        self.todolist.setObjectName("todolist")
        self.verticalLayout.addWidget(self.todolist)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        #self.lineEdit.test = self.lineEdit()
        self.verticalLayout.addWidget(self.lineEdit)
        self.addtolist = QtWidgets.QPushButton(self.verticalLayoutWidget, clicked=self.tilfoej)
        self.addtolist.setObjectName("addtolist")
        #self.addtolist.clicked.connect(on_clicked)        
        self.verticalLayout.addWidget(self.addtolist)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowIcon(QtGui.QIcon('icons/todoo32.png'))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDooListe ---"))
        self.lineEdit.setText(_translate("MainWindow", "Indtast dit foretagen her..."))
        self.addtolist.setText(_translate("MainWindow", "Add to list"))

 
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
