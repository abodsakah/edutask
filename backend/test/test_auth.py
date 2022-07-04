import os
from unittest import mock
import pytest

from src.controllers.usercontroller import UserController
from src.util.daos import getDao


def test_case_1():
    """
    Email format valid: True
    Email: jane.doe@mail.com
    Amount users with same email adress: 1
    Connected to database: True
    """
    userObj = [{'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}]
    mocked = mock.MagicMock()
    mocked.find.return_value = userObj
    controller = UserController(mocked)

    # Loging in with a unique, valid email address that is associated to a user
    # Should return: user object
    # Test case id: TC1
    user = controller.get_user_by_email("jane.doe@mail.com")
    assert user['firstName'] == 'Jane'

def test_case_2(capfd):
    """
    Email format valid: True
    Email: jane.doe@mail.com
    Amount users with same email adress: 2
    Connected to database: True
    """

    out, err = capfd.readouterr()

    userObj = [{'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}, {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}]
    mocked = mock.MagicMock()
    mocked.find.return_value = userObj
    controller = UserController(mocked)


    # Loging in with a none unique, valid email address that is associated to multiple users
    # Should return: IndexError
    # Test case id: TC2
    user = controller.get_user_by_email("jane.doe@mail.com")

    assert out == 'Error: more than one user found with mail jane.doe@mail.com\n'

def test_case_3():
    """
    Email format valid: True
    Email: helloworld@mail.com
    Amount users with same email adress: 0
    Connected to database: True
    """

    userObj = []
    mocked = mock.MagicMock()
    mocked.find.return_value = userObj
    controller = UserController(mocked)

    # valid email address that is not associated to a user
    # Should return: None
    # Test case id: TC3
    user = controller.get_user_by_email("sfdwefwefew@fewfewf.com")
    print(user)
    assert user is None


def test_case_4():
    """
    Email format valid: False
    Email: jane.doe
    Amount users with same email adress: 0
    Connected to database: True
    """

    userObj = [{'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}]
    mocked = mock.MagicMock()
    mocked.find.return_value = userObj
    controller = UserController(mocked)

    # Invalid format email address
    # Should return: ValueError
    # Test case id: TC4
    with pytest.raises(ValueError):
        user = controller.get_user_by_email("jane.doe")

def test_case_5():
    """
    Email format valid: False
    Email: mail.com
    Amount users with same email adress: 0
    Connected to database: True
    """

    userObj = [{'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}]
    mocked = mock.MagicMock()
    mocked.find.return_value = userObj
    controller = UserController(mocked)

    # Invalid format email address
    # Should return: ValueError
    # Test case id: TC5
    with pytest.raises(ValueError):
        user = controller.get_user_by_email("mail.com")


def test_case_6():
    """
    Email format valid: False
    Email: jane.doe@mail
    Amount users with same email adress: 0
    Connected to database: True
    """

    userObj = [{'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}]
    mocked = mock.MagicMock()
    mocked.find.return_value = userObj
    controller = UserController(mocked)

    #Invalid format email address
    #Should return: ValueError
    #Test case id: TC7
    with pytest.raises(ValueError):
        user = controller.get_user_by_email("jane.doe@mail")

def test_case_7():
    """
    Email format valid: False
    Email: @mail.com
    Amount users with same email adress: 0
    Connected to database: True
    """

    userObj = [{'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}]
    mocked = mock.MagicMock()
    mocked.find.return_value = userObj
    controller = UserController(mocked)

    #Invalid format email address
    #Should return: ValueError
    #Test case id: TC8
    with pytest.raises(ValueError):
        user = controller.get_user_by_email("@mail.com")

def test_case_8():
    """
    Email format valid: False
    Email: jane.doe@
    Amount users with same email adress: 0
    Connected to database: True
    """

    userObj = [{'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}]
    mocked = mock.MagicMock()
    mocked.find.return_value = userObj
    controller = UserController(mocked)

    #Invalid format email address
    #Should return: ValueError
    #Test case id: TC9
    with pytest.raises(ValueError):
        user = controller.get_user_by_email("jane.doe@")

def test_case_9():
    """
    Email format valid: False
    Email: jane.doe
    Amount users with same email adress: 1
    Connected to database: False
    """

    #Mock the database connection and raise an Exception when trying to connect to it
    #Should return: Exception
    #Test case id: TC6
    with pytest.raises(Exception):
        user = controller.get_user_by_email("jane.doe@mail.com")