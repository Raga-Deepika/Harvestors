from flask import Flask
from flasgger import Swagger
from entrepreneur.controllers import entrepreneur_blueprint
from apscheduler.schedulers.background import BackgroundScheduler
from entrepreneur.jobs import entrepreneur_ma_jobs, entrepreneur_lawsuits_jobs,entrepreneur_patents_jobs

app = Flask(__name__)
swagger = Swagger(app)
scheduler=BackgroundScheduler(daemon=True)
job1 = scheduler.add_job(entrepreneur_ma_jobs, 'interval', minutes=3)
job2 = scheduler.add_job(entrepreneur_lawsuits_jobs, 'interval', minutes=3)
job3 = scheduler.add_job(entrepreneur_patents_jobs, 'interval', minutes=3)
scheduler.start()


app.register_blueprint(entrepreneur_blueprint, url_prefix='/api/v1/entre')


if __name__ == '__main__':
    app.run(debug=True)
