from app import app
from flask import Flask, render_template

@app.route('/')
def home():
    return render_template("home.html")






if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='5000', host='127.0.0.1')