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

#this is the funtion that set the credentials of the admin
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

#function for user's information(Admin)
    def login(self):
        """Login method for admin with username and password."""
        if not self.username or not self.password:
            print("Admin account not set up. Please set up your account first.")
            return False

        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if self.username == username and self.password == password:
            print("Admin login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False

#when the inputed information is wrong the user is prompted to change password.
    def change_password(self):
        """Allow the admin to change the password."""
        current_password = input("Enter your current password: ")
        if self.password == current_password:
            new_password = input("Enter your new password: ")
            confirm_password = input("Confirm your new password: ")
            if new_password == confirm_password:
                self.password = new_password
                print("Password changed successfully.")
            else:
                print("New passwords do not match.")
        else:
            print("Incorrect current password.")

#Method that allows admin to view all bookings
    def view_all_bookings(self, bookings):
        """Display all booked tickets with user information."""
        print("All Booked Tickets:")
        if not bookings:
            print("No bookings found.")
        else:
            for booking in bookings:
                print(f"{booking['user'].get_user_info()} - {booking['ticket'].get_ticket_info()}")

#function that help Admin add new routes
    def add_place(self, places):
        """Add a new route to the available places."""
        place_name = input("Enter the name of the new route: ")
        time = input("Enter the departure time (e.g., '10:00 AM'): ")
        seats = int(input("Enter the number of seats available: "))
        new_place = Place(place_name, time, seats)
        place_number = max(places.keys()) + 1
        places[place_number] = new_place
        print(f"Route '{place_name}' added with departure at {time} and {seats} seats available.")
