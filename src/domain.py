"""Domain schemas."""
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, EmailStr


class Record(BaseModel):
    """Expense recording template."""

    id_: int
    user_id: int
    account_id: int
    category_id: int
    type_: str
    amount: Decimal
    date: str
    description: str
    tags: list[str] | None
    note: str | None


class Debts(BaseModel):
    """Representation of a debt."""

    id_: int
    institution_name: str
    user_id: int
    type_: str
    financial_fine: int
    total_fine: int
    priority: str
    installments_payble: int
    installments_value: int
    total_late: int
    max_value_negociation: int
    settled: bool


class User(BaseModel):
    """User class."""

    id_: int
    name: str
    email: EmailStr
    password: str


class Account(BaseModel):
    """Kind of account."""

    id_: int
    description: str | None
    user: User


class Category(BaseModel):
    """Category of an expense."""

    id_: int
    description: str | None
    operation: str
    user: int
