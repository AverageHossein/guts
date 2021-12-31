from core.app import create_app 
from core.config import Base

app = create_app(Base)
# app.run()