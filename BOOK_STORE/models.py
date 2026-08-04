from BOOK_STORE.database import db


# ---------------- USER TABLE ----------------

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    fullname = db.Column(db.String(100), nullable=False)

    username = db.Column(db.String(50), unique=True, nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    mobile = db.Column(db.String(15), nullable=False)

    password = db.Column(db.String(200), nullable=False)


# ---------------- ADMIN TABLE ----------------

class Admin(db.Model):

    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)


# ---------------- BOOK TABLE ----------------

class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    author = db.Column(db.String(100), nullable=False)

    category = db.Column(db.String(100), nullable=False)

    price = db.Column(db.Float, nullable=False)

    stock = db.Column(db.Integer, nullable=False)

    description = db.Column(db.Text)

    image = db.Column(db.String(255))


# ---------------- CART TABLE ----------------

class Cart(db.Model):

    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)

    book_id = db.Column(db.Integer, nullable=False)

    quantity = db.Column(db.Integer, default=1)


# ---------------- ORDER TABLE ----------------

class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)

    total_amount = db.Column(db.Float, nullable=False)

    status = db.Column(db.String(30), default="Pending")