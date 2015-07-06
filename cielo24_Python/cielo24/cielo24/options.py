# encoding: utf-8
from re import compile
from datetime import datetime
import json


class BaseOptions(object):

    def get_dict(self):
        return dict((str(k), self._get_string_value(v)) for (k, v) in vars(self).iteritems() if v)

    def to_query(self):
        option_dict = self.get_dict()
        query_array = list()
        for (k, v) in option_dict.iteritems():
            query_array.append(k + '=' + v)
        return '&'.join(query_array)

    @staticmethod
    def _get_string_value(value):
        if isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, datetime):
            return value.isoformat()
        elif isinstance(value, list):
            return '["' + '","'.join([str(x) for x in value]) + '"]'
        elif isinstance(value, tuple):
            return '("' + '","'.join([str(x) for x in value]) + '")'
        elif isinstance(value, dict):
            return json.dumps(value)
        else:
            return str(value)

    def populate_from_key_value_pair(self, key, value):
        # Iterate over instance variables
        for k, v in vars(self).iteritems():
            if k == key:
                setattr(self, key, value)
                break

    def populate_from_list(self, option_list):
        pattern = compile("([^?=&]+)(=([^&]*))?")
        if option_list is None:
            return
        for item in option_list:
            match = pattern.match(item)
            self.populate_from_key_value_pair(match.group(1), match.group(3))


class CommonOptions(BaseOptions):
    def __init__(self,
                 elementlist_version=None,
                 emit_speaker_change_token_as=None,
                 mask_profanity=None,
                 remove_disfluencies=None,
                 remove_sounds_list=None,
                 remove_sound_references=None,
                 replace_slang=None,
                 sound_boundaries=None):
        """
        Types of the constructor parameters that are guaranteed to result in a valid query string.
        Parameters that are not supplied (remain None) will not be used when building the query.
        Any parameter can also be supplied as a string, but then the caller is responsible for making sure
        that the string has a valid format (e.g. ISO format for datetime). See cielo24 Docs for details.
        :param elementlist_version: datetime
        :param emit_speaker_change_token_as: string
        :param mask_profanity: boolean
        :param remove_disfluencies: boolean
        :param remove_sounds_list: list of SoundTag enums
        :param remove_sound_references: boolean
        :param replace_slang: boolean
        :param sound_boundaries: 2-tuple of characters
        :return:
        """
        self.elementlist_version = elementlist_version
        self.emit_speaker_change_token_as = emit_speaker_change_token_as
        self.mask_profanity = mask_profanity
        self.remove_disfluencies = remove_disfluencies
        self.remove_sounds_list = remove_sounds_list
        self.remove_sound_references = remove_sound_references
        self.replace_slang = replace_slang
        self.sound_boundaries = sound_boundaries


class TranscriptOptions(CommonOptions):
    def __init__(self,
                 create_paragraphs=None,
                 newlines_after_paragraph=None,
                 newlines_after_sentence=None,
                 timecode_every_paragraph=None,
                 timecode_format=None,
                 timecode_interval=None,
                 timecode_offset=None,
                 # Common Options
                 elementlist_version=None,
                 emit_speaker_change_token_as=None,
                 mask_profanity=None,
                 remove_disfluencies=None,
                 remove_sounds_list=None,
                 remove_sound_references=None,
                 replace_slang=None,
                 sound_boundaries=None):
        """
        Types of the constructor parameters that are guaranteed to result in a valid query string.
        Parameters that are not supplied (remain None) will not be used when building the query.
        Any parameter can also be supplied as a string, but then the caller is responsible for making sure
        that the string has a valid format (e.g. ISO format for datetime). See cielo24 Docs for details.
        :param create_paragraphs: boolean
        :param newlines_after_paragraph: int
        :param newlines_after_sentence: int
        :param timecode_every_paragraph: boolean
        :param timecode_format: string
        :param timecode_interval: int
        :param timecode_offset: int
        :return:
        """
        super(TranscriptOptions, self).__init__(
            elementlist_version,
            emit_speaker_change_token_as,
            mask_profanity,
            remove_disfluencies,
            remove_sounds_list,
            remove_sound_references,
            replace_slang,
            sound_boundaries)
        self.create_paragraphs = create_paragraphs
        self.newlines_after_paragraph = newlines_after_paragraph
        self.newlines_after_sentence = newlines_after_sentence
        self.timecode_every_paragraph = timecode_every_paragraph
        self.timecode_format = timecode_format
        self.timecode_interval = timecode_interval
        self.timecode_offset = timecode_offset


