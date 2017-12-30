import sys
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(600, 450)
        self.setWindowTitle("Курс валюты")

        self.createWidgets()

    def createWidgets(self):
        # create QActions

        menubar = self.menuBar()
        file = menubar.addMenu('Файл')
        # File Actions
        edit = menubar.addMenu('Правка')

        toolbar = self.addToolBar('Выход')


def main():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()