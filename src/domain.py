from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr


class Record(BaseModel):
    id: int
    user_id: int
    account_id: int
    category_id: int
    type: str
    amount: Decimal
    date: datetime
    description: str
    tags: Optional[list[str]]
    note: Optional[str]

class Debts(BaseModel):
    id: int
    institution_name: str
    user_id: int
    type: str
    financial_fine: int
    total_fine: int
    priority: str
    installments_payble: int
    installments_value: int
    total_late: int
    max_value_negociation: int
    settled: bool

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str

class Account(BaseModel):
    id: int
    description: Optional[str]
    user: User

class Category(BaseModel):
    id: int
    description: Optional[str]
    Operation: Enum
    user: int
