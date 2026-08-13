📚BOOK STORE – Online Book Shopping System

🎯 Project Objective

The BOOK STORE project is a modern web application that allows users to browse books, add books to a shopping cart, make secure online payments, and manage orders. It also includes an admin panel for managing books and integrates Gmail OTP authentication and Razorpay online payments.

💻 Frontend Technologies
.HTML5
.CSS3
.Responsive Web Design
.Jinja2 Templates (Flask)
.Flexbox
.CSS Grid
.Media Queries
.Custom CSS Animations
⚙️ Backend Technologies
.Python 3.12
.Flask Framework
.Flask-Mail
.Flask Sessions
.Jinja2 Template Engine
.Razorpay Python SDK
.Random Module (OTP Generation)
🗄 Database
.SQLite3
(Current project database)
Future upgrade:

.MySQL
.PostgreSQL

📧 Email Service
Gmail SMTP
Used for
.Login OTP
.Password Reset OTP
.Payment Verification OTP

Using

Flask-Mail
smtp.gmail.com
TLS
App Password

💳 Payment Gateway
Razorpay
Features

.Online Payment
.UPI
.Debit Card
.Credit Card
.Net Banking
.Wallet
.QR Payment
🔐 Authentication
.User Login
.User Registration
.Gmail OTP Verification
.Forgot Password
.Session Login
.Logout


🛒 Shopping Features
Book Listing
Add to Cart
Remove Cart
Clear Cart
Total Amount Calculation
Shopping Cart
📚 Book Management

Admin can

Add Books
Upload Book Image
Manage Products
Update Stock
View Products
👤 User Features
Register
Login
Gmail OTP
Browse Books
Add to Cart
Payment
Order Success
View Orders
Update Profile
👨‍💼 Admin Features
Admin Login
Dashboard
Add Products
Manage Products



🎨 UI Design

Modern Responsive UI

Includes

Hero Banner
Navigation Bar
Book Cards
Hover Effects
Responsive Grid
Modern Buttons
Shadow Effects
Rounded Cards


📂 Project Structure

BOOK_STORE/

│
├── app.py
│
├── templates/
│      home.html
│      user_login.html
│      user_signup.html
│      admin_login.html
│      admin_dashboard.html
│      shopping_cart.html
│      payment.html
│      order_success.html
│      otpverify.html
│      login_otp.html
│      forgot_password.html
│      update_user.html
│
├── static/
│      css/
│          home.css
│
│      images/
│          home.jpg
│          Python.png
│          SQL.png
│          FLASK.png
│
└── database
       SQLite

📦 Python Packages Used

Flask
Flask-Mail
Flask-SQLAlchemy
Flask-WTF
Razorpay
Jinja2
SQLite
Werkzeug
email-validator
python-dotenv


=======Development Tools Used=========
IDE
Visual Studio Code
Programming Language
Python
Version Control
Git
GitHub
Browser
Google Chrome
Testing
Flask Development Server
Package Manager
pip
Virtual Environment
venv
External Services
Gmail SMTP Server
Razorpay Payment Gateway



Website Flow


Home Page
      │
      ▼
User Registration
      │
      ▼
User Login
      │
      ▼
Gmail OTP Verification
      │
      ▼
Home Page
      │
      ▼
Browse Books
      │
      ▼
Add to Cart
      │
      ▼
Shopping Cart
      │
      ▼
Payment (Razorpay)
      │
      ▼
Payment Success
      │
      ▼
Email OTP Verification
      │
      ▼
Order Success
      │
      ▼
User Orders


Current Features Completed
Responsive Home Page
User Registration
User Login
Gmail OTP Login
Admin Login
Shopping Cart
Add to Cart
Remove Cart
Clear Cart
Razorpay Payment Integration
Payment Success Page
Forgot Password
Update Profile
Logout
Responsive Book Grid
Hero Banner
External CSS Structure
Suggested Future Enhancements
Store user data in a SQL database instead of printing to the console.
Add password hashing using Werkzeug or bcrypt.
Verify Razorpay payment signatures for secure payment confirmation.
Create an order history stored in the database.
Add book search, filtering, and categories.
Implement user profile photos.
Add admin features for editing and deleting books.
Include order invoices (PDF generation).
Integrate SMS OTP as an alternative to email OTP.
Deploy the application on a cloud platform such as AWS, Azure, or Render.
Resume Project Description

BOOK STORE – Online Book Shopping System

Developed a full-stack web application using Python Flask and SQLite 
that enables users to browse books, register, log in with Gmail OTP verification,
manage a shopping cart, and complete secure online payments through Razorpay.
The application includes an admin dashboard for product management,
responsive UI built with HTML5, CSS3, and Jinja2, and integrates Flask-Mail for email notifications and OTP verification.
It follows a modular architecture and uses Git/GitHub for version control.
