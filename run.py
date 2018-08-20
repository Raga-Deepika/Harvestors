from flask import Flask
from flasgger import Swagger
from entrepreneur.controllers import entrepreneur_blueprint
from entrepreneur.jobs import entre_jobs
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)
swagger = Swagger(app)
scheduler = BackgroundScheduler()
job = scheduler.add_job(entre_jobs, 'interval', seconds=10, max_instances=3)
scheduler.start()


app.register_blueprint(entrepreneur_blueprint, url_prefix='/api/v1/entre')

if __name__ == '__main__':
    app.run(debug=True)