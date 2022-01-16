from accountDatabase import accounts_database

class Login:
    user    = str
    passw   = str
    session_started = bool

    def __init__(self, user, passw):
        self.user = user
        self.passw = passw


    @property
    def username(self): 
        return self.user
    

    @username.setter
    def username(self, user):
        self.user = user


    @property
    def password(self): 
        return self.passw


    @password.setter
    def password(self, passw):
        self.passw = passw
    

    @property
    def session(self): 
        return self.session_started


    @session.setter
    def session(self, session_started):
        self.session_started = session_started

    def print_instructions(self):
        print("A continuación ingresa tu usuario y password")


    def start_session(self):
        attempts = 0
        login_success = False
        while attempts < 3:
            self.user = str(input("Usuario: "))
            self.passw = str(input("Password: "))            
            login_success = self.check_login(self.user,self.passw)
            if login_success:
                break
            attempts += 1
        
        if login_success:
            self.session_started = True
        else:
            print("Has superado el número de intentos, adios")
            self.session_started = False


    def check_login(self,user,passw):
        login_success = False
        if user in accounts_database and passw == str(accounts_database.get(user, False)):
            print("Inicio de Sesión exitoso, Bienvenido: '" + user + "'")
            login_success = True
        else:
            print("Usuario y/o Password incorrecto, vuelve a intentarlo")
            login_success = False
        return login_success