class CaptionOptions(CommonOptions):
    def __init__(self,
                 build_url=None,
                 caption_words_min=None,
                 caption_by_sentence=None,
                 characters_per_caption_line=None,
                 dfxp_header=None,
                 disallow_dangling=None,
                 display_effects_speaker_as=None,
                 display_speaker_id=None,
                 force_case=None,
                 include_dfxp_metadata=None,
                 layout_target_caption_length_ms=None,
                 line_break_on_sentence=None,
                 line_ending_format=None,
                 lines_per_caption=None,
                 maximum_caption_duration=None,
                 merge_gap_interval=None,
                 minimum_caption_length_ms=None,
                 minimum_gap_between_captions_ms=None,
                 qt_seamless=None,
                 silence_max_ms=None,
                 single_speaker_per_caption=None,
                 sound_threshold=None,
                 sound_tokens_by_caption=None,
                 sound_tokens_by_line=None,
                 sound_tokens_by_caption_list=None,
                 sound_tokens_by_line_list=None,
                 speaker_on_new_line=None,
                 srt_format=None,
                 strip_square_brackets=None,
                 utf8_mark=None,
                 # Common Options
                 elementlist_version=None,
                 emit_speaker_change_token_as=None,
                 mask_profanity=None,
                 remove_disfluencies=None,
                 remove_sounds_list=None,
                 remove_sound_references=None,
                 replace_slang=None,
                 sound_boundaries=None):
        """
        Types of the constructor parameters that are guaranteed to result in a valid query string.
        Parameters that are not supplied (remain None) will not be used when building the query.
        Any parameter can also be supplied as a string, but then the caller is responsible for making sure
        that the string has a valid format (e.g. ISO format for datetime). See cielo24 Docs for details.
        :param build_url: boolean
        :param caption_words_min: int
        :param caption_by_sentence: boolean
        :param characters_per_caption_line: int
        :param dfxp_header: XML String
        :param disallow_dangling: boolean
        :param display_effects_speaker_as: string
        :param display_speaker_id: SpeakerID enum
        :param force_case: Case enum
        :param include_dfxp_metadata: boolean
        :param layout_target_caption_length_ms: int
        :param line_break_on_sentence: boolean
        :param line_ending_format: LineEnding enum
        :param lines_per_caption: int
        :param maximum_caption_duration: int
        :param merge_gap_interval: int
        :param minimum_caption_length_ms: int
        :param minimum_gap_between_captions_ms: int
        :param qt_seamless: boolean
        :param silence_max_ms: int
        :param single_speaker_per_caption: boolean
        :param sound_threshold: int
        :param sound_tokens_by_caption: boolean
        :param sound_tokens_by_line: boolean
        :param sound_tokens_by_caption_list: list of SoundTag enums
        :param sound_tokens_by_line_list: list of SoundTag enums
        :param speaker_on_new_line: boolean
        :param srt_format: string
        :param strip_square_brackets: boolean
        :param utf8_mark: boolean
        :return:
        """
        super(CaptionOptions, self).__init__(
            elementlist_version,
            emit_speaker_change_token_as,
            mask_profanity,
            remove_disfluencies,
            remove_sounds_list,
            remove_sound_references,
            replace_slang,
            sound_boundaries)
        self.build_url = build_url
        self.caption_words_min = caption_words_min
        self.caption_by_sentence = caption_by_sentence
        self.characters_per_caption_line = characters_per_caption_line
        self.dfxp_header = dfxp_header
        self.disallow_dangling = disallow_dangling
        self.display_effects_speaker_as = display_effects_speaker_as
        self.display_speaker_id = display_speaker_id
        self.force_case = force_case
        self.include_dfxp_metadata = include_dfxp_metadata
        self.layout_target_caption_length_ms = layout_target_caption_length_ms
        self.line_break_on_sentence = line_break_on_sentence
        self.line_ending_format = line_ending_format
        self.lines_per_caption = lines_per_caption
        self.maximum_caption_duration = maximum_caption_duration
        self.merge_gap_interval = merge_gap_interval
        self.minimum_caption_length_ms = minimum_caption_length_ms
        self.minimum_gap_between_captions_ms = minimum_gap_between_captions_ms
        self.qt_seamless = qt_seamless
        self.silence_max_ms = silence_max_ms
        self.single_speaker_per_caption = single_speaker_per_caption
        self.sound_threshold = sound_threshold
        self.sound_tokens_by_caption = sound_tokens_by_caption
        self.sound_tokens_by_line = sound_tokens_by_line
        self.sound_tokens_by_caption_list = sound_tokens_by_caption_list
        self.sound_tokens_by_line_list = sound_tokens_by_line_list
        self.speaker_on_new_line = speaker_on_new_line
        self.srt_format = srt_format
        self.strip_square_brackets = strip_square_brackets
        self.utf8_mark = utf8_mark


