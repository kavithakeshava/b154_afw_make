import time
from playwright.sync_api._generated import  Page

class LoginPage:

    __username:str #declare the variable as private

    def __init__(self,page:Page):
        self.page=page
        self.__username="#input-username" #initialization


    def set_username(self,un):
        print("enter the username:",un)
        self.page.locator(self.__username).fill(un) #utilzation
        time.sleep(2)


