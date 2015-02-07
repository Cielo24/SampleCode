# encoding: utf-8
from unittest import TestCase
from traceback import format_exc
from urlparse import urlparse

from cielo24.actions import Actions
from cielo24.options import *
from cielo24.web_utils import *


class TestAccess(TestCase):
    sample_video_url = "http://techslides.com/demos/sample-videos/small.mp4"
    sample_video_file_path = "C:/path/to/file.mp4"
    actions = Actions("http://sandbox-dev.cielo24.com")
    username = "api_test"
    password = "api_test"
    new_password = "api_test_new"
    api_token = None
    job_id = None
    secure_key = None
    task_id = None

    # Called before every test method runs. Can be used to set up fixture information.
    def setUp(self):
        if self.api_token is None:
            self.api_token = self.actions.login(self.username, self.password, None, True)
        if self.job_id is None:
            self.job_id = self.actions.create_job(self.api_token)['JobId']

    def test_options(self):
        co = CaptionOptions()
        co.build_url = True
        co.dfxp_header = "header"
        self.assertEqual("build_url=true&dfxp_header=header", co.to_query())
  
    def test_login_and_logout(self):
        try:
            # Username, password, no headers
            self.api_token = self.actions.login(self.username, self.password)
            self.assertEqual(32, len(self.api_token))
            # Username, password, headers
            self.api_token = self.actions.login(self.username, self.password, None, True)
            self.assertEqual(32, len(self.api_token))
            self.secure_key = self.actions.generate_api_key(self.api_token, self.username, False)
            # Username, secure key, no headers
            self.api_token = self.actions.login(self.username, None, self.secure_key)
            self.assertEqual(32, len(self.api_token))
            # Username, secure key, headers
            self.api_token = self.actions.login(self.username, None, self.secure_key, True)
            self.assertEqual(32, len(self.api_token))
            # Logout
            self.actions.logout(self.api_token)
            #assert_raise(WebError) {self.actions.logout("123")}
            self.api_token = None
        except Exception as e:
            print(format_exc())
            self.fail("test_login_and_logout() failed.")

    def test_generate_and_remove_api_key(self):
        try:
            self.secure_key = self.actions.generate_api_key(self.api_token, self.username, False)
            self.assertEqual(32, len(self.secure_key))
            self.secure_key = self.actions.generate_api_key(self.api_token, self.username, True)
            self.assertEqual(32, len(self.secure_key))
            self.actions.remove_api_key(self.api_token, self.secure_key)
        except Exception as e:
            print(format_exc())
            self.fail("test_generate_and_remove_api_key() failed.")

    def test_update_password(self):
        try:
            self.actions.update_password(self.api_token, self.new_password)
            self.actions.update_password(self.api_token, self.password)
            self.assertRaises(WebError, self.actions.update_password, "not_an_api_token", self.password)
        except Exception as e:
            print(format_exc())
            self.fail("test_update_password() failed.")

    def test_create_job(self):
        try:
            json_object = self.actions.create_job(self.api_token, "testname", "en")
            self.assertEqual(32, len(json_object['JobId']))
            self.assertEqual(32, len(json_object['TaskId']))
        except Exception as e:
            print(format_exc())
            self.fail("test_create_job() failed.")

    def test_authorize_job(self):
        try:
            self.actions.authorize_job(self.api_token, self.job_id)
            self.job_id = None
        except Exception as e:
            print(format_exc())
            self.fail("test_authorize_job() failed.")

    def test_delete_job(self):
        try:
            self.task_id = self.actions.delete_job(self.api_token, self.job_id)
            self.assertEqual(32, len(self.task_id))
            self.job_id = None
        except Exception as e:
            print(format_exc())
            self.fail("test_delete_job() failed.")

    def test_gets(self):
        try:
            json_object = self.actions.get_job_info(self.api_token, self.job_id)
            self.assertIsNotNone(json_object.get(["JobId"]))

            json_object = self.actions.get_job_list(self.api_token)
            self.assertIsNotNone(json_object.get(["ActiveJobs"]))

            json_object = self.actions.get_element_list(self.api_token, self.job_id)
            self.assertIsNotNone(json_object.get(["version"]))

            json_object = self.actions.get_list_of_element_lists(self.api_token, self.job_id)
            self.assertTrue(isinstance(json_object, list))

            media_url = self.actions.get_media(self.api_token, self.job_id)
            parsed_url = urlparse(media_url)
            self.assertIsNot(parsed_url.scheme, '')
            self.assertIsNot(parsed_url.netloc, '')
        except Exception as e:
            print(format_exc())
            self.fail("test_gets() failed.")

    def test_get_text(self):
        try:
            self.actions.get_caption(self.api_token, self.job_id, "SRT")
            self.actions.get_transcript(self.api_token, self.job_id)
            co = CaptionOptions()
            co.build_url = True
            text = self.actions.get_caption(self.api_token, self.job_id, "SRT", co)
            self.assertTrue(text.__contains__("http"))  # URL must be returned
        except Exception as e:
            print(format_exc())
            self.fail("test_get_text() failed.")

    def test_perform_transcription(self):
        try:
            self.task_id = self.actions.add_media_to_job_url(self.api_token, self.job_id, self.sample_video_url)
            self.assertEqual(32, len(self.task_id))
            self.task_id = self.actions.perform_transcription(self.api_token, self.job_id, "PREMIUM", "STANDARD")
            self.assertEqual(32, len(self.task_id))
        except Exception as e:
            print(format_exc())
            self.fail("test_perform_transcription() failed.")

    def test_add_data(self):
        try:
            self.task_id = self.actions.add_media_to_job_url(self.api_token, self.job_id, self.sample_video_url)
            self.assertEqual(32, len(self.task_id))
            self.job_id = self.actions.create_job(self.api_token)['JobId']
            self.task_id = self.actions.add_media_to_job_embedded(self.api_token, self.job_id, self.sample_video_url)
            self.assertEqual(32, len(self.task_id))
            self.job_id = self.actions.create_job(self.api_token)['JobId']
            file = open(self.sample_video_file_path, "rb")
            self.task_id = self.actions.add_media_to_job_file(self.api_token, self.job_id, file)
            self.assertEqual(32, len(self.task_id))
        except Exception as e:
            print(format_exc())
            self.fail("test_add_data() failed.")