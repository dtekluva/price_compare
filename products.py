import connect #Import the database connection module 
import datetime




class Products:  #create a product object

    def __init__(self, name = "null", date_modified = "d"):
        
        """ __init__ gives the User object properties and attributes like name, etc."""

        self.name          = name
        self.budget        = "0"
        self.id            = "0"
        self.date_modified = date_modified
        
         

    def add(self):
        """ this function allows the user to add products"""

        self.name = input('please enter the name of the product : ') #Get the product name from user
        self.budget = input('please enter your budget for this product : ') #Get user budget

        if not connect.check_product(self): #Check that the product does not exist already in the database

            try: #Try to create and populate a table if it does not exist in the database

                connect.products_table #create the table in the database
                print("Created products table")
                connect.new_product(self) #Populate the table with the product details

            except: #populate the table in the database if it already exists

                connect.new_product(self)
                print("products table Exists .!!")
        else: #product already exists
            print("\n product already exists please try another !!!\n")
            self.add() #Call the registration process again to enter a new product name






# connect.products_table()

# product = Products()
# product.add()

          