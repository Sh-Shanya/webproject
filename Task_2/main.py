from flask import Flask

app = Flask(__name__)


@app.route("/image_mars")
def image_mars():
    return """
        <head>
            <h1>Жди нас, Марс!</h1>
            <img src="/static/img/mars.jpg">
            <title>Привет, Марс!</title>
        </head>

        <body>
            </br>Вот она какая, красная планета.
        </body>
"""
