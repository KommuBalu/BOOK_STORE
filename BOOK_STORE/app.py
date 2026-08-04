from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.secret_key = "bookstore123"


# ================= HOME =================

@app.route("/")
def home():
    return render_template("home.html")


# ================= USER LOGIN =================

@app.route("/user/login", methods=["GET", "POST"])
def user_login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        print("Username :", username)
        print("Password :", password)

        return redirect(url_for("home"))

    return render_template("user_login.html")


# ================= USER SIGNUP =================

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


# ================= ADMIN LOGIN =================

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        print(username)
        print(password)

        return redirect(url_for("admin_dashboard"))

    return render_template("admin_login.html")


# ================= ADMIN DASHBOARD =================

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")


# ================= ADD PRODUCTS =================

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


# ================= MANAGE PRODUCTS =================

@app.route("/admin/manageproducts")
def manage_products():
    return render_template("admin_manageproducts.html")


# ================= SHOPPING CART =================

@app.route("/shopping/cart")
def shopping_cart():
    return render_template("shopping_cart.html")


# ================= PAYMENT =================

@app.route("/payment", methods=["GET", "POST"])
def payment():

    if request.method == "POST":

        payment_method = request.form.get("payment")

        print("Payment Method :", payment_method)

        return redirect(url_for("order_success"))

    return render_template("payment.html")


# ================= ORDER SUCCESS =================

@app.route("/order/success")
def order_success():
    return render_template("order_success.html")


# ================= USER ORDERS =================

@app.route("/user/orders")
def user_orders():
    return render_template("user_orders.html")


# ================= FORGOT PASSWORD =================

@app.route("/forgot/password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form.get("email")

        print(email)

        return redirect(url_for("otp_verify"))

    return render_template("forgot_password.html")


# ================= OTP VERIFY =================

@app.route("/otp/verify", methods=["GET", "POST"])
def otp_verify():

    if request.method == "POST":

        otp = request.form.get("otp")

        print("OTP :", otp)

        return redirect(url_for("update_user"))

    return render_template("otpverify.html")


# ================= UPDATE USER =================

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


# ================= LOGOUT =================

@app.route("/logout")
def logout():
    return redirect(url_for("home"))


# ================= RUN APP =================

if __name__ == "__main__":
    app.run(debug=True)