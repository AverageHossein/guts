from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

api = Api(None)
db = SQLAlchemy(None)
migrate = Migrate()