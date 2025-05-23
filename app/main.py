from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import Merchant
from app.admin.settings import admin
from app.routers.auth import router as auth_router

app = FastAPI()

admin.mount_to(app=app)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/merchants/")
async def get_merchant(db: Session = Depends(get_db)):
    return db.query(Merchant).all()

app.include_router(auth_router)
