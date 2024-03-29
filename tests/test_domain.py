"""Record Domain."""

import copy
from datetime import datetime

import pytest
from pydantic import ValidationError

from src.domain import Account, Category, Debts, Record, User

from .domain_data import debts_dict, user_data


@pytest.mark.parametrize('user_data', user_data)
def test_not_send_all_data_should_raise_validation_error(
    user_data: dict,
) -> None:
    """Must raise validation Error."""
    # Act
    with pytest.raises(ValidationError) as vex:
        User(
            id_=user_data['id'],
            name=user_data['name'],
            email=user_data['email'],
            password=user_data['password'],
        )

    # Assert
    error = vex.value.errors().pop()
    assert error['msg'] == 'none is not an allowed value'
    assert error['type'] == 'type_error.none.not_allowed'


def test_send_valid_data_should_create_user_domain() -> None:
    """Must create user domain."""
    # Act
    user = User(id_=1, name='test', email='email@email.com', password='123')
    # Assert
    assert isinstance(user, User)
    assert user.dict() == {
        'id_': 1,
        'name': 'test',
        'email': 'email@email.com',
        'password': '123',
    }


def test_debts_domain() -> None:
    """Must create debts domain."""
    # Act
    debts = Debts(**debts_dict)

    # Assert
    assert isinstance(debts, Debts)
    assert debts.dict() == debts_dict


@pytest.mark.parametrize(
    'debts_data',
    [
        'id_',
        'user_id',
        'institution_name',
        'type_',
        'financial_fine',
        'total_fine',
        'priority',
        'installments_payble',
        'installments_value',
        'total_late',
        'max_value_negociation',
        'settled',
    ],
)
def test_some_without_valid_fields_in_debts_should_raise_validation_error_exception(
    debts_data: dict,
) -> None:
    """Must invalid fields show ValidationError."""
    # Arrange
    record_fields = copy.deepcopy(debts_dict)
    record_fields.pop(debts_data)

    # Act
    with pytest.raises(ValidationError) as vex:
        Debts(**record_fields)

    # Assert
    error = vex.value.errors().pop()
    assert error['msg'] == 'field required'
    assert error['type'] == 'value_error.missing'


def test_valid_fields_should_create_category_domain() -> None:
    """Must create category domain."""
    # Act
    category = Category(
        id_=1,
        operation='debit',
        user=1,
    )

    # Assert
    assert isinstance(category, Category)


def test_valid_fields_should_create_account_domain() -> None:
    """Must create account domain."""
    # Act
    _user = User(id_=1, name='test', email='email@email.com', password='123')
    account = Account(
        id_=1,
        user=_user,
    )

    # Assert
    assert isinstance(account, Account)


def test_valid_fields_should_create_record_domain() -> None:
    """Must be create record domain."""
    # Arrange
    now = datetime.now()
    date_time = now.strftime('%m/%d/%Y')

    # Act
    record = Record(
        id_=1,
        user_id=1,
        account_id=1,
        category_id=1,
        type_='debit',
        amount=10.0,
        date=date_time,
        description='one description',
    )
    # Assert
    assert isinstance(record, Record)
