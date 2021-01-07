from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QMainWindow
import sys

class variables:
    def __init__(self):
        super(variables, self).__init__()
        self.sizing()
        self.style()
        self.names()

    def sizing(self):
        self.margin_left = 16
        self.margin_right = 16
        self.margin_top = 16
        self.margin_bottom = 16

        self.spacing = 8

        self.width = 1920
        self.height = 1080

        self.section1_width = 0.70       # 1% -> 0.01  10% -> 0.1  100% -> 1
        self.section2_1_height = 0.60

    def style(self):
        self.nordic_button = 'QPushButton{background-color: #2D3340; border-radius: 10px;}  ' \
                      'QPushButton:pressed{background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,' \
                      ' stop: 0 #97C2C3, stop: 1 #86ADAC);}  '
        self.nordic_background = 'background-color: #3D4454;'
        self.widget_border = 'border-color: #555555; border-style: solid; border-width: 3px; border-radius: 10px;'

    def names(self):
        self.window_title = 'Base Qt5'


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.v = variables()

        self.main()

        self.mainbox_layout()

        self.section2_layout()
        self.utilbox_layout()
        self.buttonbox_layout()

    def main(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.setSpacing(self.v.spacing)
        self.main_layout.setContentsMargins(self.v.margin_left, self.v.margin_top,
                                            self.v.margin_right, self.v.margin_bottom)

        layout = QWidget()
        layout.setLayout(self.main_layout)

        self.setStyleSheet(self.v.nordic_background)
        self.setCentralWidget(layout)
        self.setWindowTitle(self.v.window_title)
        self.setGeometry(0, 0, self.v.width, self.v.height)
        self.showFullScreen()

    def mainbox_layout(self):
        width = (self.v.width - self.v.margin_left - self.v.margin_right - self.v.spacing) * self.v.section1_width
        height = self.v.height - self.v.margin_top - self.v.margin_bottom

        self.mainbox = QWidget()
        self.mainbox.setFixedSize(width, height)
        self.mainbox.setStyleSheet(self.v.widget_border)

        self.main_layout.addWidget(self.mainbox)

    def section2_layout(self):
        self.section2 = QVBoxLayout()
        self.section2.setSpacing(self.v.spacing)
        self.section2.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addLayout(self.section2)

    def utilbox_layout(self):
        width = (self.v.width - self.v.margin_left - self.v.margin_right - self.v.spacing) * (1 - self.v.section1_width)
        height = (self.v.height - self.v.margin_top - self.v.margin_bottom - self.v.spacing) * self.v.section2_1_height

        self.utilbox = QWidget()
        self.utilbox.setFixedSize(width, height)
        self.utilbox.setStyleSheet(self.v.widget_border)

        self.section2.addWidget(self.utilbox)

    def buttonbox_layout(self):
        width = (self.v.width - self.v.margin_left - self.v.margin_right - self.v.spacing) * (1 - self.v.section1_width)
        height = (self.v.height - self.v.margin_top - self.v.margin_bottom - self.v.spacing) * (1 - self.v.section2_1_height)

        self.buttonbox = QWidget()
        self.buttonbox.setFixedSize(width, height)
        self.buttonbox.setStyleSheet(self.v.widget_border)

        self.section2.addWidget(self.buttonbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())
