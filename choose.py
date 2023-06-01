from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import FileOperation
import window
import ProcessList
import Manage

class Ui_MainWindow(object):
    # UI设置
    # 标签(QLabel)、下拉框(QComboBox)、按钮(QPushButton)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 245)
        QApplication.setStyle("Fusion")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(206, 30, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(206, 110, 121, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # retranslateUi函数用于设置各个组件的属性和文本内容，
        # 并将点击按钮后触发的函数与按钮的点击事件(clicked)绑定。
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "选择页面"))
        self.label.setText(_translate("MainWindow", "请选择测试文件"))
        self.label_2.setText(_translate("MainWindow", "请选择调度算法"))
        self.comboBox.setItemText(0, _translate("MainWindow", "input1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "input2"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "进程调度：时间片轮转法"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "进程调度：多级反馈队列法"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "作业调度：先来先服务"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "作业调度：短作业优先"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "作业调度：最高响应比"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton.clicked.connect(lambda: self.button(MainWindow))  # 点击确定按钮触发button函数

    # button函数是在点击按钮后触发的函数，根据用户选择的文件和调度算法，
    # 设置相关的参数，然后创建一个名为m的主窗口(QMainWindow)并显示。
    def button(self, MainWindow):
        file = self.comboBox.currentText()  # 选择调度算法
        idea = self.comboBox_2.currentText()  # 选择测试文件
        if file == "input1":
            FileOperation.file_num = 1
        elif file == "input2":
            FileOperation.file_num = 2

        if idea == "进程调度：时间片轮转法":
            ProcessList.idea = 1
        elif idea == "进程调度：多级反馈队列法":
            ProcessList.idea = 2
        elif idea == "作业调度：先来先服务":
            ProcessList.idea = 3
        elif idea == "作业调度：短作业优先":
            ProcessList.idea = 4
        elif idea == "作业调度：最高响应比":
            ProcessList.idea = 5

        Manage.t.before_prepare()
        self.m = QMainWindow()
        ui = window.ui
        ui.setupUi(self.m)
        self.m.show()  # 显示主窗口
        MainWindow.close()
        window.ui.printf("进程/作业调度事件:")
