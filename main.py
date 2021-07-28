from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/equipment-finance")
def equipment():
    return render_template("equipment.html")

@app.route("/vehicle-finance")
def vehicle():
    return render_template("vehicle.html")

@app.route("/leaders")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    app.run(debug=True)