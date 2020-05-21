import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import time, datetime

TIME = time.strftime('%Y-%m-%d', time.localtime(time.time()))

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(852, 590)
        self.today = '今天日期为：'+ TIME+ '  星期'+ str(datetime.datetime.now().isoweekday())
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 190, 701, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.path = QtWidgets.QTextEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(110, 140, 611, 31))
        self.path.setObjectName("path")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 150, 71, 16))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.sale_file = QtWidgets.QTextEdit(self.centralwidget)
        self.sale_file.setGeometry(QtCore.QRect(110, 90, 301, 31))
        self.sale_file.setObjectName("sale_flie")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 71, 16))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 350, 54, 12))
        self.label_3.setObjectName("label_3")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(740, 140, 75, 31))
        self.run.setObjectName("run")
        self.run.clicked.connect(self.start)
        self.member_file = QtWidgets.QTextEdit(self.centralwidget)
        self.member_file.setGeometry(QtCore.QRect(510, 90, 301, 31))
        self.member_file.setObjectName("member_file")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 100, 71, 16))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "文件夹路径："))
        self.label_2.setText(_translate("mainWindow", "营销员会议："))
        self.label_3.setText(_translate("mainWindow", "Logging："))
        self.run.setText(_translate("mainWindow", "开始处理"))
        self.label_4.setText(_translate("mainWindow", "会员会议："))


    def start(self):

        self.textBrowser.append(self.today)
        # path = self.path.text()
        # sale_file = self.sale_file.text()
        # member_file = self.member_file.text()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    MainWindow = QMainWindow()

    ui = Ui_mainWindow()

    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
