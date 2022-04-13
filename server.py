from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)
app.secret_key = "as;diujasdnbvpiausdfhva"

@app.route("/")
def main():
    users = User.get_all()
    return render_template("read.html", users=users)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    new_user_data = {
        "first_name" : request.form["firstname"],
        "last_name" : request.form["lastname"],
        "email" : request.form["email"]
    }
    User.create_new(new_user_data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)