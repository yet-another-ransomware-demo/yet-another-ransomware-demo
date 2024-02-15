from PyQt5 import QtWidgets

import sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ransomware Demo")
        l = QtWidgets.QLabel("This is a ransomware!")
        l.setMargin(10)
        self.setCentralWidget(l)
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()
