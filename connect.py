import pymysql

connection = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'scraper', charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor )

table_name = "user" #table name here

def create_table():

        """ This function is used to create a table in the database """

        with connection.cursor() as cursor:

                sql = f""" CREATE TABLE {table_name}(id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100), email VARCHAR(100), phone VARCHAR(15), password VARCHAR(100), datemodified TIMESTAMP)"""

                cursor.execute(sql)
                connection.commit()

def check_username(user):

        """ Check that the username does not exist in the user table"""

        with connection.cursor() as cursor:

                try:
                        sql = """ SELECT username FROM {} WHERE username = '{}'""".format(table_name, user.username)
                        cursor.execute(sql)

                        return len(cursor.fetchone()) > 0
                except:
                        print("Table does not exist")
                        return False

def add_user(user):

    """ Add the user information to the user table in the database"""

    with connection.cursor() as cursor:

        sql = """ INSERT INTO user(username, email, phone, password) VALUES('{}', '{}', '{}', '{}')""".format(user.username, user.email, user.phone, user.password)

        cursor.execute(sql)
        connection.commit()

def login_authentication(username, password):

        """ Retrieve and compare that the username and password provided by the user during login is accurate"""

        with connection.cursor() as cursor:

                try:
                        sql = """ SELECT username, password FROM user WHERE username = '{}' AND password = '{}'""".format(username, password)
                        cursor.execute(sql)

                        return cursor.fetchone()
                except:
                        print('The Query encountered problems')
                
def retrieve_profile(user):

        """ After login, user information needs retrieving. THis function is used to retrieve the user profile information"""

        with connection.cursor() as cursor:

                sql = """ SELECT id, username, email, phone, datemodified FROM {} WHERE username = '{}'""".format(table_name, user.username)
                cursor.execute(sql)

                return cursor.fetchone()

                