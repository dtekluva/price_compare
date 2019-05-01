import pymysql

connection = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'Scraper', charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor )

def create_table():

    with connection.cursor() as cursor:

        try:
                sql = """ CREATE TABLE User(id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100), emailAddress VARCHAR(100), phoneNumber VARCHAR(15), password VARCHAR(100))"""

                cursor.execute(sql)
                connection.commit()
        except:
                print('Table already exists')

def add(user_profile):

    with connection.cursor() as cursor:

        sql = """ INSERT INTO User(username, emailAddress, phoneNumber, password) VALUES('{}', '{}', '{}', '{}')""".format(user_profile[0], user_profile[1], user_profile[2], user_profile[3])

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
                