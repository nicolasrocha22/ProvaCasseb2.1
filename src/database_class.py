import sys
import pymysql
import database_runner as runner


class Database:
    def connect_db(self):
        login = runner.DBRunner()
        host = login.get_host()
        user = login.get_user()
        password = login.get_password()
        db = login.get_database()

        config = {
            "host": host,
            "user": user,
            "password": password,
            "database": db
        }

        global database
        global cursor

        try:
            database = pymysql.connect(**config)
            cursor = database.cursor()
        except pymysql.err.OperationalError:
            sys.exit("[ERROR]: Fail to connect with the database!")

    def create_table_db(self):
        """Creates a new table in the database called "registry" if it doesn't exist"""
        try:
            command = """CREATE TABLE IF NOT EXISTS registry (
                movie_title VARCHAR(50),
                movie_code INT,
                client_name VARCHAR(50),
                client_id INT NOT NULL
            );"""

            cursor.execute(command)
            database.commit()
        except:
            database.rollback()

    def add_values_db(self, mt, mc, cn, ci):
        """Adds values ​​to the "registry" table in the database"""
        try:
            command = """INSERT INTO registry(movie_title, movie_code, client_name, client_id)
            VALUES (%s, %s, %s, %s);"""
            val = (mt, mc, cn, ci)

            cursor.execute(command, val)
            database.commit()
        except:
            database.rollback()

    def modify_values_db(self, mt, mc, ci):
        """Modifys the values ​​of the "registry" table in the database"""
        try:
            command = "UPDATE registry SET movie_title = %s WHERE client_id = %s;"
            val = (mt, ci)
            cursor.execute(command, val)

            command = "UPDATE registry SET movie_code = %s WHERE client_id = %s;"
            val = (mc, ci)
            cursor.execute(command, val)

            database.commit()
        except:
            database.rollback()

    def delete_values_db(self, ci):
        """Deletes values from the "registry" table in the database"""
        try:
            command = "DELETE FROM registry WHERE client_id = %s;"
            val = ci

            cursor.execute(command, val)
            database.commit()
        except:
            database.rollback()

    def drop_table_db(self):
        """Deletes the "registry" table from the database
        WARNING: This function should only be used in tests"""
        try:
            command = "DROP TABLE IF EXISTS registry;"

            cursor.execute(command)
            database.commit()
        except:
            database.rollback()

    def show_table_db(self):
        """Shows values of the "registry" table from the database"""
        try:
            command = "SELECT * FROM registry;"

            cursor.execute(command)
            return cursor.fetchall()
        except:
            return False

    def close_db(self):
        cursor.close()
        database.close()
