
from database import db


# ===========================
# USER TABLE
# ===========================

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    fullname = db.Column(db.String(100), nullable=False)

    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    mobile = db.Column(db.String(15))

    password = db.Column(db.String(255), nullable=False)


# ===========================
# ADMIN TABLE
# ===========================

class Admin(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True)

    password = db.Column(db.String(255))


# ===========================
# BOOK TABLE
# ===========================

class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    author = db.Column(db.String(100))

    category = db.Column(db.String(100))

    price = db.Column(db.Integer)

    stock = db.Column(db.Integer)

    description = db.Column(db.Text)

    image = db.Column(db.String(255))


# ===========================
# CART TABLE
# ===========================

class Cart(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    book_id = db.Column(db.Integer)

    quantity = db.Column(db.Integer, default=1)


# ===========================
# ORDER TABLE
# ===========================

class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    total_amount = db.Column(db.Integer)

    payment_id = db.Column(db.String(150))

    status = db.Column(db.String(50), default="Pending")