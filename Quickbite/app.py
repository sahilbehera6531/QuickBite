from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

users = {}

food_items = [
    {
        "id": 1,
        "name": "Pizza",
        "price": 250,
        "image": "https://images.unsplash.com/photo-1594007654729-407eedc4be65"
    },
    {
        "id": 2,
        "name": "Burger",
        "price": 120,
        "image": "https://images.unsplash.com/photo-1550547660-d9450f859349"
    },
    {
        "id": 3,
        "name": "Pasta",
        "price": 180,
        "image": "https://images.unsplash.com/photo-1525755662778-989d0524087e"
    },
    {
        "id": 4,
        "name": "Sandwich",
        "price": 90,
        "image": "https://images.unsplash.com/photo-1567234669003-dce7a7a88821"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            message = "User already exists!"

        else:
            users[username] = password
            message = "Signup successful! Please login."

    return render_template("signup.html", message=message)


@app.route("/login", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            return redirect(url_for("menu"))

        else:
            message = "Invalid username or password"

    return render_template("login.html", message=message)


@app.route("/menu")
def menu():
    return render_template("menu.html", foods=food_items)


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/api/foods")
def get_foods():
    return jsonify(food_items)


if __name__ == "__main__":
    app.run(debug=True)