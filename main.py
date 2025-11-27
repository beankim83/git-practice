import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import QIcon

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1=QPushButton('Message', self)
        self.btn1.clicked.connect(self.activateMessage)

        self.text_edit = QPlainTextEdit()
        self.text_edit.setReadOnly(True)

        vbox = QVBoxLayout()
        vbox.addWidget(self.text_edit)
        vbox.addWidget(self.btn1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()
    
    def activateMessage(self):
        self.text_edit.appendPlainText('Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())