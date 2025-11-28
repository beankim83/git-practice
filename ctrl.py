class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.activateMessage)
        self.view.btn_reset.clicked.connect(self.clearMessage)

    def activateMessage(self):
        self.view.text_edit.appendPlainText('Button clicked!')

    def clearMessage(self):
        self.view.text_edit.clear()
