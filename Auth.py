from App import MainApp
from PyQt5 import QtWidgets, uic
from MySQLHandler import MySQLHandler
from qt_material import apply_stylesheet, list_themes
class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('LoginUI.ui', self)
        self.checkRemembered()
        self.button_login.clicked.connect(self.authenticate)
        #self.main_app.button_logout.clicked.connect(self.logout)
    
    def authenticate(self):
        email = self.line_login_email.text()
        password = self.line_login_pass.text()
        try:
            mysql_handler = MySQLHandler()
            mysql_handler.connect()
            query = "select email, password from employees where email = %s and password = %s"
            values = email, password
            auth = None
            auth = mysql_handler.fetch_data(query, values)
            print(auth)
            mysql_handler.disconnect()
            
            if auth:
                authenticated = True
                if self.cb_remember.isChecked():
                    try:
                        with open("remember.text", "w")as f:
                            f.write(email)
                    except Exception as e:
                        print("Error writing remmber to file: {e}")
                #self.self.line_login_email.clear()
                #self.self.line_login_pass.clear()
                self.start_main()
            else:
                print("wrong login!")
        except Exception as err:
            print("Login error: {err}")
        
    def logout(self):
        if self.main_app:
            self.main_app.quit()
            self.show()
    
    def start_main(self):
        self.main_app = MainApp()
        self.hide()

        apply_stylesheet(self.main_app, theme=read, extra=extra)
        self.main_app.page_setting.comboBox_themes.setCurrentText(read)
            # apply_stylesheet(app, theme='light_blue.xml', css_file='custom.css')
        self.main_app.adjustSize()
        self.main_app.showMaximized()
        self.main_app.show()
        
    def checkRemembered(self):
        try:
            with open("remember.text", "r") as f:
                content = f.read()
                if content:
                    self.line_login_email.setText(content.strip())
                    self.cb_remember.setChecked(True)
        except FileNotFoundError:
            print("File not found.")
        except Exception as err:
            print(f"Error reading file: {err}") 
extra = {
    # Density Scale
    "density_scale": "-2",
}
with open("config.txt", "r") as f:
            read = f.read()   
            if not read:
                read = "dark_medical.xml"
if __name__=="__main__":
    app = QtWidgets.QApplication([])
    login_window = LoginWindow()
    apply_stylesheet(login_window, theme=read, extra=extra)
    login_window.show()
    app.exec_()
