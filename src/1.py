import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    icon_path = r'../img/Geralt.jpg'

    def __init__(self):
        super(Window, self).__init__()

        self.set_window()

        self.buttons()
        self.progress_bar()
        self.set_main_menu()
        self.set_toolbar()

        self.styles()
        self.layout()
        self.show()

    def layout(self):
        self.setGeometry(50, 50, 300, 220)

        self.comboBox.move(20, 125)
        self.styleChoice.move(20, 100)
        self.progress_dwnld.setGeometry(20, 160, 250, 20)
        self.btn_quit.setGeometry(150, 75, 75, 75)
        self.check_box.move(20, 75)
        self.btn_downld.move(20, 180)

    def styles(self):
        # QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
        # todo
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("costam", self)
        print(QtGui.QStyleFactory.keys())
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem("motif")
        self.comboBox.addItem("Windows")
        self.comboBox.addItem("cde")
        self.comboBox.addItem("Plastique")
        self.comboBox.addItem("Cleanlooks")
        self.comboBox.addItem("windowsvista")
        self.comboBox.addItem('WindowsXP')
        self.comboBox.activated[str].connect(self.style_choice)

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def progress_bar(self):
        self.progress_dwnld = QtGui.QProgressBar(self)

    def buttons(self):
        self.btn_quit = QtGui.QPushButton('Quit', self)
        self.btn_quit.clicked.connect(self.close_app)
        # print(self.btn_quit.sizeHint())
        # print(self.btn_quit.minimumSizeHint())
        # print(self.btn_quit.size())

        self.check_box = QtGui.QCheckBox('Enlarge Window', self)
        self.check_box.stateChanged.connect(self.enlarge_window)

        self.btn_downld = QtGui.QPushButton('Download', self)
        self.btn_downld.clicked.connect(self.download)

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def set_window(self):
        self.setWindowTitle('VooYoo')
        self.setWindowIcon(QtGui.QIcon(self.icon_path))

    def set_main_menu(self):
        menu_exit = QtGui.QAction('Exit', self)
        menu_exit.setShortcut("q")
        menu_exit.setStatusTip('Exit')
        menu_exit.triggered.connect(self.close_app)
        menu_exit.setIcon(QtGui.QIcon(self.icon_path))

        self.statusBar()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        file_menu.addAction(menu_exit)

    def set_toolbar(self):
        tlbr_exit = QtGui.QAction(QtGui.QIcon(self.icon_path), 'Exit', self)
        tlbr_exit.triggered.connect(self.close_app)

        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(tlbr_exit)

        fontChoice = QtGui.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)

        # self.toolbar = self.addToolBar("Font")
        self.toolbar.addAction(fontChoice)

        # color = QtGui.QColor(0, 0, 0)
        #
        # fontColor = QtGui.QAction('Font bg Color', self)
        # fontColor.triggered.connect(self.color_picker)
        #
        # self.toolbar.addAction(fontColor)
        #
        # cal = QtGui.QCalendarWidget(self)
        # cal.setGeometry(500, 200, 200, 200)

    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
            QtGui.QApplication.setFont(font)

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.00001
            self.progress_dwnld.setValue(self.completed)

    def close_app(self):
        choice = QtGui.QMessageBox.question(self, 'Exit', 'Exit?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()


def main():
    app = QtGui.QApplication(sys.argv)
    _ = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
