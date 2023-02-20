import sys
from main import DatabaseConnector


class MyDb:
    def __init__(self):
        self.db = DatabaseConnector()
        self.menu()

    def menu(self):

        user_input = int(input(
            """
            1. Enter 1 to register
            2. Enter 2 to login
            3. Enter anything to exit
            """
        ))

        if user_input == 1:
            self.register()
        elif user_input == 2:
            self.login()
        else:
            sys.exit(400)

    def register(self):
        name = input("Enter Name")
        email = input("Enter Email")
        password = input("Enter password")

        response = self.db.register(name, email, password)

        if response:
            print("Registered")
        else:
            print("Failed to register")
        self.menu()

    def login(self):
        email = input("Enter your Email")
        password = input("Enter Password")

        data = self.db.search(email, password)
        if len(data) == 0:
            print("Not registered")
            self.menu()
        else:
            print("Sucessfully loged in")
            print(f'Hello {data[0][1]}')


obj = MyDb()