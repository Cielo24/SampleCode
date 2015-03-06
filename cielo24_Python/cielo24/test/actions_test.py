# encoding: utf-8
from unittest import TestCase
from cielo24.actions import Actions
import config as config


class ActionsTest(TestCase):
    actions = Actions(config.server_url)
    api_token = None
    secure_key = None

    def setUp(self):
        if self.api_token is None:
            self.api_token = self.actions.login(config.username, config.password, None, True)
        if self.secure_key is None:
            self.secure_key = self.actions.generate_api_key(self.api_token, config.username, False)