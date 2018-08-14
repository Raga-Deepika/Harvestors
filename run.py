from flask import Flask
from flasgger import Swagger
from entrepreneur.controllers import entrepreneur_blueprint
from entrepreneur.controllers import entrepreneur


app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(entrepreneur_blueprint, url_prefix='/api/v1/entre')


if __name__ == '__main__':
    app.run(debug=True)
