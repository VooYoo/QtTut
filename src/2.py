import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    icon_path = r'C:\PythonWorkspace\QtTut\img\Geralt.jpg'

    def __init__(self):
        super(Window, self).__init__()

        self.set_window()

        self.buttons()
        self.progress_bar()
        self.set_main_menu()
        self.set_toolbar()
        self.show()

    def progress_bar(self):
        self.progress_dwnld = QtGui.QProgressBar(self)
        self.progress_dwnld.setGeometry(200, 80, 250, 20)

    def buttons(self):
        btn = QtGui.QPushButton('Quit', self)
        btn.clicked.connect(self.close_app)
        # print(btn.sizeHint())
        # print(btn.minimumSizeHint())
        # print(btn.size())
        btn.resize(100, 100)
        btn.move(100, 100)

        self.check_box = QtGui.QCheckBox('Enlarge Window', self)
        self.check_box.stateChanged.connect(self.enlarge_window)
        self.check_box.move(0, 50)

        self.btn_downld = QtGui.QPushButton('Download', self)
        self.btn_downld.move(200, 120)
        self.btn_downld.clicked.connect(self.download)

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def set_window(self):
        self.setGeometry(50, 50, 500, 300)
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
