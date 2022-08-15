from src.domain import (
    User,
    Category,
    Debts,
    Record,
    Account
)


def test_user_domain():
    user = User(
        id=1,
        name='test',
        email='email@email.com',
        password='123'
    )
    assert user.dict() == dict(id=1, name='test', email='email@email.com', password='123')


def test_debts_domain():
    record = Debts(
        id=1,
        institution_name='institution test',
        type='type',
        financial_fine=1,
        total_fine=1,
        priority='high',
        installments_payble=1,
        installments_value=1,
        total_late=1,
        max_value_negociation=1,
        settled=True,
    )
    record_dict = dict(
        id=1,
        institution_name='institution test',
        type='type',
        financial_fine=1,
        total_fine=1,
        priority='high',
        installments_payble=1,
        installments_value=1,
        total_late=1,
        max_value_negociation=1,
        settled=True,
    )
    assert record.dict() == record_dict

