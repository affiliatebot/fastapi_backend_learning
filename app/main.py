from fastapi import FastAPI
from app.routes import user
from app.database.db import engine, Base
app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(user.router)

