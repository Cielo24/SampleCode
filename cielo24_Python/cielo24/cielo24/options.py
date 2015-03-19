# encoding: utf-8
from re import compile


class BaseOptions(object):

    def get_dict(self):
        return dict((k, v) for k, v in vars(self).iteritems() if v)

    def to_query(self):
        option_dict = self.get_dict()
        query_array = list()
        for k, v in option_dict.iteritems():
            query_array.append(k + "=" + self.__get_string_value(v))
        return "&".join(query_array)

    @staticmethod
    def __get_string_value(value):
        if isinstance(value, bool):
            return str(value).lower()
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
        self.elementlist_version = elementlist_version
        self.emit_speaker_change_token_as = emit_speaker_change_token_as
        self.mask_profanity = mask_profanity
        self.remove_disfluencies = remove_disfluencies
        self.remove_sounds_list = remove_sounds_list
        self.remove_sound_references = remove_sound_references
        self.replace_slang = replace_slang
        self.sound_boundaries = sound_boundaries


class TranscriptionOptions(CommonOptions):
    def __init__(self,
                 create_paragraphs=None,
                 newlines_after_paragraph=None,
                 newlines_after_sentence=None,
                 timecode_every_paragraph=None,
                 timecode_format=None,
                 timecode_interval=None,
                 timecode_offset=None):
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
                 utf8_mark=None):
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
                 sub_account=None):
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
        self.username = sub_account