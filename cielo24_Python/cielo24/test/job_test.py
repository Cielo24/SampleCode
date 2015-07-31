# encoding: utf-8
from uuid import uuid4
from datetime import datetime
from actions_test import ActionsTest
from urlparse import urlparse
from cielo24.options import BaseOptions, CaptionOptions, JobListOptions, TranscriptOptions, PerformTranscriptionOptions
from cielo24.enums import CaptionFormat, Language, Fidelity, Priority, SoundTag
import config as config


class JobTest(ActionsTest):

    def setUp(self):
        super(JobTest, self).setUp()
        # Always start with a fresh job
        self.job_id = self.actions.create_job(self.api_token, 'Python_test')['JobId']

    def test_options_get_dict(self):
        options = JobListOptions()
        options.CreationDateFrom = datetime(2015, 6, 25, 15, 45, 34, 123456)
        options.Fidelity = Fidelity.PROFESSIONAL
        options.ExternalId = 'Python_id'
        options.TurnaroundTimeHoursTo = 45
        test_dict = {'CreationDateFrom': datetime(2015, 6, 25, 15, 45, 34, 123456).isoformat(),
                     'Fidelity': str(Fidelity.PROFESSIONAL),
                     'ExternalId': 'Python_id',
                     'TurnaroundTimeHoursTo': str(45)}
        self.assertEqual(options.get_dict(), test_dict)
        # Can only assert length because Dict produces different order each time
        expected_length = len(test_dict) - 1
        for (k, v) in test_dict.iteritems():
            expected_length += len(str(k)) + 1 + len(str(v))
        self.assertEqual(expected_length, len(options.to_query()))

    def test_options_populate_from_list(self):
        options = CaptionOptions()
        options.populate_from_list(['build_url=true', 'dfxp_header=header'])
        # Can only assert length because Dict produces different order each time
        self.assertEqual(len('build_url=true&dfxp_header=header'), len(options.to_query()))

    def test_option_string_conversions(self):
        # string
        self.assertEqual(BaseOptions._get_string_value('Python_test'), 'Python_test')
        # datetime
        self.assertEqual(BaseOptions._get_string_value(datetime(2015, 6, 25, 15, 45, 34, 123456)),
                         '2015-06-25T15:45:34.123456')
        # int
        self.assertEqual(BaseOptions._get_string_value(1234), '1234')
        # boolean
        self.assertEqual(BaseOptions._get_string_value(True), 'true')
        self.assertEqual(BaseOptions._get_string_value(False), 'false')
        # enum
        self.assertEqual(BaseOptions._get_string_value(SoundTag.ENDS_SENTENCE), 'ENDS_SENTENCE')
        # list of enums
        self.assertEqual(BaseOptions._get_string_value([SoundTag.NOISE]), '["NOISE"]')
        self.assertEqual(BaseOptions._get_string_value([SoundTag.BLANK_AUDIO, SoundTag.APPLAUSE]),
                         '["BLANK_AUDIO","APPLAUSE"]')
        # tuple of characters
        self.assertEqual(BaseOptions._get_string_value(('{', '}')), '("{","}")')
        # list of strings
        self.assertEqual(BaseOptions._get_string_value(['test']), '["test"]')
        self.assertEqual(BaseOptions._get_string_value(['test1', 'test2']), '["test1","test2"]')
        # dictionary
        self.assertEqual(BaseOptions._get_string_value({'notes': 'test'}), '{"notes": "test"}')
        self.assertEqual(BaseOptions._get_string_value({'notes': 'test', "speaker_id": True}),
                         '{"notes": "test", "speaker_id": true}')

    def test_create_job(self):
        response = self.actions.create_job(self.api_token, 'Python_test', Language.ENGLISH, 'Python_external_id')
        self.assertEqual(32, len(response['JobId']))
        self.assertEqual(32, len(response['TaskId']))

    def test_authorize_job(self):
        self.actions.authorize_job(self.api_token, self.job_id)

    def test_delete_job(self):
        self.task_id = self.actions.delete_job(self.api_token, self.job_id)
        self.assertEqual(32, len(self.task_id))

    def test_get_job_info(self):
        response = self.actions.get_job_info(self.api_token, self.job_id)
        self.assertIsNotNone(response.get('JobId'))

    def test_get_job_list(self):
        response = self.actions.get_job_list(self.api_token)
        self.assertIsNotNone(response.get('ActiveJobs'))

    def test_get_job_list_with_options(self):
        # Create job with unique External Id
        external_id = uuid4()
        self.job_id = self.actions.create_job(self.api_token, 'Python_test', external_id=external_id)['JobId']
        options = JobListOptions(external_id=external_id,
                                 job_name='Python_test')
        response = self.actions.get_job_list(self.api_token, options)
        self.assertEqual(len(response.get('ActiveJobs')), 1)

    def test_get_element_list(self):
        response = self.actions.get_element_list(self.api_token, self.job_id)
        self.assertIsNotNone(response.get('version'))

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
        self.assertTrue(media_url.__contains__('http'))  # URL must be returned

    def test_get_transcript(self):
        options = TranscriptOptions(timecode_every_paragraph=True)
        self.actions.get_transcript(self.api_token, self.job_id, options)

    def test_get_caption(self):
        options = CaptionOptions(caption_by_sentence=True)
        self.actions.get_caption(self.api_token, self.job_id, CaptionFormat.SRT, options)

    def test_get_caption_build_url(self):
        options = CaptionOptions(build_url=True)
        caption_url = self.actions.get_caption(self.api_token, self.job_id, CaptionFormat.SRT, options)
        parsed_url = urlparse(caption_url)
        self.assertIsNot(parsed_url.scheme, '')
        self.assertIsNot(parsed_url.netloc, '')
        self.assertTrue(caption_url.__contains__('http'))  # URL must be returned

    def test_perform_transcription(self):
        self.task_id = self.actions.add_media_to_job_url(self.api_token, self.job_id, config.sample_video_url)
        self.assertEqual(32, len(self.task_id))
        options = PerformTranscriptionOptions(notes='Python_test_notes')
        self.task_id = self.actions.perform_transcription(self.api_token,
                                                          self.job_id,
                                                          Fidelity.PREMIUM,
                                                          Priority.STANDARD,
                                                          'http://fake-url.com/callback?job_id={job_id}',
                                                          48,
                                                          Language.ENGLISH,
                                                          options)
        self.assertEqual(32, len(self.task_id))

    def test_add_media_to_job_url(self):
        self.task_id = self.actions.add_media_to_job_url(self.api_token, self.job_id, config.sample_video_url)
        self.assertEqual(32, len(self.task_id))

    def test_add_media_to_job_embedded(self):
        self.task_id = self.actions.add_media_to_job_embedded(self.api_token, self.job_id, config.sample_video_url)
        self.assertEqual(32, len(self.task_id))

    def test_add_media_to_job_file(self):
        file = open(config.sample_video_file_path, 'rb')
        self.task_id = self.actions.add_media_to_job_file(self.api_token, self.job_id, file)
        self.assertEqual(32, len(self.task_id))
