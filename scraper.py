import time, users, products
import requests
from bs4 import BeautifulSoup


def welcome():
    """ This function displays welcome message"""
    print("Welcome to scrapie !!!")
    welcome = input("Please select an option [register /login] : ")
    return welcome
    
    


def action(welcome):
    """ This function allows the user to select action to perform on dashboard """

    action = input("what would you like to do today [add/view/remove] ===> :")
    return action



def dashboard(action):
    """ This function is used to create dashboard """

    user = users.User()

    if welcome == "register":
        user.register()



    elif welcome == "login":
        
        user.login()
        print(f'Hello {user.username}, ')  
        product = products.Products()

        if action == "add":
            product.add()

        elif action == "view":
            product.view()
        
        elif action == "remove":
            product.remove()


    else:
        action() #Call the action process again to enter a new product name

        pass   






# while True:

#     page = requests.get("http://scholarx.co")

#     print(page)
#     print(page.status_code)
#     print(page.content)

#     soup = BeautifulSoup(page.content, 'html.parser')
#     print(soup.find_all('p'))
#     print(soup.find_all('p')[0].get_text())
#     print(soup.find('p').get_text())

#     print(soup.prettify())
#     html = list(soup.children)[2]
#     html = list(soup.children)

#     print([type(item) for item in data])
#     print(list(html.children))
#     print(html)


        









