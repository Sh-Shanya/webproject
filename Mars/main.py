from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("db/mars_explorer.db")

    user1 = User()
    user1.surname = "Scott"
    user1.name = "Ridley"
    user1.age = 21
    user1.position = "captain"
    user1.speciality = "research engineer"
    user1.address = "module_1"
    user1.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user1)

    user2 = User()
    user2.surname = "Weir"
    user2.name = "Andy"
    user2.age = 17
    user2.position = "scientist"
    user2.speciality = "chief scientist"
    user2.address = "module_2"
    user2.email = "weir_andy@mars.org"
    db_sess.add(user2)

    user3 = User()
    user3.surname = "Bean"
    user3.name = "Sean"
    user3.age = 24
    user3.position = "ingeneer"
    user3.speciality = "chief ingeneer"
    user3.address = "module_1"
    user3.email = "bean_sean@mars.org"
    db_sess.add(user3)

    user4 = User()
    user4.surname = "Kapoor"
    user4.name = "Venkat"
    user4.age = 15
    user4.position = "ingeneer's support"
    user4.speciality = "middle scientist"
    user4.address = "module_2"
    user4.email = "kapoor_venkat@mars.org"
    db_sess.add(user4)

    db_sess.commit()


if __name__ == "__main__":
    main()