class PerformTranscriptionOptions(BaseOptions):
    def __init__(self,
                 customer_approval_steps=None,
                 customer_approval_tool=None,
                 custom_metadata=None,
                 generate_media_intelligence_for_iwp=None,
                 notes=None,
                 return_iwp=None,
                 speaker_id=None):
        """
        Types of the constructor parameters that are guaranteed to result in a valid query string.
        Parameters that are not supplied (remain None) will not be used when building the query.
        Any parameter can also be supplied as a string, but then the caller is responsible for making sure
        that the string has a valid format (e.g. ISO format for datetime). See cielo24 Docs for details.
        :param customer_approval_steps: list of CustomerApprovalStep enums
        :param customer_approval_tool: CustomerApprovalTool enum
        :param custom_metadata: single level JSON dictionary
        :param generate_media_intelligence_for_iwp: list of IWP enums
        :param notes: string
        :param return_iwp: list of IWP enums
        :param speaker_id: boolean
        :return:
        """
        self.customer_approval_steps = customer_approval_steps
        self.customer_approval_tool = customer_approval_tool
        self.custom_metadata = custom_metadata
        self.generate_media_intelligence_for_iwp = generate_media_intelligence_for_iwp
        self.notes = notes
        self.return_iwp = return_iwp
        self.speaker_id = speaker_id


class JobListOptions(BaseOptions):
    def __init__(self,
                 creation_date_from=None,
                 creation_date_to=None,
                 start_date_from=None,
                 start_date_to=None,
                 due_date_from=None,
                 due_date_to=None,
                 complete_date_from=None,
                 complete_date_to=None,
                 job_status=None,
                 fidelity=None,
                 priority=None,
                 turnaround_time_hours_from=None,
                 turnaround_time_hours_to=None,
                 job_name=None,
                 external_id=None,
                 job_difficulty=None,
                 sub_account=None):
        """
        Types of the constructor parameters that are guaranteed to result in a valid query string.
        Parameters that are not supplied (remain None) will not be used when building the query.
        Any parameter can also be supplied as a string, but then the caller is responsible for making sure
        that the string has a valid format (e.g. ISO format for datetime). See cielo24 Docs for details.
        :param creation_date_from: datetime
        :param creation_date_to: datetime
        :param start_date_from: datetime
        :param start_date_to: datetime
        :param due_date_from: datetime
        :param due_date_to: datetime
        :param complete_date_from: datetime
        :param complete_date_to: datetime
        :param job_status: JobStatus enum
        :param fidelity: Fidelity enum
        :param priority: Priority enum
        :param turnaround_time_hours_from: int
        :param turnaround_time_hours_to: int
        :param job_name: string
        :param external_id: string
        :param job_difficulty: JobDifficulty enum
        :param sub_account: string
        :return:
        """
        self.CreationDateFrom = creation_date_from
        self.CreationDateTo = creation_date_to
        self.StartDateFrom = start_date_from
        self.StartDateTo = start_date_to
        self.DueDateFrom = due_date_from
        self.DueDateTo = due_date_to
        self.CompleteDateFrom = complete_date_from
        self.CompleteDateTo = complete_date_to
        self.JobStatus = job_status
        self.Fidelity = fidelity
        self.Priority = priority
        self.TurnaroundTimeHoursFrom = turnaround_time_hours_from
        self.TurnaroundTimeHoursTo = turnaround_time_hours_to
        self.JobName = job_name
        self.ExternalId = external_id
        self.JobDifficulty = job_difficulty
        self.Username = sub_account
