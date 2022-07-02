from datetime import datetime
import email
import pytest
from src.util.dao import DAO
from src.util.daos import getDao
from bson import json_util
from bson.objectid import ObjectId

dao = DAO(collection_name='task')

taskData = {'title': 'hello', 'description': '(add a description here)', 'todos': [], 'startdate': datetime(2022, 7, 2, 11, 24, 36, 467306), 'categories': [], 'video': ObjectId('62c00ed43ef84fb08f8dd096')}

task = dao.create(taskData)

dao = DAO(collection_name='user')

def test_case_1():
    """
        Data complies with validator: True
        Data complies with bson validator: True
        uniques are unique: True
    """

    # Object containing all required properties and complies with bson type constraints
    # Should return: the newly created object
    # Test case id: TC1
    data = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com', 'tasks': [ObjectId(task['_id']["$oid"])]}
    print(data)
    user = dao.create(data)
    assert user['firstName'] == 'Jane'
    dao.delete(user['_id']['$oid'])

def test_case_2():
    """
        Data complies with validator: False
        Data complies with bson validator: True
        uniques are unique: True
    """

    # Object missing required property
    # Should raise: WriteError
    # Test case id: TC2
    with pytest.raises(Exception):
        data = {'firstName': 'Jane', 'lastName': 'Doe'}
        user = dao.create(data)

def test_case_3():
    """
        Data complies with validator: True
        Data complies with bson validator: False
        uniques are unique: True
    """

    # Object containing property with invalid bson type
    # Should raise: WriteError
    # Test case id: TC3
    with pytest.raises(Exception):
        data = {'firstName': 'Jane', 'lastName': 'Doe', 'email': {'hello': 'world'}}
        user = dao.create(data)

def test_case_4():
    """
        Data complies with validator: True
        Data complies with bson validator: True
        uniques are unique: False
    """

    # Object containing property with invalid bson type
    # Should raise: WriteError
    # Test case id: TC4
    with pytest.raises(Exception):
        data = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com', 'tasks': [ObjectId(task['_id']["$oid"])]}
        user = dao.create(data)
        dao.delete(user['_id']['$oid'])

    dao = DAO(collection_name='task')
    dao.delete(task['_id']["$oid"])