# encoding: utf-8
from actions_test import ActionsTest


class AccessTest(ActionsTest):

    # Username, password, no headers
    def test_login_password_no_headers(self):
        self.api_token = self.actions.login(self.username, self.password)
        self.assertEqual(32, len(self.api_token))

    # Username, password, headers
    def test_login_password_headers(self):
        self.api_token = self.actions.login(self.username, self.password, None, True)
        self.assertEqual(32, len(self.api_token))

    # Username, secure key, no headers
    def test_login_securekey_no_headers(self):
        self.api_token = self.actions.login(self.username, None, self.secure_key)
        self.assertEqual(32, len(self.api_token))

    # Username, secure key, headers
    def test_login_securekey_headers(self):
        self.api_token = self.actions.login(self.username, None, self.secure_key, True)
        self.assertEqual(32, len(self.api_token))

    # Logout
    def test_logout(self):
        self.actions.logout(self.api_token)
        self.api_token = None

    # Generate API key with force_new option
    def test_generate_api_key_force_new(self):
        self.secure_key = self.actions.generate_api_key(self.api_token, self.username, False)
        self.assertEqual(32, len(self.secure_key))

    # Generate API key with force_new option
    def test_generate_api_key_not_force_new(self):
        self.secure_key = self.actions.generate_api_key(self.api_token, self.username, True)
        self.assertEqual(32, len(self.secure_key))

    # Remove API key
    def test_remove_api_key(self):
        self.actions.remove_api_key(self.api_token, self.secure_key)
        self.secure_key = None

    # Update password
    def test_update_password(self):
        self.actions.update_password(self.api_token, self.new_password)
        self.actions.update_password(self.api_token, self.password)
