from flask import Flask, render_template, request, redirect, url_for, session
from models import User, Admin, Book, Cart, Order
from config import Config
from database import db
from flask_mail import Mail, Message
import random
import razorpay
from flask import Flask
from config import Config


from dotenv import load_dotenv
import os

load_dotenv()





# Create Flask app FIRST
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

# Gmail
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT"))
app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS") == "True"
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

# Razorpay
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")

client = razorpay.Client(
    auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)
)


# ===========================
# HOME
# ===========================

@app.route("/")
def home():
    return render_template("home.html")


# ===========================
# USER LOGIN
# ===========================




@app.route("/user/login", methods=["GET", "POST"])
def user_login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        # Generate OTP
        otp = str(random.randint(100000, 999999))

        session["login_email"] = email
        session["login_otp"] = otp

        try:
            msg = Message(
                "BOOK STORE Login OTP",
                sender=app.config["MAIL_USERNAME"],
                recipients=[email]
            )

            msg.body = f"""
Hello,

Your BOOK STORE Login OTP is:

{otp}

Do not share this OTP.

Thank You
BOOK STORE
"""

            mail.send(msg)

            print("OTP Sent:", otp)

            return redirect(url_for("login_otp"))

        except Exception as e:
            return f"Mail Error : {e}"

    return render_template("user_login.html")


# ===========================
# USER SIGNUP
# ===========================

@app.route("/user/signup", methods=["GET", "POST"])
def user_signup():

    if request.method == "POST":

        fullname = request.form.get("fullname")
        username = request.form.get("username")
        email = request.form.get("email")
        mobile = request.form.get("mobile")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        print(fullname)
        print(username)
        print(email)
        print(mobile)
        print(password)
        print(confirm_password)

        return redirect(url_for("user_login"))

    return render_template("user_signup.html")


# ===========================
# ADMIN LOGIN
# ===========================

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        print(username)
        print(password)

        return redirect(url_for("admin_dashboard"))

    return render_template("admin_login.html")


# ===========================
# ADMIN DASHBOARD
# ===========================

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")


# ===========================
# ADD PRODUCT
# ===========================

@app.route("/admin/addproducts", methods=["GET", "POST"])
def add_products():

    if request.method == "POST":

        title = request.form.get("title")
        author = request.form.get("author")
        category = request.form.get("category")
        price = request.form.get("price")
        stock = request.form.get("stock")
        description = request.form.get("description")

        image = request.files.get("image")

        print(title)
        print(author)
        print(category)
        print(price)
        print(stock)
        print(description)

        if image:
            print(image.filename)

        return redirect(url_for("manage_products"))

    return render_template("admin_addproducts.html")


# ===========================
# MANAGE PRODUCTS
# ===========================

@app.route("/admin/manageproducts")
def manage_products():
    return render_template("admin_manageproducts.html")


# ===========================
# ADD TO CART
# ===========================

@app.route("/add/cart")
def add_cart():

    book_name = request.args.get("book_name")
    price = request.args.get("price")

    cart = session.get("cart", [])

    cart.append({
        "book_name": book_name,
        "price": price
    })

    session["cart"] = cart

    return redirect(url_for("shopping_cart"))


# ===========================
# SHOPPING CART
# ===========================

@app.route("/shopping/cart")
def shopping_cart():

    cart = session.get("cart", [])

    total = 0

    for item in cart:
        total += int(item["price"])

    return render_template(
        "shopping_cart.html",
        cart=cart,
        total=total
    )


# ===========================
# REMOVE CART ITEM
# ===========================

@app.route("/remove/cart/<int:index>")
def remove_cart(index):

    cart = session.get("cart", [])

    if 0 <= index < len(cart):
        cart.pop(index)

    session["cart"] = cart

    return redirect(url_for("shopping_cart"))


# ===========================
# CLEAR CART
# ===========================

@app.route("/clear/cart")
def clear_cart():

    session["cart"] = []

    return redirect(url_for("shopping_cart"))

# # ===========================
# # PAYMENT PAGE
# # ===========================

# @app.route("/payment")
# def payment():

#     cart = session.get("cart", [])

#     total = 0

#     for item in cart:
#         total += int(item["price"])

#     payment = client.order.create({
#         "amount": total * 100,
#         "currency": "INR",
#         "payment_capture": 1
#     })

#     return render_template(
#         "payment.html",
#         amount=total,
#         order_id=payment["id"],
#         razorpay_key=RAZORPAY_KEY_ID
#     )


# ===========================
# PAYMENT PAGE
# ===========================

@app.route("/payment")
def payment():

    cart = session.get("cart", [])

    total = 0

    for item in cart:
        total += int(item["price"])

    payment = client.order.create({
        "amount": total * 100,
        "currency": "INR",
        "payment_capture": 1
    })

    return render_template(
        "payment.html",
        amount=total,
        order_id=payment["id"],
        razorpay_key=RAZORPAY_KEY_ID
    )


# ===========================
# PAYMENT SUCCESS
# ===========================

@app.route("/payment/success", methods=["POST"])
def payment_success():

    payment_id = request.form.get("razorpay_payment_id")
    order_id = request.form.get("razorpay_order_id")
    signature = request.form.get("razorpay_signature")

    print("Payment ID :", payment_id)
    print("Order ID   :", order_id)
    print("Signature  :", signature)

    # Here you can verify Razorpay signature
    # client.utility.verify_payment_signature(...)

    # Send OTP after successful payment
    return redirect(url_for("send_payment_otp"))

# ===========================
# ORDER SUCCESS
# ===========================

@app.route("/order/success")
def order_success():
    return render_template("order_success.html")


# ===========================
# USER ORDERS
# ===========================

@app.route("/user/orders")
def user_orders():
    return render_template("user_orders.html")


# ===========================
# FORGOT PASSWORD
# ===========================

@app.route("/forgot/password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form.get("email")

        print(email)

        return redirect(url_for("otp_verify"))

    return render_template("forgot_password.html")


# ===========================
# OTP VERIFY
# ===========================

@app.route("/otp/verify", methods=["GET", "POST"])
def otp_verify():

    if request.method == "POST":

        otp = request.form.get("otp")

        print("OTP :", otp)

        return redirect(url_for("update_user"))

    return render_template("otpverify.html")


@app.route("/login/otp", methods=["GET", "POST"])
def login_otp():

    if request.method == "POST":

        entered_otp = request.form.get("otp")

        if entered_otp == session.get("login_otp"):

            session["user"] = session["login_email"]

            session.pop("login_otp", None)

            return redirect(url_for("home"))

        else:
            return "Invalid OTP"

    return render_template("login_otp.html")


# ===========================
# UPDATE PROFILE
# ===========================

@app.route("/update/profile", methods=["GET", "POST"])
def update_user():

    if request.method == "POST":

        fullname = request.form.get("fullname")
        username = request.form.get("username")
        email = request.form.get("email")
        mobile = request.form.get("mobile")
        password = request.form.get("password")

        print(fullname)
        print(username)
        print(email)
        print(mobile)
        print(password)

        return redirect(url_for("home"))

    return render_template("update_user.html")


# ===========================
# LOGOUT
# ===========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# ===========================
# RUN SERVER
# ===========================

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)