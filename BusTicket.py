#!/usr/bin/env python3
from datetime import datetime

class User:
    def __init__(self, name, email, telephone, location):
        self.name = name
        self.email = email
        self.telephone = telephone
        self.location = location
    
    def get_user_info(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.telephone}, Location: {self.location}"

class Admin:
    def __init__(self):
        self.username = None
        self.password = None

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

