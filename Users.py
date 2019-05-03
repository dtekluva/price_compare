import connect #Import the databse connection module 

class User: #create a user object

    def __init__(self, username = "null", email="null", password = "000000", phone = "0", date_modified = "d"): 

        """ __init__ gives the User object properties and attributes like
        name, email, password etc."""

        self.username  = username
        self.email     = email
        self.password  = password
        self.phone     = phone
        self.id        = "0"
        self.date_modified = date_modified

    def register(self):
        
        """ this function allows the user to register"""

        self.username = input('please enter your prefered username : ') #Get the username input from an intended user
        
        if not connect.check_username(self): #Check that the username does not exist already in the database

            self.email = input('Please your email : ')   # Collect further information from the user email,phone and password.
            self.phone = input('please enter phone number : ')
            self.password = input('please enter password : ')

            try: #Try to create and populate a table if it does not exist in the database

                connect.create_table() #create the table in the database
                print(f"Created Table {connect.table_name}.")
                connect.add_user(self) #Populate the table with the user details

            except: #populate the table in the database if it already exists

                connect.add(self)
                print(f"Table {connect.table_name} Exists .!!")
        else: #Username already exists
            print("\nUsername already exists please try another !!!\n")
            self.register() #Call the registration process again to enter a new username


    def login(self):

        """ this function allows the user to login to the system and have access to their information"""

        username = input('please enter your username : ') #enter username
        password = input('please enter your password : ') # enter password
        check = connect.login_authentication(username, password) #Check that the username and password exists in the database
        print(check)
        if check is None: # username or password does not exist  

            print('invalid username and password')
            self.login() #restart login process

        else: #username and password exists

            print('you are now logged in')
            self.username = check['username'] #set username for profile to be retrieved
            self.load_data() #load user data
        
    def load_data(self): 

        """ This function is used to retreive all customer information after login"""

        user_data = connect.retrieve_profile(self) #retrieve all information for a logged in user
        self.username = user_data['username']    
        self.email    = user_data['email']
        self.phone    = user_data['phone']
        self.id       = user_data['id']
        self.date_modified = user_data['datemodified']

        print(f"username {self.username}\nemail {self.email} \nphone {self.phone}") #Print the information to screen


user = User()
# user.register()
user.login()
