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

    def view_all_bookings(self, bookings):
        """Display all booked tickets with user information."""
        print("All Booked Tickets:")
        if not bookings:
            print("No bookings found.")
        else:
            for booking in bookings:
                print(f"{booking['user'].get_user_info()} - {booking['ticket'].get_ticket_info()}")

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

    def create_user(self):
        """Prompt for user information and create a User instance."""
        name = input("Please enter your name: ")
        email = input("Please enter your email: ")
        telephone = input("Please enter your telephone: ")
        location = input("Please enter your location: ")
        self.user = User(name, email, telephone, location)
        print(f"User created: {self.user.get_user_info()}")

    def display_places(self):
        """Display available routes and departure times with numbered choices."""
        print("Available Routes and Departure Times:")
        for number, place in self.places.items():
            print(f"{number}. {place.get_place_info()}")

    def select_place(self):
        """Allow user to select a place or enter a custom location."""
        while True:
            try:
                choice = int(input("Enter the number of the route you'd like to book, or 0 for a custom location, or 'b' to go back: "))
                if choice in self.places:
                    selected_place = self.places[choice]
                    if selected_place.book_seat():
                        print(f"Booking confirmed for {selected_place.place_name} at {selected_place.time}")
                        self.create_ticket(selected_place.place_name)
                        self.send_confirmation_message(selected_place.place_name)
                        break
                    else:
                        print("Sorry, no seats available for this route.")
                elif choice == 0:
                    custom_location = input("Enter the custom location you'd like to book: ")
                    self.create_ticket(custom_location)
                    self.send_confirmation_message(custom_location)
                    break
                elif choice == 'b':
                    break
                else:
                    print("Invalid choice. Please select a valid route number or 0 for a custom location.")
            except ValueError:
                print("Please enter a valid number.")

    def create_ticket(self, place_name):
        """Create a ticket, add it to the user's booking history, and store it in the shared booking list."""
        ticket = Ticket(place_name)
        self.bookings.append({"user": self.user, "ticket": ticket})  # Store booking with user and ticket details
        print(f"Ticket created: {ticket.get_ticket_info()}")

    def send_confirmation_message(self, place_name):
        """Simulate sending a confirmation message to the user's phone."""
        print(f"Confirmation message sent to {self.user.telephone}: 'Your ticket for {place_name} has been confirmed.'")

    def view_tickets(self):
        """Display all tickets booked by the user."""
        print("Your booking history:")
        user_bookings = [b for b in self.bookings if b["user"] == self.user]
        if not user_bookings:
            print("No tickets booked yet.")
        else:
            for booking in user_bookings:
                print(booking["ticket"].get_ticket_info())

    def admin_access(self):
        """Handles admin access, including initial setup and login."""
        if not self.admin.username or not self.admin.password:
            # Admin setup
            self.admin.set_credentials()
        
        # Admin login
        if self.admin.login():
            self.admin_dashboard()

    def admin_dashboard(self):
        """Admin dashboard options for viewing bookings and adding places."""
        while True:
            admin_choice = input("Enter '1' to view all bookings, '2' to add a new route, '3' to change password, or 'b' to go back: ")
            if admin_choice == '1':
                self.admin.view_all_bookings(self.bookings)
            elif admin_choice == '2':
                self.admin.add_place(self.places)
            elif admin_choice == '3':
                self.admin.change_password()
            elif admin_choice == 'b':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def start_app(self):
        """Main loop for switching between 'User' and 'Admin' modes."""
        while True:
            user_type = input("Welcome! Are you a 'User' or 'Admin'? Enter 'q' to quit. ").lower()
            if user_type == 'user':
                self.create_user()
                while True:
                    self.display_places()
                    self.select_place()
                    if input("Enter 'b' to go back or any key to continue: ").lower() == 'b':
                        break
                    self.view_tickets()
            elif user_type == 'admin':
                self.admin_access()
            elif user_type == 'q':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter either 'User', 'Admin', or 'q' to quit.")

# Running the program
if __name__ == "__main__":
    booking_system = BusTicketBooking()
    booking_system.start_app()
