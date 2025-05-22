from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

import base64
from typing import Annotated

from app.database import SessionLocal
from app.models import Merchant

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dep = Annotated[Session, Depends(get_db)]

security = HTTPBasic()
sec_dep = Annotated[HTTPBasicCredentials, Depends(security)]

def get_merchant(credentials: sec_dep, db: db_dep):
    merchant = db.query(Merchant).filter(api_key=credentials.username).first()

    if not merchant:
        raise HTTPException(status_code=403, detail="Invalid API key")

    return merchant