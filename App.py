import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        #self.page_test_ui = uic.loadUi('test.ui')
        #self.stackedWidget.addWidget(self.page_test_ui)
        #self.button_test.clicked.connect(self.show_test)

   # def show_test(self):
    #    self.stackedWidget.setCurrentWidget(self.page_test_ui)


if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
