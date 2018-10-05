import os
import config  # noqa:E401
from flask import Flask

app = Flask(__name__)

if os.environ['ENV'] == 'production':
    app.config.from_object('config.settings.Prod')
else:
    app.config.from_object('config.settings.Dev')


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


print(app.config)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
