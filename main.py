import os
import sys
import platform

from selenium import webdriver
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import mainwindow

def main():
    if platform.system() == "Linux":
        driver_name = "chromedriver"
    elif platform.system() == "Windows":
        driver_name = "chromedriver.exe"
    else:
        print("Only works in Linux or Windows")
        return

    cur_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(cur_path, driver_name)
    
    driver = webdriver.Chrome(file_path)
    app = QtWidgets.QApplication(sys.argv)

    # Create main window
    main_window = QtWidgets.QMainWindow()
    main_ui = mainwindow.Ui_MainWindow()
    main_ui.setupUi(main_window)
    main_ui.initialize(driver)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
