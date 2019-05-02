import connect
class User:

    def __init__(self, username = "null", email="null", password = "000000", phone = "0"):

        self.username  = username
        self.email     = email
        self.password  = password
        self.phone     = phone
        self.id        = "0"

    def register(self):
        

        self.username = input('please enter your prefered username : ')
        
        if not connect.check(self) :
            self.email = input('Please your email : ')
            self.phone = input('please enter phone number : ')
            self.password = input('please enter password : ')

            try:
                connect.create_table()
                print(f"Created Table {connect.table_name}.")
                connect.add(self)
            except:
                connect.add(self)
                print(f"Table {connect.table_name} Exists .!!")
        else: 
            print("\nUsername already exists please try another !!!\n")
            self.register()


    def login(self):

        username = input('please enter your username : ')
        password = input('please enter your password : ')
        check = connect.retrieve_for_authentication(username, password)
        print(check)
        if check is None:

            print('invalid username and password')

        else:

            print('you are now logged in')
            self.load_data()
        
    def load_data(self):
        user_data = connect.retrieve_all_data()
        self.username = user_data.username


user = User()
# user.register()
user.login()
