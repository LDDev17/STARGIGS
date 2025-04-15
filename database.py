from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): # Creating our Base model that will be inherited by all other models
    pass

db = SQLAlchemy(model_class=Base) # Instantiating our db