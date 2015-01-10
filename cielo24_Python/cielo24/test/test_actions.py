# encoding: utf-8
from unittest import TestCase
from urlparse import urlparse

from cielo24.actions import Actions
from cielo24.options import *
from cielo24.web_utils import *
from cielo24.enums import *


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


class JobTest(ActionsTest):
    sample_video_url = "http://techslides.com/demos/sample-videos/small.mp4"
    sample_video_file_path = "C:/path/to/file.mp4"
    job_id = None
    task_id = None

    def setUp(self):
        super(JobTest, self).setUp()
        if self.job_id is None:
            self.job_id = self.actions.create_job(self.api_token)['JobId']

    # Since all option classes extend BaseOptions class (with all of the functionality) we only need to test one class
    def test_options(self):
        options = CaptionOptions()
        options.build_url = True
        options.dfxp_header = "header"
        self.assertEqual("build_url=true&dfxp_header=header", options.to_query())

    def test_create_job(self):
        response = self.actions.create_job(self.api_token, "test_name", Language.English)
        self.assertEqual(32, len(response['JobId']))
        self.assertEqual(32, len(response['TaskId']))

    def test_authorize_job(self):
        self.actions.authorize_job(self.api_token, self.job_id)
        self.job_id = None  # Create new job in setUp()

    def test_delete_job(self):
        self.task_id = self.actions.delete_job(self.api_token, self.job_id)
        self.assertEqual(32, len(self.task_id))
        self.job_id = None  # Create new job in setUp()

    def test_get_job_info(self):
        response = self.actions.get_job_info(self.api_token, self.job_id)
        self.assertIsNotNone(response.get("JobId"))

    def test_get_job_list(self):
        response = self.actions.get_job_list(self.api_token)
        self.assertIsNotNone(response.get("ActiveJobs"))

    def test_get_element_list(self):
        response = self.actions.get_element_list(self.api_token, self.job_id)
        self.assertIsNotNone(response.get("version"))

    def test_get_list_of_element_lists(self):
        response = self.actions.get_list_of_element_lists(self.api_token, self.job_id)
        self.assertTrue(isinstance(response, list))

    def test_get_media(self):
        # Add media to job first
        self.actions.add_media_to_job_url(self.api_token, self.job_id, self.sample_video_url)
        # Test get media
        media_url = self.actions.get_media(self.api_token, self.job_id)
        parsed_url = urlparse(media_url)
        self.assertIsNot(parsed_url.scheme, '')
        self.assertIsNot(parsed_url.netloc, '')
        self.assertTrue(media_url.__contains__("http"))  # URL must be returned
        self.job_id = None  # Create new job in setUp()

    def test_get_transcript(self):
        self.actions.get_transcript(self.api_token, self.job_id)

    def test_get_caption(self):
        self.actions.get_caption(self.api_token, self.job_id, CaptionFormat.SRT)

    def test_get_caption_build_url(self):
        options = CaptionOptions(build_url=True)
        caption_url = self.actions.get_caption(self.api_token, self.job_id, CaptionFormat.SRT, options)
        parsed_url = urlparse(caption_url)
        self.assertIsNot(parsed_url.scheme, '')
        self.assertIsNot(parsed_url.netloc, '')
        self.assertTrue(caption_url.__contains__("http"))  # URL must be returned

    def test_perform_transcription(self):
        self.task_id = self.actions.add_media_to_job_url(self.api_token, self.job_id, self.sample_video_url)
        self.assertEqual(32, len(self.task_id))
        self.task_id = self.actions.perform_transcription(self.api_token, self.job_id, Fidelity.PREMIUM, Priority.STANDARD)
        self.assertEqual(32, len(self.task_id))

    def test_add_media_to_job_url(self):
        self.task_id = self.actions.add_media_to_job_url(self.api_token, self.job_id, self.sample_video_url)
        self.assertEqual(32, len(self.task_id))
        self.job_id = None  # Create new job in setUp()

    def test_add_media_to_job_embedded(self):
        self.task_id = self.actions.add_media_to_job_embedded(self.api_token, self.job_id, self.sample_video_url)
        self.assertEqual(32, len(self.task_id))
        self.job_id = None  # Create new job in setUp()

    def test_add_media_to_job_file(self):
        file = open(self.sample_video_file_path, "rb")
        self.task_id = self.actions.add_media_to_job_file(self.api_token, self.job_id, file)
        self.assertEqual(32, len(self.task_id))
        self.job_id = None  # Create new job in setUp()