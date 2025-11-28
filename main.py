import sys
from PyQt5.QtWidgets import QApplication
from ui import View
from ctrl import Control

def main():
    app = QApplication(sys.argv)
    view = View()
    ctrl = Control(view=view)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()