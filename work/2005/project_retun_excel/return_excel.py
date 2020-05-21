# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retun_v1.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import return_fans, return_staff
import six
import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 335)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 70, 161, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 211, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.file_path_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.file_path_browser.setGeometry(QtCore.QRect(90, 20, 451, 21))
        self.file_path_browser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_path_browser.setObjectName("file_path_browser")
        self.choose_file = QtWidgets.QPushButton(self.centralwidget)
        self.choose_file.setGeometry(QtCore.QRect(550, 20, 75, 23))
        self.choose_file.setObjectName("choose_file")
        self.choose_file.clicked.connect(self.select_file_path)  # 选择路径按钮
        self.check_fans = QtWidgets.QCheckBox(self.centralwidget)
        self.check_fans.setGeometry(QtCore.QRect(230, 70, 71, 21))
        self.check_fans.setText("")
        self.check_fans.setObjectName("check_fans")
        self.check_sale = QtWidgets.QCheckBox(self.centralwidget)
        self.check_sale.setGeometry(QtCore.QRect(230, 100, 71, 21))
        self.check_sale.setText("")
        self.check_sale.setObjectName("check_sale")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(10, 140, 81, 31))
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.start)  # 开始按钮
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 140, 501, 131))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自动生成表格"))
        self.label.setText(_translate("MainWindow", "生成未报名粉丝表格"))
        self.label_2.setText(_translate("MainWindow", "生成未领取海报营销员表格"))
        self.label_3.setText(_translate("MainWindow", "文件路径"))
        self.choose_file.setText(_translate("MainWindow", "选择路径"))
        self.start_button.setText(_translate("MainWindow", "开始处理"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">使用说明（必读）</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. 将需要用到的原始数据全都放到同一个文件夹下</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   <span style=\" font-weight:600;\">必须把员工列表.csv放到文件夹下</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   只可放置溯源海报的【统计明细】表格</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. 点击右上方【选择路径】按钮，选择到放置数据的文件夹</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. 勾选需要生成的表格</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. 点击【开始处理】</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5. 生成的表格会放到原文件夹内命名为今日日期的文件夹中</p></body></html>"))


    def select_file_path(self):
        self.dir_choose = QFileDialog.getExistingDirectory(None, "选取文件夹", self.cwd,)  # 起始路径
        self.file_path_browser.append(self.dir_choose)
        self.dir_choose = self.dir_choose + '\\'
        return


    def get_new_file(self,lis):
        l = []
        for name in lis:
            index = name.split('-')[1]
            l.append(index)
        max_index = max(l)
        for name in lis:
            if max_index in name:
                return name


    def get_file_name(self):
        sale_file = []
        member_file = []
        for root, dirs, files in os.walk(self.dir_choose):
            for file in files:
                if '营销员' in file:
                    sale_file.append(file)
                if '会员' in file:
                    member_file.append(file)
        if len(sale_file) == 1:
            self.s = sale_file[0]
        elif len(sale_file) > 1:
            self.s = self.get_new_file(sale_file)
        if len(member_file) ==1 :
            self.m = member_file[0]
        elif len(member_file) > 1:
            self.m = self.get_new_file(member_file)
        return self.s, self.m


    def start(self):
        try:
            self.get_file_name()
        except Exception as e:
            self.textBrowser.append(str(e))

        self.textBrowser.clear()
        if self.check_sale.checkState() !=QtCore.Qt.Checked and self.check_fans.checkState() != QtCore.Qt.Checked:
            self.textBrowser.append('？？？')
        else:
            self.textBrowser.append('开始处理...')
        if self.check_fans.checkState() == QtCore.Qt.Checked:
            self.textBrowser.append('--' * 20)
            self.textBrowser.append('开始处理未报名粉丝表格')
            try:
                return_fans.domain(self.dir_choose, self.s, self.m)
                self.textBrowser.append('--'*20)
                self.textBrowser.append('未报名粉丝表格处理完成')
            except Exception as e:
                self.textBrowser.append('生成未报名粉丝表格出错')
                self.textBrowser.append(str(e))
        if self.check_sale.checkState() == QtCore.Qt.Checked:
            self.textBrowser.append('--' * 20)
            self.textBrowser.append('开始处理未领取海报营销员表格')
            try:
                return_staff.domain(self.dir_choose, self.s)
                self.textBrowser.append('--' * 20)
                self.textBrowser.append('未领取海报营销员表格处理完成')
            except Exception as e:
                self.textBrowser.append('生成未领取海报营销员表格出错')
                self.textBrowser.append(str(e))
        return



app = QApplication(sys.argv)

MainWindow = QMainWindow()

ui = Ui_MainWindow()

ui.setupUi(MainWindow)

MainWindow.show()

sys.exit(app.exec_())
