from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sklearn.linear_model import LinearRegression
from flask_cors import CORS
import joblib

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

# Database setup (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# ------------------- User Model -------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))


# ------------------- Routes -------------------
# Home
@app.route("/")
def index():
    return render_template("login_signup.html")

# Signup
@app.route("/signup", methods=["POST"])
def signup():
    fullname = request.form['fullname']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return "⚠️ Username already exists!"

    new_user = User(fullname=fullname, email=email, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("index"))

# Login
@app.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username, password=password).first()
    if user:
        session['user'] = user.username
        return redirect(url_for("dashboard"))
    else:
        return "❌ Invalid Username or Password"

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

# Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session['user'])
    return redirect(url_for("index"))


# ------------------- Price Prediction -------------------
@app.route("/predict_price", methods=["POST"])
def predict_price():
    data = request.json  # Get data from frontend (AJAX / fetch)
    item = data.get("item", "tomato")
    year = int(data.get("year", 2024))
    month = int(data.get("month", 1))

    # Load dataset
    df = pd.read_csv("data/crop_prices.csv")   # Make sure file exists

    # Filter for the selected crop
    crop_data = df[df["item"].str.lower() == item.lower()]

    if crop_data.empty:
        return jsonify({"error": f"No data for {item}"}), 400

    X = crop_data[["year", "month"]]
    y = crop_data["avg_price"]

    # Train simple model
    model = LinearRegression()
    model.fit(X, y)

    pred = model.predict([[year, month]])[0]

    return jsonify({"item": item, "predicted_price": round(pred, 2)})


# ------------------- Run -------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
