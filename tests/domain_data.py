"""Dummy domain."""

user_data = [
    {
        'id': None,
        'name': 'John Doe',
        'email': 'email@email.com',
        'password': '123',
    },
    {'id': 1, 'name': None, 'email': 'email@email.com', 'password': '123'},
    {'id': 1, 'name': 'John Doe', 'email': None, 'password': '123'},
    {
        'id': 1,
        'name': 'John Doe',
        'email': 'email@email.com',
        'password': None,
    },
]

debts_dict = {
    'id_': 1,
    'user_id': 1,
    'institution_name': 'institution test',
    'type_': 'type',
    'financial_fine': 1,
    'total_fine': 1,
    'priority': 'high',
    'installments_payble': 1,
    'installments_value': 1,
    'total_late': 1,
    'max_value_negociation': 1,
    'settled': True,
}
