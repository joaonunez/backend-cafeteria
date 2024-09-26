# extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Inicialización de extensiones
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
