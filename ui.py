from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QPlainTextEdit, QHBoxLayout)
from PyQt5.QtGui import QIcon

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1=QPushButton('Message', self)
        self.btn_reset=QPushButton('Reset', self)
        self.text_edit = QPlainTextEdit()
        self.text_edit.setReadOnly(True)

        vbox = QVBoxLayout()
        vbox.addWidget(self.text_edit)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn_reset)
        
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()
