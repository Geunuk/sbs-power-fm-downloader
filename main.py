import sys

from selenium import webdriver
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import mainwindow

if __name__ == "__main__":
    driver = webdriver.Chrome()
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_ui = mainwindow.Ui_MainWindow()
    main_ui.setupUi(main_window)
    main_window.show()

    main_window.setEnabled(False)
    main_ui.initialize(driver)
    main_window.setEnabled(True)

    sys.exit(app.exec_())
