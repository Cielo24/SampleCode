# encoding: utf-8
from unittest import TestCase
from cielo24.actions import Actions


class ActionsTest(TestCase):
    actions = Actions("http://sandbox-dev.cielo24.com")
    username = "api_test"
    password = "api_test"
    new_password = "api_test_new"
    api_token = None
    secure_key = None

    def setUp(self):
        if self.api_token is None:
            self.api_token = self.actions.login(self.username, self.password, None, True)
        if self.secure_key is None:
            self.secure_key = self.actions.generate_api_key(self.api_token, self.username, False)