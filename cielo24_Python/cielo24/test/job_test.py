# encoding: utf-8
from actions_test import ActionsTest
from urlparse import urlparse
from cielo24.options import CaptionOptions
from cielo24.enums import Case, CaptionFormat, Language, Fidelity, Priority
import config as config


class JobTest(ActionsTest):

    job_id = None
    task_id = None

    def setUp(self):
        super(JobTest, self).setUp()
        # Always start with a fresh job
        self.job_id = self.actions.create_job(self.api_token, "Python_test")['JobId']

    # Since all option classes extend BaseOptions class (with all of the functionality) we only need to test one class
    def test_options(self):
        options = CaptionOptions()
        options.populate_from_list(["build_url=true", "dfxp_header=header"])
        options.force_case = Case.UPPER
        options.caption_by_sentence = True
        # Can only assert length because Dict produces different order each time
        self.assertEqual(len("build_url=true&caption_by_sentence=true&dfxp_header=header&force_case=upper"), len(options.to_query()))

    def test_create_job(self):
        response = self.actions.create_job(self.api_token, "Python_test", Language.English)
        self.assertEqual(32, len(response['JobId']))
        self.assertEqual(32, len(response['TaskId']))

    def test_authorize_job(self):
        self.actions.authorize_job(self.api_token, self.job_id)

    def test_delete_job(self):
        self.task_id = self.actions.delete_job(self.api_token, self.job_id)
        self.assertEqual(32, len(self.task_id))

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
        self.actions.add_media_to_job_url(self.api_token, self.job_id, config.sample_video_url)
        # Test get media
        media_url = self.actions.get_media(self.api_token, self.job_id)
        parsed_url = urlparse(media_url)
        self.assertIsNot(parsed_url.scheme, '')
        self.assertIsNot(parsed_url.netloc, '')
        self.assertTrue(media_url.__contains__("http"))  # URL must be returned

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
        self.task_id = self.actions.add_media_to_job_url(self.api_token, self.job_id, config.sample_video_url)
        self.assertEqual(32, len(self.task_id))
        self.task_id = self.actions.perform_transcription(self.api_token, self.job_id, Fidelity.PREMIUM, Priority.STANDARD)
        self.assertEqual(32, len(self.task_id))

    def test_add_media_to_job_url(self):
        self.task_id = self.actions.add_media_to_job_url(self.api_token, self.job_id, config.sample_video_url)
        self.assertEqual(32, len(self.task_id))

    def test_add_media_to_job_embedded(self):
        self.task_id = self.actions.add_media_to_job_embedded(self.api_token, self.job_id, config.sample_video_url)
        self.assertEqual(32, len(self.task_id))

    def test_add_media_to_job_file(self):
        file = open(config.sample_video_file_path, "rb")
        self.task_id = self.actions.add_media_to_job_file(self.api_token, self.job_id, file)
        self.assertEqual(32, len(self.task_id))
