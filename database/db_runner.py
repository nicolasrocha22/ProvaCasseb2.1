import configparser

class Runner:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password


class DBRunner(Runner):
    login = configparser.ConfigParser()
    login.read("db.ini")

    host_login = login["Connection"]["Host"]
    user_login = login["Connection"]["User"]
    password_login = login["Connection"]["Password"]
    database_login = login["Connection"]["Database"]

    def __init__(
        self,
        host = host_login,
        user = user_login,
        password = password_login,
        database = database_login
    ):
        super().__init__(user, password)
        self.host = host
        self.database = database

    def get_host(self):
        return self.host

    def get_user(self):
        return super().get_user()

    def get_password(self):
        return super().get_password()

    def get_database(self):
        return self.database
