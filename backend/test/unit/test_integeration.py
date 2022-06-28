import email
import pytest
from src.util.dao import DAO
from src.util.daos import getDao

def test_create():
    """
    test DAO.create()
    """

    dao = DAO(collection_name='user')

    # Object containing all required properties and complies with bson type constraints
    # Should return: the newly created object
    data = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}
    user = dao.create(data)
    assert user['firstName'] == 'Jane'

    # Object missing required property
    # Should raise: WriteError
    with pytest.raises(Exception):
        data = {'firstName': 'Jane', 'lastName': 'Doe'}
        user = dao.create(data)

    # Object containing property with invalid bson type
    # Should raise: WriteError
    with pytest.raises(Exception):
        data = {'firstName': 'Jane', 'lastName': 'Doe', 'email': {'hello': 'world'}}
        user = dao.create(data)



