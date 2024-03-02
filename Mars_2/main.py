from flask import Flask
from data import db_session
from data.jobs import Jobs
import datetime


app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("mars_explorer.db")
    db_sess = db_session.create_session()

    job1 = Jobs()
    job1.team_leader = 1
    job1.job = "deployment of residential modules 1 and 2"
    job1.work_size = 15
    job1.collaborators = "2, 3"
    job1.start_date = datetime.datetime.now()
    job1.is_finished = False
    db_sess.add(job1)

    db_sess.commit()


if __name__ == "__main__":
    main()
