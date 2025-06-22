from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Title", "Description", "Button text", "static/images/CARDONE.png"),
        ("Title", "Description", "Button text", "static/images/CARDTWO.png"),
        ("Title", "Description", "Button text", "static/images/CARDTHREE.png"),
        ("Title", "Description", "Button text", "static/images/CARDFOUR.png"),
    )
    return render_template("index.html", cards=card_data), 200


@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200


@app.route('/RAC.html')
def RAC():
    return render_template("RAC.html"), 200



if __name__ == '__main__':
    app.run(debug=True)