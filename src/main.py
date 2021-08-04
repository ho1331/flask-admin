from flask_restful import Api

from src.app import app
from src.resources.healthcheck import HealthCheck

# API
api = Api(app)
api.add_resource(HealthCheck, "/healthcheck/")
