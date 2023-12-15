from PyQt5 import QtWidgets, uic, QtCore
from MySQLHandler import MySQLHandler
from qt_material import apply_stylesheet, list_themes
from Employee import Employee, Employees
import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
#Warning.filterwarnings("ignore")
class LoginWindow(QtWidgets.QMainWindow):
    login_reference_signal = QtCore.pyqtSignal(object)
    def __init__(self):
        super().__init__()
        uic.loadUi('LoginUI.ui', self)
        self.employee:Employee = None
        self.checkRemembered()
        self.button_login.clicked.connect(self.authenticate)
        self.wrong_login.hide()
        #self.main_app.button_logout.clicked.connect(self.logout)
    
    def authenticate(self):
        email = self.line_login_email.text().strip()
        password = self.line_login_pass.text().strip()
        try:
            mysql_handler = MySQLHandler()
            mysql_handler.connect()
            query = "select email, password from employees where email = %s"
            values = email
            auth = None
            auth = mysql_handler.fetch_data(query, (values,))
            print(auth[0][0])
            mysql_handler.disconnect()
            
            if auth[0][0].strip()==email and auth[0][1].strip()==password:
                #authenticated = True
                self.wrong_login.hide()
                if self.cb_remember.isChecked():
                    try:
                        with open("remember.text", "w")as f:
                            f.write(email)
                    except Exception as e:
                        print("Error writing remmber to file: {e}")
                #self.self.line_login_email.clear()
                #self.self.line_login_pass.clear()
                self.line_login_pass.clear()
                for e in Employees:
                    if email == e.email:
                        self.employee = e
                self.start_main()
            elif email == '' or password == '':
                self.wrong_login.show()
                self.wrong_login.setText("Please fill all fields!")
            else:
                self.line_login_pass.clear()
                self.wrong_login.show()
                self.wrong_login.setText("Wrong Login Info!").show()
        except Exception as err:
            print("Login error: {err}")
    
    def start_main(self):
        try:
            #from App import MainApp
            self.hide()
            self.login_reference_signal.emit(self)
            '''
            apply_stylesheet(self.main_app, theme=read, extra=extra)
            
            self.main_app.page_setting.comboBox_themes.setCurrentText(read)
                # apply_stylesheet(app, theme='light_blue.xml', css_file='custom.css')
            self.main_app.adjustSize()
            self.main_app.showMaximized()
            self.main_app.show()
            '''
        except Exception as err:
            self.show()
            print("Error starting main app: {err}")
        
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
    from App import MainApp
    app = QtWidgets.QApplication([])
    
    main_app = MainApp()
    login_window = LoginWindow()
    
    login_window.login_reference_signal.connect(main_app.handleLoginReference)
    invert:bool = False
    if "light" in read:
        invert = True   
    apply_stylesheet(main_app, theme=read, invert_secondary=invert, extra=extra,  css_file="custom.css")
    apply_stylesheet(login_window, theme=read, invert_secondary=invert, extra=extra,  css_file="custom.css")
    #login_window.adjustSize()
    login_window.show()
    app.exec_()
