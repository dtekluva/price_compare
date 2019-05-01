import connect
class User:

    # def __init__(self, name):

    #     self.name  = name

    def register(self):

        username = input('please enter your prefered username')
        self.name = username
        email = input('Please your email')
        phone_number = input('please enter phone number')
        password = input('please enter password')
        new_user = [self.name, email,phone_number,password]

        #connect.create_table()
        connect.add(new_user)


    def login(self):

        username = input('please enter your username')
        password = input('please enter your password')
        check = connect.retrieve_for_authentication(username, password)
        print(check)
        if check is None:

            print('invalid username and password')

        else:

            print('you are now logged in')

user = User()
#user.register()
user.login()
