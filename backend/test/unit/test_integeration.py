import email
import pytest

from src.util.dao import DAO
from src.util.daos import getDao

def test_create():
    """
    test creating a user
    """

    dao = DAO(collection_name='user')
    
    # Test with correct parameters should return a user object
    data = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}
    user = dao.create(data)
    assert user['firstName'] == 'Jane'

    # Test with wrong key name should return WriteError
    data = {'first_name': 'Jane', 'last_name': 'Doe', 'email': 'jane.doe@mail.com'}
    # should raise an error WriteError
    with pytest.raises(Exception):
        dao.create(data)

    # Test with wrong values
    data = {'firstName': 123, 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}
    with pytest.raises(Exception):
        dao.create(data)




