import sys
from PyQt4 import QtCore, QtGui


class Player():
    pass

class GameWindow(QtGui.QMainWindow):
    total_money = '0000000000'
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.create_widgets()

    def create_widgets(self):
        self.resize(535, 300)
        self.setWindowTitle("Хозяин Таверны")

        display_money = QtGui.QLabel("Всего денег: " + self.total_money)

        vbox = QtGui.QVBoxLayout()
        vbox.setMargin(5)
        vbox.addWidget(display_money)
        widget = QtGui.QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(vbox)


def main():
    app = QtGui.QApplication(sys.argv)
    main = GameWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()