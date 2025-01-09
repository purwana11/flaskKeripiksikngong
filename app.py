from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route for the About page
@app.route("/about")
def about():
    return render_template("about.html")

# Route for the Contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Route for the Menu page
@app.route("/menu")
def menu():
    return render_template("menu.html")

# Route for the Testimonial page
@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")

# Route for the Service page
@app.route("/service")
def service():
    return render_template("service.html")

# Route for the Reservation page
@app.route("/reservation")
def reservation():
    return render_template("reservation.html")

if __name__ == "__main__":
    app.run(debug=True)
