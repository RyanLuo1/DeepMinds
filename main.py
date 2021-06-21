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
        # print(ticker_value)

        df = picker_select(ticker_value)

        # creating a list for each column in the csv format
        date_list = []
        for data in df["Date"]:
            date_list.append(data)

        open_list = []
        for data in df["Open"]:
            open_list.append(data)

        high_list = []
        for data in df["High"]:
            high_list.append(data)

        close_list = []
        for data in df["Close"]:
            close_list.append(data)

        adj_close_list = []
        for data in df["Adj Close"]:
            adj_close_list.append(data)

        volume_list = []
        for data in df["Volume"]:
            volume_list.append(data)
        # end of creating a list for each column

        # creating dictionaries from specific items for each list previously created
        every_info = []
        b = 0
        for i in date_list:
            new_dict = {
                "Date":date_list[b],
                "Open":open_list[b],
                "High":high_list[b],
                "Close":close_list[b],
                "Adj Close":adj_close_list[b],
                "Volume":volume_list[b]
            }
            every_info.append(new_dict)
            b = b + 1
        print(every_info)

        return render_template("picker.html", every_info=every_info)
    return render_template("picker.html")


from picker.app import picker_bp

app.register_blueprint(picker_bp, url_prefix='/picker')

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port='5000', host='127.0.0.1')
