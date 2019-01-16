# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import loading
import scraper

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.program_list = QtWidgets.QListWidget(self.centralwidget)
        self.program_list.setObjectName("program_list")
        self.gridLayout.addWidget(self.program_list, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(100)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.start_label = QtWidgets.QLabel(self.centralwidget)
        self.start_label.setAlignment(QtCore.Qt.AlignCenter)
        self.start_label.setObjectName("start_label")
        self.horizontalLayout_3.addWidget(self.start_label)
        self.start_date = QtWidgets.QDateEdit(self.centralwidget)
        self.start_date.setObjectName("start_date")
        self.horizontalLayout_3.addWidget(self.start_date)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.end_label = QtWidgets.QLabel(self.centralwidget)
        self.end_label.setAlignment(QtCore.Qt.AlignCenter)
        self.end_label.setObjectName("end_label")
        self.horizontalLayout_2.addWidget(self.end_label)
        self.end_date = QtWidgets.QDateEdit(self.centralwidget)
        self.end_date.setObjectName("end_date")
        self.horizontalLayout_2.addWidget(self.end_date)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mon_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.mon_check_box.setChecked(True)
        self.mon_check_box.setObjectName("mon_check_box")
        self.horizontalLayout.addWidget(self.mon_check_box)
        self.tue_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.tue_check_box.setChecked(True)
        self.tue_check_box.setObjectName("tue_check_box")
        self.horizontalLayout.addWidget(self.tue_check_box)
        self.wed_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.wed_check_box.setChecked(True)
        self.wed_check_box.setObjectName("wed_check_box")
        self.horizontalLayout.addWidget(self.wed_check_box)
        self.thu_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.thu_check_box.setChecked(True)
        self.thu_check_box.setObjectName("thu_check_box")
        self.horizontalLayout.addWidget(self.thu_check_box)
        self.fri_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.fri_check_box.setChecked(True)
        self.fri_check_box.setTristate(False)
        self.fri_check_box.setObjectName("fri_check_box")
        self.horizontalLayout.addWidget(self.fri_check_box)
        self.sat_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.sat_check_box.setChecked(True)
        self.sat_check_box.setObjectName("sat_check_box")
        self.horizontalLayout.addWidget(self.sat_check_box)
        self.sun_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.sun_check_box.setChecked(True)
        self.sun_check_box.setObjectName("sun_check_box")
        self.horizontalLayout.addWidget(self.sun_check_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.query_line = QtWidgets.QLineEdit(self.centralwidget)
        self.query_line.setObjectName("query_line")
        self.horizontalLayout_6.addWidget(self.query_line)
        self.query_btn = QtWidgets.QPushButton(self.centralwidget)
        self.query_btn.setObjectName("query_btn")
        self.horizontalLayout_6.addWidget(self.query_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.episode_list = QtWidgets.QListWidget(self.centralwidget)
        self.episode_list.setObjectName("episode_list")
        self.verticalLayout_2.addWidget(self.episode_list)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.center_line = QtWidgets.QFrame(self.centralwidget)
        self.center_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.center_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.center_line.setObjectName("center_line")
        self.gridLayout.addWidget(self.center_line, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SBS Power FM Downloader"))
        self.start_label.setText(_translate("MainWindow", "시작일"))
        self.end_label.setText(_translate("MainWindow", "종료일"))
        self.mon_check_box.setText(_translate("MainWindow", "월요일"))
        self.tue_check_box.setText(_translate("MainWindow", "화요일"))
        self.wed_check_box.setText(_translate("MainWindow", "수요일"))
        self.thu_check_box.setText(_translate("MainWindow", "목요일"))
        self.fri_check_box.setText(_translate("MainWindow", "금요일"))
        self.sat_check_box.setText(_translate("MainWindow", "토요일"))
        self.sun_check_box.setText(_translate("MainWindow", "일요일"))
        self.query_btn.setText(_translate("MainWindow", "검색"))

    # ------------------------------------------------------------------------------------

    def initialize(self, driver):
        self.driver = driver

        # Initialize call back function
        self.query_btn.clicked.connect(self.query)
        self.episode_list.itemDoubleClicked.connect(self.download_episode)

        # Set start time and end time
        now = datetime.datetime.now()
        now_minus_7 = now - datetime.timedelta(days=7)

        self.end_date.setMaximumDate(QtCore.QDate(now.year, now.month, now.day))
        self.end_date.dateChanged.connect(self.set_start_date_max)

        self.end_date.setDate(QtCore.QDate(now.year, now.month, now.day))
        self.start_date.setDate(QtCore.QDate(now_minus_7.year, now_minus_7.month, now_minus_7.day))

        self.init_program_list()

    def download_episode(self):
        selected_file_name = self.episode_list.currentItem().text()
        for e in self.query_result:
            if e.file_name == selected_file_name:
                e.download()

    def query(self):
        # Clear previous query result
        self.episode_list.clear()
        self.query_result = None

        # Loading query result
        program_name = self.program_list.currentItem().text()
        program_url = self.program_dict[program_name]

        # Collecting query info
        min_time = datetime.datetime.min.time()
        start_date = self.start_date.date().toPyDate()
        start_date = datetime.datetime.combine(start_date, min_time)
        end_date = self.end_date.date().toPyDate()
        end_date = datetime.datetime.combine(end_date, min_time)

        check_box_list = [self.mon_check_box, self.tue_check_box, self.wed_check_box, self.thu_check_box,
                          self.fri_check_box, self.sat_check_box, self.sun_check_box]
        checked_week_days = []
        for i, box in enumerate(check_box_list):
            if box.isChecked():
                checked_week_days.append(i)

        query_string = self.query_line.text()

        # Querying
        program_down_url = scraper.get_download_url(self.driver, program_url)
        self.query_result = scraper.get_episodes_cond(self.driver, program_down_url, start_date, end_date, checked_week_days)

        if query_string != '':
            self.query_result = [e for e in self.query_result if query_string in e.name]

        self.show_query_result()

    def show_query_result(self):
        self.episode_list.addItems([episode.file_name for episode in self.query_result])

    def set_start_date_max(self):
        self.start_date.setMaximumDate(self.end_date.date())

    def init_program_list(self):
        self.program_dict = scraper.get_programs(self.driver)
        self.program_list.addItems([name for name in self.program_dict.keys()])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
