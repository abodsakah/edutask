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

    # Test to find a user with the same email
    user = dao.find({'email': 'jane.doe@mail.com'})
    assert user[0]['firstName'] == 'Jane' and user[0]['email'] == 'jane.doe@mail.com'

    # Test to find a user with invalid email
    user = dao.find({'email': 'janel.doe@mail'})
    assert user == []

    # Find user with valid id
    userId = dao.find({'email': 'jane.doe@mail.com'})
    user = dao.findOne(userId[0]['_id']['$oid'])
    assert user['firstName'] == 'Jane' and user['email'] == 'jane.doe@mail.com'
      
    # Find user with invalid id
    userId = '123132313'
    with pytest.raises(Exception):
        dao.findOne(userId)

    # Test updaing user information
    user = dao.find({'email': 'jane.doe@mail.com'})
    userId = user[0]['_id']['$oid']
    newUser = dao.update(userId, {'$set': {'firstName': 'Janel'}})
    assert newUser == True

    # Test deleting user
    user = dao.find({'email': 'jane.doe@mail.com'})
    userId = user[0]['_id']['$oid']
    user = dao.delete(userId)
    print(user)
    assert user == True



