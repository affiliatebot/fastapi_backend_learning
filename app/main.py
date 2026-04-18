from fastapi import FastAPI
from routes import user
from database.db import engine, Base
app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(user.router)

