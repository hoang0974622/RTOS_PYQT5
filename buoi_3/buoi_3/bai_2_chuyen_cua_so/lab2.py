from PyQt5 import QtCore, QtGui, QtWidgets


class PageWindow(QtWidgets.QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)


class loginWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("LOGIN")
        self.initUI()

    def initUI(self):
        self.UiComponents()

    def UiComponents(self):
        self.resize(400,400)
        self.loginButton = QtWidgets.QPushButton("LOGIN", self)
        self.loginButton.setGeometry(QtCore.QRect(220, 140, 181, 81))
        self.loginButton.clicked.connect(
            self.make_handleButton("LOGIN")
        )

    def make_handleButton(self, button):
        def handleButton():
            if button == "LOGIN":
                self.goto("main")
        return handleButton


class SearchWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Setting")
        self.UiComponents()
        self.resize(400,400)

    def goToMain(self):
        self.goto("main")

    def UiComponents(self):
        self.backButton = QtWidgets.QPushButton("OK", self)
        self.backButton.setGeometry(QtCore.QRect(220, 140, 181, 81))
        self.backButton.clicked.connect(self.goToMain)

class mainWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Main")
        self.UiComponents()
        self.resize(400,400)

    def goToLogin(self):
        self.goto("login")
    def goToMain(self):
        self.goto("setting")

    def UiComponents(self):
        self.backButton = QtWidgets.QPushButton("Setting", self)
        self.backButton.setGeometry(QtCore.QRect(220, 50, 181, 81))
        self.backButton.clicked.connect(self.goToMain)
        self.logoutButton = QtWidgets.QPushButton("Logout", self)
        self.logoutButton.setGeometry(QtCore.QRect(220, 140, 181, 81))
        self.logoutButton.clicked.connect(self.goToLogin)

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}

        self.register(loginWindow(), "login")
        self.register(SearchWindow(), "setting")
        self.register(mainWindow(), "main")

        self.goto("login")
        self.initUI()
    def initUI(self):
        self.resize(600,400)

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())