from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy credentials
VALID_USER = "admin"
VALID_PASS = "admin123"

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == VALID_USER and password == VALID_PASS:
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    return "<h1>Login Successful 🎉</h1>"


if __name__ == "__main__":
    app.run(debug=True)
print("Scammed")