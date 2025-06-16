from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Title", "Description", "Button text", "static/images/card1.png"),
        ("Title", "Description", "Button text", "static/images/card2.png"),
        ("Title", "Description", "Button text", "static/images/card3.png"),
        ("Title", "Description", "Button text", "static/images/card4.png"),
    )
    return render_template("index.html", cards=card_data), 200


@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

if __name__ == '__main__':
    app.run(debug=True)