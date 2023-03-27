from flask import Flask
from data import db_session
from data.users import Jobs
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def write_to_jobs_db(info: list):

    job = Jobs()
    job.team_leader = info[0]
    job.job = info[1]
    job.work_size = info[2]
    job.collaborators = info[3]
    job.start_date = info[4]
    job.is_finished = info[5]

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


def main():
    db_session.global_init("server/SQLAlchemy/First Job/db/blogs.db")
    now_dt = datetime.datetime.now()
    info = [1, "deployment of residential modules 1 and 2",
            15, "2, 3", now_dt, True]

    write_to_jobs_db(info=info)

    app.run()


if __name__ == '__main__':
    main()
