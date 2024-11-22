Bus Ticket Booking App
Welcome to the Bus Ticket Booking App, a Python-based project that was created with ease in mind in making bookings for bus tickets. This application showcases both the user and administrator sides, providing ease of use without sacrificing robust functionality.

Features
For Users:
User Account Creation
Users can create an account with their information, including name, email, phone number, and location.

View Available Routes
Users can view available routes with their respective departure times and the number of seats available in each.

Book Tickets
Users select a route or input a custom location to book their tickets. Immediately after booking, the seat availability automatically changes.

Receive Confirmation Messages
Upon booking, it sends a confirmation message to the user's phone.

View Booking History
Users view their booking history along with complete details of the ticket and timestamp of bookings.

For Administrator:
Admin Account Creation and Login
Admins can create a secure account and log in to manage the app's features.

View All Bookings
Admins can view all tickets booked by users, including user details and ticket information.

Add New Routes
Admins can add new routes, specifying departure times and seat availability.

Change Admin Password
Admins can securely update their password if needed.

How It Works
Upon launching, the app greets the user and asks if they are a User or Admin.
Users' functionality includes account creation, route browsing, and ticket booking; users can also see their booking history.
Admins can log in to go into the admin dashboard and look at bookings or add new routes, or they may want to change their password.
Team Contributions
This project was a collaborative project by our group, where each one contributed to the specific parts of the code.

Prince: He created the User and Admin modules. He implemented a User class for maintaining user information like name, email, phone, and location, including methods to handle the display of user information. On the admin side, he provided an Admin class which securely sets up admin credentials using the function set_credentials. In his development, he laid the foundation to effectively manage users and admins.

Promesse: He worked on enhancing the Admin functionalities, implementing features that enable the admin to manage the system effectively. He developed the login method for secure access, the change_password method for updating credentials, and the view_all_bookings method to display user booking details. Additionally, he created the add_place function, allowing the admin to add new routes with departure times and seat availability. His contributions ensure robust admin control and flexibility in managing the app’s operations.

Christian: He worked on designing key structural components of the app, focusing on managing routes and ticketing functionalities. He developed the Place class to define routes with attributes like departure times, seat availability, and methods for booking and checking seat availability. He also created the Ticket class to handle ticket generation with booking timestamps. Additionally, Gisa contributed to the BusTicketBooking class by initializing routes, incorporating predefined locations, and setting up a shared booking list. His work laid the foundation for efficient route management and ticket processing in the application.

Gisa: He worken on creating and managing the core functionalities of the BusTicketBooking system. Gisa implemented methods for user creation, route selection, ticket booking, and sending confirmation messages. He also developed functions for viewing user booking history and built the admin interface, enabling features like adding new routes, managing bookings, and resetting credentials. Additionally, the contributor designed the main application flow, allowing users to navigate between user and admin roles seamlessly. His work ensures the application operates efficiently, offering a smooth and interactive experience for both users and admins.

Running the Application
Make sure Python 3 is installed on your computer.
Save the code in a file with the name BusTicket.py
Execute the application with the following command:
python3 BusTicket.py
The application will start, and you will be prompted on your screen to start working as a User or Admin.
Future Development
We would like to improve the application by the following:

Showing Real-time Seat Availability.
Allowing User Authentication for security purposes.
Thank you for using Bus Ticket Booking Application!
