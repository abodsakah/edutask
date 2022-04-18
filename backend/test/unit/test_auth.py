import pytest
import unittest.mock as mock

from src.util.helpers import hasAttribute, ValidationHelper
from src.controllers.usercontroller import UserController
from src.util.daos import getDao

controller = UserController(getDao(collection_name='user'))

# # tests for the hasAttribute method
# @pytest.mark.demo
# @pytest.mark.parametrize('obj, expected', [({'name': 'Jane'}, True), ({'email': 'jane.doe@gmail.com'}, False), (None, False)])
# def test_hasAttribute_true(obj, expected):
#     assert hasAttribute(obj, 'name') == expected

# # tests for the validateAge method
# @pytest.fixture
# def sut(age: int):
#     mockedusercontroller = mock.MagicMock()
#     mockedusercontroller.get.return_value = {'age': age}
#     mockedsut = ValidationHelper(usercontroller=mockedusercontroller)
#     return mockedsut

# @pytest.mark.demo
# @pytest.mark.parametrize('age, expected', [(-1, 'invalid'), (0, 'underaged'), (1, 'underaged'), (17, 'underaged'), (18, 'valid'), (19, 'valid'), (119, 'valid'), (120, 'valid'), (121, 'invalid')])
# def test_validateAge(sut, expected):
#     validationresult = sut.validateAge(userid=None)
#     assert validationresult == expected

def test_create_user():
    """
    Test the create_user method
    """

    # Creating a user with valid data
    data = {'firstName': 'Janel', 'lastName': 'Doe', 'email': 'janel.doe@mail.com'}
    user = controller.create(data)
    assert user['firstName'] == 'Janel'

    # Creating a user with a invalid email
    data = {'firstName': 'Janel', 'lastName': 'Doe', 'email': 'janel.doe@mail'}
    user = controller.create(data)
    assert user is None

    # Creating a user with empty fields show return list index out of range error
    data = {'firstName': '', 'lastName': '', 'email': ''}
    user = controller.create(data)
    assert user is None

    # Try to register a user with an existing email
    data = {'firstName': 'Janel', 'lastName': 'Doe', 'email': 'janel.doe@mail.com'}
    user = controller.create(data)
    assert user is None


def test_get_user_info_by_mail():
    """
    test getting the user by the email
    """
    # Try to login with a valid email adress
    user = controller.get_user_by_email('janel.doe@mail.com')
    assert user['firstName'] == 'Janel'

    # Try to login with a invalid email adress
    with pytest.raises(IndexError):
        controller.get_user_by_email('mail@mail.com')

    # Try to send a invalid email format
    with pytest.raises(ValueError):
        controller.get_user_by_email('mail')
        