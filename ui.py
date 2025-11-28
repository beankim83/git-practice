from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QPlainTextEdit, QHBoxLayout, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1=QPushButton('Message', self)
        self.btn_reset=QPushButton('Reset', self)
        self.text_edit = QPlainTextEdit()
        self.text_edit.setReadOnly(True)

        self.lbl_date = QLabel(QDate.currentDate().toString('yyyy년 MM월 dd일 dddd'), self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.text_edit)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn_reset)
        
        vbox.addLayout(hbox)
        vbox.addWidget(self.lbl_date)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()
