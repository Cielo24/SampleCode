# encoding: utf-8
from actions_test import ActionsTest
from cielo24.actions import Actions
from cielo24.web_utils import WebError
from cielo24.enums import ErrorType
import config as config


class SequentialTest(ActionsTest):

    # Called before every test method runs. Can be used to set up fixture information.
    def setUp(self):
        self.actions = Actions(config.server_url)
        # Do nothing else - we want to be able to control when we login/logout etc.

    def test_sequence(self):
        # Login, generate API key, logout
        self.api_token = self.actions.login(config.username, config.password)
        self.secure_key = self.actions.generate_api_key(self.api_token, config.username, True)
        self.actions.logout(self.api_token)
        self.api_token = None

        # Login using API key
        self.api_token = self.actions.login(config.username, None, self.secure_key)

        # Create a job using a media URL
        self.job_id = self.actions.create_job(self.api_token, 'Python_test')['JobId']
        self.actions.add_media_to_job_url(self.api_token, self.job_id, config.sample_video_url)

        # Assert JobList and JobInfo data
        job_list = self.actions.get_job_list(self.api_token)
        self.assertTrue(self.contains_job(self.job_id, job_list), 'JobId not found in JobList')
        job = self.actions.get_job_info(self.api_token, self.job_id)
        self.assertEqual(self.job_id, job['JobId'], 'Wrong JobId found in JobInfo')

        # Logout
        self.actions.logout(self.api_token)
        self.api_token = None

        # Login/logout/change password
        self.api_token = self.actions.login(config.username, config.password)
        self.actions.update_password(self.api_token, config.new_password)
        self.actions.logout(self.api_token)
        self.api_token = None

        # Change password back
        self.api_token = self.actions.login(config.username, config.new_password)
        self.actions.update_password(self.api_token, config.password)
        self.actions.logout(self.api_token)
        self.api_token = None

        # Login using API key
        self.api_token = self.actions.login(config.username, None, self.secure_key)

        # Delete job and assert JobList data
        self.actions.delete_job(self.api_token, self.job_id)
        job_list2 = self.actions.get_job_list(self.api_token)
        self.assertFalse(self.contains_job(self.job_id, job_list2), 'JobId should not be in JobList')

        # Delete current API key and try to re-login (should fail)
        self.actions.remove_api_key(self.api_token, self.secure_key)
        self.actions.logout(self.api_token)
        self.api_token = None

        # Should not be able to login using invalid API key
        with self.assertRaises(WebError) as err:
            self.api_token = self.actions.login(config.username, self.secure_key)
            self.assertEqual(ErrorType.ACCOUNT_UNPRIVILEGED.value, err.error_type, 'Unexpected error type')

    def contains_job(self, job_id, job_list):
        for j in job_list['ActiveJobs']:
            if job_id == j['JobId']:
                return True
        return False
