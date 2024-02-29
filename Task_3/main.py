from flask import Flask, url_for

app = Flask(__name__)


@app.route("/promotion_image")
def promotion_image():
    return """
        <head>
            <title>Колонизация</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
            <link rel="stylesheet" href="static/css/style.css"/>
        </head>
        <body>
            <h1 class="red-title">Жди нас, Марс!</h1>
            <img src="/static/img/mars.jpg">
            <div class="alert alert-secondary" role="alert">Человечество вырастает из детства.</div>
            <div class="alert alert-success" role="alert">Человечеству мала одна планета.</div>
            <div class="alert alert-secondary" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
            <div class="alert alert-warning" role="alert">И начнем с Марса!</div>
            <div class="alert alert-danger" role="alert">Присоединяйся!</div>
        </body>
"""
