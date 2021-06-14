from app import app
from flask import Flask, render_template, request
from picker.picker import *


@app.route('/')
def home():
    return render_template("home.html")


# We used a ["POST"] method to create user input and it needs to be routed through main.py
# created the variable ticker_value
@app.route('/picker', methods=["POST"])
def picker():
    if request.form:
        ticker_value = request.form.get("ticker")
        print(ticker_value)
        return render_template("picker.html", df=picker_select(ticker_value))
    return render_template("picker.html")


from picker.app import picker_bp

app.register_blueprint(picker_bp, url_prefix='/picker')

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port='5000', host='127.0.0.1')
