import sys

from selenium import webdriver
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import mainwindow

if __name__ == "__main__":
    driver = webdriver.Chrome("chromedriver44.exe")
    app = QtWidgets.QApplication(sys.argv)

    # Create main window
    main_window = QtWidgets.QMainWindow()
    main_ui = mainwindow.Ui_MainWindow()
    main_ui.setupUi(main_window)
    main_ui.initialize(driver)
    main_window.show()
    sys.exit(app.exec_())

    # Create loading message
    from ui import loading
    loading_dialog = QtWidgets.QDialog()
    loading_ui = loading.Ui_Dialog()
    loading_ui.setupUi(loading_dialog)
    loading_ui.loading_label.setText("Loading program list. Please wait a second...")

    # Loading program list
    loading_dialog.show()

    main_ui.init_program_list(loading_dialog, main_window)

    # removed
    # self.program_list.itemDoubleClicked.connect(self.set_episode_list)
    # Finish to Load program list
    #loading_dialog.close()
    #main_window.show()
    #import time
    #time.sleep(5)

    print("go")
    main_window.setEnabled(False)
    main_window.setEnabled(True)
    print("end")

