from pydantic.dataclasses import dataclass
from typing import Optional
from  decimal import Decimal
from datetime import datetime
from pydantic import BaseModel
from enum import Enum

class Record(BaseModel):
    id: int
    user: int
    account: int
    category: int
    type: str
    amount: Decimal
    date: datetime
    description: str
    tags: Optional[list[str]]
    note: Optional[str]

class Debts(BaseModel):
    id: int
    institution_name: str
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
    email: str
    password: str

@dataclass
class Account:
    id: int
    user: User
    description: str

@dataclass
class Category:
    id: int
    user: int
    description: str
    Operation: Enum
