import pytest
from pydantic import ValidationError

from src.domain import Account, Category, Debts, Record, User

from .domain_data import record_dict, user_data


@pytest.mark.parametrize("user_data", user_data)
def test_not_send_all_data_should_raise_validation_error(user_data) -> None:
    with pytest.raises(ValidationError) as validation_err:
        User(
            id=user_data["id"],
            name=user_data["name"],
            email=user_data["email"],
            password=user_data["password"]
        )
    error = validation_err.value.errors().pop()
    assert error['msg'] == 'none is not an allowed value'
    assert error['type'] == 'type_error.none.not_allowed'


def test_send_valid_data_should_create_user_domain() -> None:
    # Act
    user = User(
        id=1,
        name='test',
        email='email@email.com',
        password='123'
    )
    # Assert
    assert isinstance(user, User)
    assert user.dict() == dict(id=1, name='test', email='email@email.com', password='123')


def test_debts_domain():
    record = Debts(
        id=1,
        user_id=1,
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


def test_category_domain():
    pass


def test_account_domain():
    pass


def test_record_domain():
    pass
