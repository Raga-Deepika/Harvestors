from flask import Flask
from flasgger import Swagger
from entrepreneur.controllers import entrepreneur_blueprint
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from entrepreneur.controllers import entrepreneur


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'entrepreneur:entrepreneur',
            'args': None,
            'trigger': 'interval',
            'minutes': 1
        }
    ]

    SCHEDULER_JOBSTORES = {
        'default': MongoDBJobStore()
    }

    SCHEDULER_EXECUTORS = {
        'default': ThreadPoolExecutor(10)
    }

    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }

    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
swagger = Swagger(app)
app.config.from_object(Config())
scheduler = BackgroundScheduler()
scheduler.start()
job = scheduler.add_job(entrepreneur, 'interval', minutes=2)

app.register_blueprint(entrepreneur_blueprint, url_prefix='/api/v1/entre')


if __name__ == '__main__':
    app.run(debug=True)
