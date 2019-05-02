import pymysql

connection = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'db', charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor )

table_name = "user" #table name here

def create_table():

    with connection.cursor() as cursor:

        try:
                sql = f""" CREATE TABLE {table_name}(id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100), emailAddress VARCHAR(100), phoneNumber VARCHAR(15), password VARCHAR(100))"""

                cursor.execute(sql)
                connection.commit()
        except:
                print('Table already exists')

def add(user):

    with connection.cursor() as cursor:

        sql = """ INSERT INTO user(username, emailAddress, phoneNumber, password) VALUES('{}', '{}', '{}', '{}')""".format(user.username, user.email, user.phone, user.password)

        cursor.execute(sql)
        connection.commit()

def retrieve_for_authentication(username, password):

        with connection.cursor() as cursor:

                try:
                        sql = """ SELECT username, password FROM user WHERE username = '{}' AND password = '{}'""".format(username, password)
                        cursor.execute(sql)

                        return cursor.fetchone()
                except:
                        print('The username or password not found')
                

def check(user):

        with connection.cursor() as cursor:

                try:
                        sql = """ SELECT username FROM {} WHERE username = '{}'""".format(table_name, user.username)
                        cursor.execute(sql)

                        return len(cursor.fetchone()) > 0
                except:
                        print("Table does not exist")
                        return False
                        