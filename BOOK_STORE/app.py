from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
from dotenv import load_dotenv
from database import db
from config import Config
from shopping import shopping_bp

import random
import os
import razorpay

load_dotenv()


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(shopping_bp)

# Database
db.init_app(app)

# Mail
mail = Mail(app)

# ==========================================================
# RAZORPAY
# ==========================================================

RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")

client = razorpay.Client(
    auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)
)

# ==========================================================
# HOME
# ==========================================================

@app.route("/")
def home():
    return render_template("home.html")


# ==========================================================
# USER LOGIN
# ==========================================================

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
            return f"Mail Error: {e}"

    return render_template("user_login.html")


# ==========================================================
# USER SIGNUP
# ==========================================================

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


# ==========================================================
# ADMIN LOGIN
# ==========================================================

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        print(username)
        print(password)

        return redirect(url_for("admin_dashboard"))

    return render_template("admin_login.html")


# ==========================================================
# ADMIN DASHBOARD
# ==========================================================

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

# ===========================
# PAYMENT PAGE
# ===========================

@app.route("/payment")
def payment():

    cart = session.get("cart", [])

    if not cart:
        return redirect(url_for("shopping_cart"))

    total = 0

    for item in cart:

        # Support old cart items
        quantity = int(item.get("quantity", 1))
        price = float(item["price"])

        item_total = price * quantity

        total += item_total

    print("PAYMENT CART:", cart)
    print("PAYMENT TOTAL:", total)

    if total <= 0:
        return "Cart total is ₹0. Please add a book with a valid price."

    try:

        payment = client.order.create({

            "amount": int(total * 100),

            "currency": "INR",

            "payment_capture": 1

        })

        print("RAZORPAY ORDER:", payment["id"])

        return render_template(

            "payment.html",

            amount=total,

            order_id=payment["id"],

            razorpay_key=RAZORPAY_KEY_ID

        )

    except Exception as e:

        print("RAZORPAY ERROR:", e)

        return f"Razorpay Error: {e}"






# ==========================================================
# FORGOT PASSWORD
# ==========================================================

@app.route("/forgot/password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form.get("email")

        print("Forgot password email:", email)

        return redirect(url_for("otp_verify"))

    return render_template("forgot_password.html")


# ==========================================================
# OTP VERIFY
# ==========================================================

@app.route("/otp/verify", methods=["GET", "POST"])
def otp_verify():

    if request.method == "POST":

        otp = request.form.get("otp")

        print("OTP:", otp)

        return redirect(url_for("update_user"))

    return render_template("otpverify.html")


# ==========================================================
# LOGIN OTP
# ==========================================================

@app.route("/login/otp", methods=["GET", "POST"])
def login_otp():

    if request.method == "POST":

        entered_otp = request.form.get("otp")

        if entered_otp == session.get("login_otp"):

            session["user"] = session.get("login_email")

            session.pop("login_otp", None)

            return redirect(url_for("home"))

        else:
            return "Invalid OTP"

    return render_template("login_otp.html")


# ==========================================================
# UPDATE PROFILE
# ==========================================================

@app.route("/update/profile", methods=["GET", "POST"])
def update_user():

    if request.method == "POST":

        fullname = request.form.get("fullname")
        username = request.form.get("username")
        email = request.form.get("email")
        mobile = request.form.get("mobile")
        password = request.form.get("password")

        print("Full Name:", fullname)
        print("Username:", username)
        print("Email:", email)
        print("Mobile:", mobile)
        print("Password:", password)

        return redirect(url_for("home"))

    return render_template("update_user.html")


# ==========================================================
# LOGOUT
# ==========================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# ==========================================================
# CREATE DATABASE
# ==========================================================

with app.app_context():
    db.create_all()


# ==========================================================
# RUN SERVER
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)


