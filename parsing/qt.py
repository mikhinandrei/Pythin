from PyQt4 import QtGui, QtCore
import sys

app = QtGui.Application(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle('Hello, World!!!')
window.resize(300, 70)
label = QtGui.QLabel('<center>Hello, World!!!</center>')
btn = QtGui.QPushButton('Close Window')
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label, btn)
window.setLayout(vbox)
QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT('quit()'))
window.show()
sys.exit(app.exec_())
