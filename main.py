from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Title", "Description", "Button text", "static/images/logo.png"),
        ("Title", "Description", "Button text", "static/images/logo.png"),
        ("Title", "Description", "Button text", "static/images/logo.png"),
        ("Title", "Description", "Button text", "static/images/logo.png"),
    )
    return render_template("index.html", cards=card_data), 200


if __name__ == '__main__':
    app.run(debug=True)