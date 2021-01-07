from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QMainWindow, qApp, QAction, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.menubar = self.menuBar()
        self.UI()

    def UI(self):
        self.menuBarItems()
        self.fileMenuMap()

        grid = QGridLayout()

        layout = QWidget()
        layout.setLayout(grid)
        #self.setStyleSheet("background-color: #FFFFFF")
        self.setCentralWidget(layout)
        self.setGeometry(2080, 90, 1600, 900)
        self.setWindowTitle("Test App")
        self.showFullScreen()
        #self.show()

    def fileMenuMap(self):
        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(self.setAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

    def menuBarItems(self):
        self.exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Exit application')
        self.exitAct.triggered.connect(qApp.quit)

        self.setAct = QAction(QIcon('settings.png'), 'Settings', self)
        self.setAct.setShortcut('Ctrl+,')
        self.setAct.setStatusTip('Open settings')
        self.setAct.triggered.connect(self.open_settings)

    def buttons(self):
        self.button1 = QtWidgets.QPushButton("Settings")
        self.button1.clicked.connect(self.open_settings)

    def open_settings(self):
        self.settings.show()


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.label1 = QtWidgets.QLabel('exp:')
        self.label2 = QtWidgets.QLabel('')

        self.line1 = QtWidgets.QLineEdit('')
        self.line1.returnPressed.connect(self.printLine)

        self.closeBut = QtWidgets.QPushButton('Close')
        self.closeBut.clicked.connect(self.close_window)

        grid1 = QGridLayout()
        grid1.addWidget(self.label1, 0, 0)
        grid1.addWidget(self.line1, 0, 1, 0, 2)

        grid2 = QGridLayout()
        grid2.addWidget(self.closeBut, 0, 0)
        grid2.addWidget(self.label2, 0, 1, 0, 2)

        gridV1 = QVBoxLayout()
        gridV1.addLayout(grid1)
        gridV1.addLayout(grid2)

        self.setLayout(gridV1)
        self.setWindowFlag(Qt.FramelessWindowHint)
        #self.setStyleSheet("background-color: #FFFFFF")
        self.setGeometry(2084, 118, 300, 50)
        self.setWindowTitle("Test App - Settings")

    def printLine(self):
        print(self.line1.text())

    def close_window(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())
