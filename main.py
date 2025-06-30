from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Fantasy", "A type of genre", "Explore", "static/images/CARDONE.png"),
        ("Horror", "A type of genre", "Explore", "static/images/CARDTWO.png"),
        ("Sci-Fi", "A type of genre", "Explore", "static/images/CARDTHREE.png"),
        ("Historic", "A type of genre", "Explore", "static/images/CARDFOUR.png"),
    )
    return render_template("index.html", cards=card_data), 200


@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200


@app.route('/RAC.html')
def RAC():
    return render_template("RAC.html"), 200


@app.route('/Home.html')
def Home():
    return render_template("Home.html"), 200


@app.route('/TTHP.html')
def TTHP():
    return render_template("TTHP.html"), 200

@app.route('/WG.html')
def WG():
    return render_template("WG.html"), 200

if __name__ == '__main__':
    app.run(debug=True)