#!/usr/bin/env python3
from datetime import datetime
#this is the class of the User
class User:
    def __init__(self, name, email, telephone, location):
        self.name = name
        self.email = email
        self.telephone = telephone
        self.location = location


    #this is the function that get the user information
    def get_user_info(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.telephone}, Location: {self.location}"

#this is the class of admin that contain the data of the admin
class Admin:
    def __init__(self):
        self.username = None
        self.password = None

#this is the funtion that set the credentials of the admin and admin can view bookinga ang add routhes and try to fix the essue the user will meet
    def set_credentials(self):
        """Set up admin username and password for the first time."""
        print("Set up your admin account:")
        self.username = input("Enter admin username: ")
        password = input("Set admin password: ")
        confirm_password = input("Confirm admin password: ")
        if password == confirm_password:
            self.password = password
            print("Admin account set up successfully.")
        else:
            print("Passwords do not match. Please try again.")
            self.set_credentials()

