import email
import pytest
from src.util.dao import DAO
from src.util.daos import getDao

dao = DAO(collection_name='user')

def test_case_1():
    # Object containing all required properties and complies with bson type constraints
    # Should return: the newly created object
    # Test case id: TC1
    data = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}
    user = dao.create(data)
    assert user['firstName'] == 'Jane'
    dao.delete(user['_id']['$oid'])

def test_case_2():
    
    # Object missing required property
    # Should raise: WriteError
    # Test case id: TC2
    with pytest.raises(Exception):
        data = {'firstName': 'Jane', 'lastName': 'Doe'}
        user = dao.create(data)

def test_case_3():

    # Object containing property with invalid bson type
    # Should raise: WriteError
    # Test case id: TC3
    with pytest.raises(Exception):
        data = {'firstName': 'Jane', 'lastName': 'Doe', 'email': {'hello': 'world'}}
        user = dao.create(data)