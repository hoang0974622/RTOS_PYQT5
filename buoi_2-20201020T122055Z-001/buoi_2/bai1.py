# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bai1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 384)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_tinh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tinh.setGeometry(QtCore.QRect(160, 230, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_tinh.setFont(font)
        self.pushButton_tinh.setObjectName("pushButton_tinh")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 290, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_kq = QtWidgets.QLabel(self.centralwidget)
        self.label_kq.setGeometry(QtCore.QRect(140, 290, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_kq.setFont(font)
        self.label_kq.setText("")
        self.label_kq.setObjectName("label_kq")
        self.label_a = QtWidgets.QLabel(self.centralwidget)
        self.label_a.setGeometry(QtCore.QRect(120, 30, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_a.setFont(font)
        self.label_a.setObjectName("label_a")
        self.lineEdit_a = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_a.setGeometry(QtCore.QRect(150, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_a.setFont(font)
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.label_a_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_a_2.setGeometry(QtCore.QRect(120, 100, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_a_2.setFont(font)
        self.label_a_2.setObjectName("label_a_2")
        self.lineEdit_b = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_b.setGeometry(QtCore.QRect(150, 100, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_b.setFont(font)
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 180, 241, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_cong = QtWidgets.QRadioButton(self.widget)
        self.radioButton_cong.setObjectName("radioButton_cong")
        self.horizontalLayout.addWidget(self.radioButton_cong)
        self.radioButton_tru = QtWidgets.QRadioButton(self.widget)
        self.radioButton_tru.setObjectName("radioButton_tru")
        self.horizontalLayout.addWidget(self.radioButton_tru)
        self.radioButton_nhan = QtWidgets.QRadioButton(self.widget)
        self.radioButton_nhan.setObjectName("radioButton_nhan")
        self.horizontalLayout.addWidget(self.radioButton_nhan)
        self.radioButton_chia = QtWidgets.QRadioButton(self.widget)
        self.radioButton_chia.setObjectName("radioButton_chia")
        self.horizontalLayout.addWidget(self.radioButton_chia)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_tinh.clicked.connect(self.tinh)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bài 1"))
        self.pushButton_tinh.setText(_translate("MainWindow", "Tính"))
        self.label.setText(_translate("MainWindow", "Kq:"))
        self.label_a.setText(_translate("MainWindow", "a"))
        self.label_a_2.setText(_translate("MainWindow", "b"))
        self.radioButton_cong.setText(_translate("MainWindow", "+"))
        self.radioButton_tru.setText(_translate("MainWindow", "-"))
        self.radioButton_nhan.setText(_translate("MainWindow", "x"))
        self.radioButton_chia.setText(_translate("MainWindow", "/"))
        self.label_kq.setText(_translate("MainWindow", "Kết quả"))

    def congAB(self):
        if self.radioButton_cong.isChecked() == True:
            self.cong = int(self.lineEdit_a.text()) + int(self.lineEdit_b.text())
            self.label_kq.setText(str(self.cong))

    def truAB(self):
        if self.radioButton_tru.isChecked() == True:
            self.tru = int(self.lineEdit_a.text()) - int(self.lineEdit_b.text())
            self.label_kq.setText(str(self.tru))

    def nhanAB(self):
        if self.radioButton_nhan.isChecked() == True:
            self.nhan = int(self.lineEdit_a.text()) * int(self.lineEdit_b.text())
            self.label_kq.setText(str(self.nhan))

    def chiaAB(self):
        if self.radioButton_chia.isChecked() == True:
            self.chia = int(self.lineEdit_a.text()) / int(self.lineEdit_b.text())
            self.label_kq.setText(str(self.chia))

    def tinh(self):
        self.congAB()
        self.truAB()
        self.nhanAB()
        self.chiaAB()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
