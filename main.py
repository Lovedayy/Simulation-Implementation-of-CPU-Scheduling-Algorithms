import choose
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # 创建一个QApplication对象，用来管理应用程序的主要设置和资源
    app2 = QApplication(sys.argv)
    # 创建了一个QMainWindow对象，它是选择窗口的主窗口，并将其设置为UI类的实例
    MainWindow = QMainWindow()
    # 调用choose.py中的UI类来生成选择窗口的UI
    ui = choose.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()  # 显示选择窗口
    sys.exit(app2.exec_())
