from fastapi import APIRouter

from app.schemas import PaymentCreate
from app.dependencies import db_dep, sec_dep

router = APIRouter(prefix="/payment", tags=["Payment"])


@router.post("/create-payment")
def create_payment(data: PaymentCreate, merchant: sec_dep, db: db_dep):
    pass