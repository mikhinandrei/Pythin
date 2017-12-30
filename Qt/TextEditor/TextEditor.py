__author__ = 'Admin'
import sys
from PyQt4 import QtGui, QtCore
#from find import *
import shelve


TITLE = 'TextEditor'
FORMATS = 'All Files (*);;Penguin text file (*.pt);;Python files (*.py;*.pyw);;Text Files (*.txt)'


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(300, 200)
        self.setWindowTitle("PenguinEditor")
        self.setWindowIcon(QtGui.QIcon('icons/penguin.png'))

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

        ############### FILE MENU ###############################################3
        new = QtGui.QAction(QtGui.QIcon('icons/new.ico'), 'New...', self)
        new.setShortcut('Ctrl+N')
        new.setStatusTip('Create new file')
        self.connect(new, QtCore.SIGNAL('triggered()'), self.createNew)

        exit = QtGui.QAction(QtGui.QIcon('icons/out.ico'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit Application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), self.end)

        save = QtGui.QAction(QtGui.QIcon('icons/save.ico'), 'Save...', self)
        save.setShortcut('Ctrl+S')
        save.setStatusTip('Save File')
        self.connect(save, QtCore.SIGNAL('triggered()'), self.showSaveDialog)

        saveAs = QtGui.QAction('Save As...', self)
        saveAs.setShortcut('Ctrl+Shift+S')
        saveAs.setStatusTip('Save file as...')
        self.connect(saveAs, QtCore.SIGNAL('triggered()'), self.saveFileAs)

        openFile = QtGui.QAction(QtGui.QIcon('icons/folder.ico'), 'Open...', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        self.connect(openFile, QtCore.SIGNAL('triggered()'), self.showOpenDialog)

        exportPdf = QtGui.QAction('Export to PDF', self)
        exportPdf.setShortcut('Ctrl+E')
        exportPdf.setStatusTip('Export to PDF')
        self.connect(exportPdf, QtCore.SIGNAL('triggered()'), self.exportToPDF)

        printer = QtGui.QAction('Print...', self)
        printer.setShortcut('Ctrl+P')
        printer.setStatusTip('Print file')
        self.connect(printer, QtCore.SIGNAL('triggered()'), self.runPrinter)

        ################## EDIT MENU ###############################################
        undo = QtGui.QAction('Undo...', self)
        undo.setShortcut('Ctrl+Z')
        undo.setStatusTip("Undo")
        self.connect(undo, QtCore.SIGNAL('triggered()'), self.textEdit.undo)

        redo = QtGui.QAction('Redo...', self)
        redo.setShortcut('Ctrl+Y')
        redo.setStatusTip("Redo...")
        self.connect(redo, QtCore.SIGNAL('triggered()'), self.textEdit.redo)

        copy = QtGui.QAction('Copy...', self)
        copy.setShortcut('Ctrl+C')
        copy.setStatusTip("Copy...")
        self.connect(copy, QtCore.SIGNAL('triggered()'), self.textEdit.copy)

        paste = QtGui.QAction('Paste...', self)
        paste.setShortcut('Ctrl+V')
        paste.setStatusTip("Paste...")
        self.connect(paste, QtCore.SIGNAL('triggered()'), self.textEdit.paste)

        cut = QtGui.QAction('Cut...', self)
        cut.setShortcut('Ctrl+X')
        cut.setStatusTip("Cut...")
        self.connect(cut, QtCore.SIGNAL('triggered()'), self.textEdit.cut)

        ################## WINDOW MENU #############################################
        setBgColor = QtGui.QAction('Set background color...', self)
        setBgColor.setStatusTip('Change background color')
        self.connect(setBgColor, QtCore.SIGNAL('triggered()'), self.changeBackgroundColor)

        setFontColor = QtGui.QAction('Set font color...', self)
        setFontColor.setStatusTip('Change font color')
        self.connect(setFontColor, QtCore.SIGNAL('triggered()'), self.changeFontColor)

        setFont = QtGui.QAction('Change font...', self)
        setFont.setStatusTip('Change font in text editor')
        self.connect(setFont, QtCore.SIGNAL('triggered()'), self.changeFont)

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(new)
        file.addAction(openFile)
        file.addAction(save)
        file.addAction(saveAs)
        file.addAction(printer)
        file.addAction(exportPdf)
        file.addSeparator()
        file.addAction(exit)

        edit =menubar.addMenu('&Edit')
        edit.addAction(undo)
        edit.addAction(redo)
        edit.addSeparator()
        edit.addAction(copy)
        edit.addAction(cut)
        edit.addAction(paste)

        window = menubar.addMenu('&Window')
        window.addAction(setBgColor)
        window.addAction(setFontColor)
        window.addAction(setFont)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(new)
        toolbar.addAction(openFile)
        toolbar.addAction(save)
        toolbar.addAction(exit)

        area = QtGui.QMdiArea()

        self.loadSettings()

    def okToContinue(self):
        if self.textEdit.document().isModified():
            q = QtGui.QMessageBox.warning(self, "PenguinEditor", "The document was modified\nWould You like to save changes?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel)
            if q == QtGui.QMessageBox.Yes:
                return self.showSaveDialog()
            elif q == QtGui.QMessageBox.Cancel:
                return False
        return True

    def createNew(self):
        if self.okToContinue():
            self.textEdit.setText('')
            self.setWindowTitle('New.txt')

    def showOpenDialog(self):
        if not self.okToContinue():
            return False
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File..', None, FORMATS)
        if not filename:
            return False
        file = open(filename)
        data = file.read()
        self.textEdit.setText(data)
        self.setWindowTitle(filename)
        return True

    def showSaveDialog(self):
        text = self.textEdit.toPlainText()
        if not text:
            self.setStatusTip("Nothing to save")
            return False
        if self.windowTitle() != 'PenguinEditor' and self.windowTitle() != 'New.txt':
            filename = self.windowTitle()
        else:
            filename = QtGui.QFileDialog.getSaveFileName(self, 'Save As', '.', FORMATS)
        if not filename:
            self.setStatusTip("Not correct name")
            return False
        file = open(filename, 'w')
        file.write(text)
        self.setWindowTitle(filename)
        file.close()
        self.setStatusTip("Succesfully saved")
        self.textEdit.document().setModified(False)
        return True

    def saveFileAs(self):
        text = self.textEdit.toPlainText()
        if not text:
            self.setStatusTip("Nothing to save")
            return False
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save As', '.', FORMATS)
        if not filename:
            self.setStatusTip("Not correct name")
            return False
        file = open(filename, 'w')
        file.write(text)
        self.setWindowTitle(filename)
        file.close()
        self.setStatusTip("Succesfully saved")
        self.textEdit.document().setModified(False)
        return True

    def changeBackgroundColor(self):
        color = QtGui.QColorDialog.getColor()
        if not color:
            return False
        file = shelve.open('style/settings')
        bgColor = color.name()
        file['bgColor'] = bgColor
        file.close()
        self.loadSettings()
        return True

    def changeFontColor(self):
        color = QtGui.QColorDialog.getColor()
        if not color:
            return False
        file = shelve.open('style/settings')
        fontColor = color.name()
        file['fontColor'] = fontColor
        file.close()
        self.loadSettings()
        return True

    def changeFont(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            file = shelve.open('style/settings')
            font = QtGui.QFont.toString(font)
            e = font.split(',')
            font = e[0]
            size = e[1]
            file['font'] = font
            file['size'] = size
            file.close()
            self.loadSettings()
            return True

    def loadSettings(self):
        file = shelve.open('style/settings')
        bgColor = file['bgColor']
        fontColor = file['fontColor']
        font = file['font']
        size = file['size']
        xi = "QWidget { background-color: " + bgColor + " ;color: ", fontColor, ";font-family:", font, ";font-size:", size,"pt;}"
        style = ''.join(x for x in xi)
        self.textEdit.setStyleSheet(style)
        #self.textEdit.setFont(qfont)

    def runPrinter(self):
        p = QtGui.QPrinter()
        dialog = QtGui.QPrintDialog(p, self)
        if dialog.exec() == QtGui.QDialog.Accepted:
            self.textEdit.print_(p)

    def askYesNo(self, title, q):
        question = QtGui.QMessageBox.question(self, title, q, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if question == QtGui.QMessageBox.Yes:
            return True
        else:
            return False

    def end(self):
        if self.okToContinue():
            sys.exit()
            return True
        else:
            return False

    def exportToPDF(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (*.pdf)")
        if not filename:
            return False
        #if QtCore.QFileInfo(filename).suffix().isEmpty():
            #filename += '.pdf'
        printer = QtGui.QPrinter()
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        self.textEdit.document().print_(printer)
        return True


def main():
    app = QtGui.QApplication(sys.argv)
    splash = QtGui.QSplashScreen(QtGui.QPixmap('icons/penguin.jpg'))
    splash.show()
    main = MainWindow()
    main.show()
    splash.finish(main)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()