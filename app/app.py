from flask import Flask, redirect, url_for, request
from flask_restful import Api, Resource

import configuration

from health.status import Working

# instantiate app
app = Flask(__name__)
api = Api(app)

# base urls for service pulled from package.json
url_base = configuration.SERVICE_URL_BASE

# endpoints

api.add_resource(Working, url_base + "working/")

# serve up app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)