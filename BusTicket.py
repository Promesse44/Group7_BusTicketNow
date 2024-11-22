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

class Place:
    def __init__(self, place_name, time, seats=20):
        self.place_name = place_name
        self.time = time
        self.seats = seats

    def has_available_seat(self):
        return self.seats > 0

    def book_seat(self):
        if self.has_available_seat():
            self.seats -= 1
            return True
        return False

    def get_place_info(self):
        return f"{self.place_name} (Departs at {self.time}) - Available Seats: {self.seats}"

class Ticket:
    def __init__(self, ticket_name):
        self.ticket_name = ticket_name
        self.timestamp = datetime.now()  # Automatically sets the booking timestamp

    def get_ticket_info(self):
        return f"Ticket for {self.ticket_name}, Booked at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

class BusTicketBooking:
    def __init__(self):
        self.user = None
        self.admin = Admin()  # Initialize Admin without credentials
        self.places = {
            1: Place('Nyanza - Nyabugogo', '10:00 AM'),
            2: Place('Remera - Nyabugogo', '1:00 PM'),
            3: Place('Karama - Kigali', '9:30 AM'),
            4: Place('Gahanga - Kigali', '2:45 PM')
        }
        self.bookings = []  # Shared booking list
