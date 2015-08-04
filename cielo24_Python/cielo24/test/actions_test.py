# encoding: utf-8
import logging
from unittest import TestCase
from cielo24.actions import Actions
from cielo24.web_utils import WebUtils
import config as config


class ActionsTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # Make WebUtils logger output to stdout
        cls.console_handler = logging.StreamHandler()
        cls.old_level = WebUtils.LOGGER.level
        WebUtils.LOGGER.level = logging.DEBUG
        WebUtils.LOGGER.addHandler(cls.console_handler)

    @classmethod
    def tearDownClass(cls):
        # Restore WebUtils logger settings
        WebUtils.LOGGER.level = cls.old_level
        WebUtils.LOGGER.removeHandler(cls.console_handler)

    def setUp(self):
        self.actions = Actions(config.server_url)
        # Start with a fresh session each time
        self.api_token = self.actions.login(config.username, config.password, None, True)
        self.secure_key = self.actions.generate_api_key(self.api_token, config.username, False)
