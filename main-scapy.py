from PyQt5 import QtCore, QtGui, QtWidgets
import scapy.all as scapy
import time
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(334, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 321, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 171, 31))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 161, 27))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setGeometry(QtCore.QRect(70, 80, 171, 35))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 291, 351))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 40, 171, 31))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.toolButton_3 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_3.setGeometry(QtCore.QRect(70, 160, 171, 35))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(80, 10, 161, 27))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 110, 61, 31))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 110, 61, 31))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(110, 80, 101, 27))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(150, 110, 16, 27))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 210, 291, 281))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(90, 540, 161, 27))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionOpen_Result = QtWidgets.QAction(MainWindow)
        self.actionOpen_Result.setObjectName(_fromUtf8("actionOpen_Result"))
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        self.toolButton.clicked.connect(check1)
        self.toolButton_3.clicked.connect(check2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Network Scanning Tool v1.0", None))
        self.label_2.setText(_translate("MainWindow", "Enter IP Address:", None))
        self.toolButton.setText(_translate("MainWindow", "Scan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "IP Scanner", None))
        self.toolButton_3.setText(_translate("MainWindow", "Scan", None))
        self.label_4.setText(_translate("MainWindow", "Enter IP Address:", None))
        self.label_5.setText(_translate("MainWindow", "Port Range:", None))
        self.label_6.setText(_translate("MainWindow", "-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Port Scanner", None))
        self.label.setText(_translate("MainWindow", "Networks & SpaceCode Team 2021", None))
        self.actionOpen_Result.setText(_translate("MainWindow", "Open ", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit_2.setText(_translate("MainWindow", "Exit", None))


def IP_Address(addr):
    ui.textEdit.append('Scanning IP addresses....')
    ui.textEdit.repaint() # for update the textEdit immediately not wait to all function to finish

    # Try ARPing the ip address range supplied by the user.
    # The arping() method in scapy creates a pakcet with an ARP message
    # and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff.
    # If a valid ip address range was supplied the program will return
    # the list of all results.
    ans, unans = scapy.arping(addr)
    return ans


def check1():
    ui.textEdit.clear()
    start_time = time.monotonic()
    user_IP = ui.lineEdit.text()
    x = str(user_IP.split(".")[0]) + "." + str(user_IP.split(".")[1]) + "." + str(user_IP.split(".")[2]) + "."
    x = x + '0/24'
    ans = IP_Address(x)
    ui.textEdit.clear()
    for result in ans.res:
        printing = ("%s - %s" % (result[0].payload.pdst, result[1].payload.hwsrc))
        ui.textEdit.append(printing)
    ui.textEdit.append('--------------------------------------------------------')
    ui.textEdit.append("Time used: %s seconds" % (time.monotonic() - start_time))


def Port(host_IP, frst, last):
    ui.textEdit_3.repaint() # for update the textEdit immediately not wait to all function to finish
    ui.textEdit_3.clear()
    start_time = time.monotonic()
    for dport in range(frst, last):
        pkt = scapy.IP(dst=host_IP) / scapy.TCP(dport=dport)
        ans, unans = scapy.sr(pkt, timeout=1)
        if ans:
            for send, rcv in ans:
                if rcv[scapy.TCP].flags == "SA":
                    port_s = (' Port %d   ->     OPEN' % (dport))
                    ui.textEdit_3.append(port_s)
    ui.textEdit_3.append('--------------------------------------------------------')
    ui.textEdit_3.append("Time used: %s seconds" % (time.monotonic() - start_time))


def check2():
    ui.textEdit_3.clear()
    user_IP = ui.lineEdit_3.text()
    x = str(user_IP.split(".")[0]) + "." + str(user_IP.split(".")[1]) + "." + str(user_IP.split(".")[2]) + "." + str(
        user_IP.split(".")[3])
    frst_port = int(ui.lineEdit_5.text())
    last_port = int(ui.lineEdit_6.text())
    ui.textEdit_3.append('Scanning Open Ports.....')
    Port(x, frst_port, last_port)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
