from flask import Blueprint, render_template, request, redirect, url_for, session


# ==========================================================
# SHOPPING BLUEPRINT
# ==========================================================

shopping_bp = Blueprint("shopping", __name__)


# ==========================================================
# ADD PRODUCT
# ==========================================================

@shopping_bp.route("/admin/addproducts", methods=["GET", "POST"])
def add_products():

    if request.method == "POST":

        title = request.form.get("title")
        author = request.form.get("author")
        category = request.form.get("category")
        price = request.form.get("price")
        stock = request.form.get("stock")
        description = request.form.get("description")

        image = request.files.get("image")

        print("Title:", title)
        print("Author:", author)
        print("Category:", category)
        print("Price:", price)
        print("Stock:", stock)
        print("Description:", description)

        if image:
            print("Image:", image.filename)

        return redirect(url_for("shopping.manage_products"))

    return render_template("admin_addproducts.html")


# ==========================================================
# MANAGE PRODUCTS
# ==========================================================

@shopping_bp.route("/admin/manageproducts")
def manage_products():

    return render_template("admin_manageproducts.html")


# ==========================================================
# ADD TO CART
# ==========================================================

@shopping_bp.route("/add/cart")
def add_cart():

    book_name = request.args.get("book_name")
    price = request.args.get("price")

    if not book_name or not price:
        return "Book name or price is missing"

    try:
        price = float(price)
    except ValueError:
        return "Invalid price"

    cart = session.get("cart", [])

    found = False

    for item in cart:

        if item["book_name"] == book_name:

            item["quantity"] = int(
                item.get("quantity", 1)
            ) + 1

            found = True
            break

    if not found:

        cart.append({
            "book_name": book_name,
            "price": price,
            "quantity": 1
        })

    session["cart"] = cart
    session.modified = True

    print("CART:", cart)

    return redirect(url_for("shopping.shopping_cart"))


# ==========================================================
# INCREASE QUANTITY
# ==========================================================

@shopping_bp.route("/cart/increase/<int:index>")
def increase_quantity(index):

    cart = session.get("cart", [])

    if 0 <= index < len(cart):

        cart[index]["quantity"] = int(
            cart[index].get("quantity", 1)
        ) + 1

        session["cart"] = cart
        session.modified = True

    return redirect(url_for("shopping.shopping_cart"))


# ==========================================================
# DECREASE QUANTITY
# ==========================================================

@shopping_bp.route("/cart/decrease/<int:index>")
def decrease_quantity(index):

    cart = session.get("cart", [])

    if 0 <= index < len(cart):

        quantity = int(
            cart[index].get("quantity", 1)
        )

        if quantity > 1:

            cart[index]["quantity"] = quantity - 1

        else:

            cart.pop(index)

        session["cart"] = cart
        session.modified = True

    return redirect(url_for("shopping.shopping_cart"))


# ==========================================================
# REMOVE CART ITEM
# ==========================================================

@shopping_bp.route("/remove/cart/<int:index>")
def remove_cart(index):

    cart = session.get("cart", [])

    print("BEFORE REMOVE:", cart)
    print("REMOVE INDEX:", index)

    if 0 <= index < len(cart):

        removed_item = cart.pop(index)

        print("REMOVED:", removed_item)

        session["cart"] = cart
        session.modified = True

    else:

        print("INVALID CART INDEX")

    print("AFTER REMOVE:", session.get("cart", []))

    return redirect(url_for("shopping.shopping_cart"))


# ==========================================================
# SHOPPING CART
# ==========================================================

@shopping_bp.route("/shopping/cart")
def shopping_cart():

    cart = session.get("cart", [])

    total = 0

    for item in cart:

        if "quantity" not in item:
            item["quantity"] = 1

        price = float(item["price"])
        quantity = int(item["quantity"])

        total += price * quantity

    session["cart"] = cart
    session.modified = True

    print("CART:", cart)
    print("TOTAL:", total)

    return render_template(
        "shopping_cart.html",
        cart=cart,
        total=total
    )


# ==========================================================
# CLEAR CART
# ==========================================================

@shopping_bp.route("/clear/cart")
def clear_cart():

    session["cart"] = []
    session.modified = True

    return redirect(url_for("shopping.shopping_cart"))


# ==========================================================
# USER ORDERS
# ==========================================================

@shopping_bp.route("/user/orders")
def user_orders():

    return render_template("user_orders.html")

