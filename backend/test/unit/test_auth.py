import pytest
import unittest.mock as mock

from src.util.helpers import hasAttribute, ValidationHelper
from src.controllers.usercontroller import UserController
from src.util.daos import getDao

controller = UserController(getDao(collection_name='user'))

def test_get_user_info_by_mail(capsys):
    """
    test getting the user by the email
    """

    captured = capsys.readouterr()

    data = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@mail.com'}
    controller.create(data)

    # Loging in with a unique, valid email address that is associated to a user
    # Should return: user object
    user = controller.get_user_by_email("jane.doe@mail.com")
    assert user['firstName'] == 'Jane'

    # valid email address that is not associated to a user
    # Should return: None
    user = controller.get_user_by_email("jane@mail.com")
    assert user is None

    # Invalid format email address
    # Should return: ValueError
    with pytest.raises(ValueError):
        user = controller.get_user_by_email("jane.doe@mail")


    data = {'firstName': 'Janel', 'lastName': 'Doel', 'email': 'jane.doe@mail.com'}
    controller.create(data)

    # Loging in with a none unique, valid email address that is associated to multiple users
    # Should return: IndexError
    user = controller.get_user_by_email("jane.doe@mail.com")
    assert 'Error: more than one user found with mail ' in captured.out
