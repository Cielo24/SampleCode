module Cielo24
  class BaseOptions

    def get_hash
      hash = {}
      self.instance_variables.each{ |var|
        value = self.instance_variable_get(var)
        unless value.nil?
          hash[var.to_s.delete('@')] = value
        end
      }
      return hash
    end

    def to_query
      hash = get_hash
      array = Array.new
      hash.each do |key, value|
        array.push(key + '=' + value.to_s)
      end
      return array.join('&')
    end

    def populate_from_key_value_pair(key, value)
      # Iterate over instance variables
      self.instance_variables.each{ |var|
        # key gets converted to_s because it can be a Symbol
        if var.to_s.delete('@') == key.to_s
          self.instance_variable_set(var, value)
          break
        end
      }
    end

    def populate_from_hash(hash)
      unless hash.nil?
        hash.each do |key, value|
          populate_from_key_value_pair(key, value)
        end
      end
    end
  end

  class CommonOptions < BaseOptions

    attr_accessor :elementlist_version
    attr_accessor :emit_speaker_change_token_as
    attr_accessor :mask_profanity
    attr_accessor :remove_disfluencies
    attr_accessor :remove_sounds_list
    attr_accessor :remove_sound_references
    attr_accessor :replace_slang
    attr_accessor :sound_boundaries

    def initialize
      @elementlist_version = nil
      @emit_speaker_change_token_as = nil
      @mask_profanity = nil
      @remove_disfluencies = nil
      @remove_sounds_list = nil
      @remove_sound_references = nil
      @replace_slang = nil
      @sound_boundaries = nil
    end
  end

  class TranscriptOptions < CommonOptions

    attr_accessor :create_paragraphs
    attr_accessor :newlines_after_paragraph
    attr_accessor :newlines_after_sentence
    attr_accessor :timecode_every_paragraph
    attr_accessor :timecode_format
    attr_accessor :timecode_interval
    attr_accessor :timecode_offset

    def initialize(option_hash={})
      @create_paragraphs = nil
      @newlines_after_paragraph = nil
      @newlines_after_sentence = nil
      @timecode_every_paragraph = nil
      @timecode_format = nil
      @timecode_interval = nil
      @timecode_offset = nil
      populate_from_hash(option_hash)
    end
  end

  class CaptionOptions < CommonOptions

    attr_accessor :build_url
    attr_accessor :caption_words_min
    attr_accessor :caption_by_sentence
    attr_accessor :characters_per_caption_line
    attr_accessor :dfxp_header
    attr_accessor :disallow_dangling
    attr_accessor :display_effects_speaker_as
    attr_accessor :display_speaker_id
    attr_accessor :force_case
    attr_accessor :include_dfxp_metadata
    attr_accessor :layout_target_caption_length_ms
    attr_accessor :line_break_on_sentence
    attr_accessor :line_ending_format
    attr_accessor :lines_per_caption
    attr_accessor :maximum_caption_duration
    attr_accessor :merge_gap_interval
    attr_accessor :minimum_caption_length_ms
    attr_accessor :minimum_gap_between_captions_ms
    attr_accessor :qt_seamless
    attr_accessor :silence_max_ms
    attr_accessor :single_speaker_per_caption
    attr_accessor :sound_threshold
    attr_accessor :sound_tokens_by_caption
    attr_accessor :sound_tokens_by_line
    attr_accessor :sound_tokens_by_caption_list
    attr_accessor :sound_tokens_by_line_list
    attr_accessor :speaker_on_new_line
    attr_accessor :srt_format
    attr_accessor :strip_square_brackets
    attr_accessor :utf8_mark

    def initialize(option_hash={})
      @build_url = nil
      @caption_words_min = nil
      @caption_by_sentence = nil
      @characters_per_caption_line = nil
      @dfxp_header = nil
      @disallow_dangling = nil
      @display_effects_speaker_as = nil
      @display_speaker_id = nil
      @force_case = nil
      @include_dfxp_metadata = nil
      @layout_target_caption_length_ms = nil
      @line_break_on_sentence = nil
      @line_ending_format = nil
      @lines_per_caption = nil
      @maximum_caption_duration = nil
      @merge_gap_interval = nil
      @minimum_caption_length_ms = nil
      @minimum_gap_between_captions_ms = nil
      @qt_seamless = nil
      @silence_max_ms = nil
      @single_speaker_per_caption = nil
      @sound_threshold = nil
      @sound_tokens_by_caption = nil
      @sound_tokens_by_line = nil
      @sound_tokens_by_caption_list = nil
      @sound_tokens_by_line_list = nil
      @speaker_on_new_line = nil
      @srt_format = nil
      @strip_square_brackets = nil
      @utf8_mark = nil
      populate_from_hash(option_hash)
    end
  end

  class PerformTranscriptionOptions < BaseOptions

    attr_accessor :customer_approval_steps
    attr_accessor :customer_approval_tool
    attr_accessor :custom_metadata
    attr_accessor :generate_media_intelligence_for_iwp
    attr_accessor :notes
    attr_accessor :return_iwp
    attr_accessor :speaker_id

    def initialize(option_hash={})
      @customer_approval_steps = nil
      @customer_approval_tool = nil
      @custom_metadata = nil
      @generate_media_intelligence_for_iwp = nil
      @notes = nil
      @return_iwp = nil
      @speaker_id = nil
      populate_from_hash(option_hash)
    end
  end

  class JobListOptions < BaseOptions

    attr_accessor :CreationDateFrom
    attr_accessor :CreationDateTo
    attr_accessor :StartDateFrom
    attr_accessor :StartDateTo
    attr_accessor :DueDateFrom
    attr_accessor :DueDateTo
    attr_accessor :CompleteDateFrom
    attr_accessor :CompleteDateTo
    attr_accessor :JobStatus
    attr_accessor :Fidelity
    attr_accessor :Priority
    attr_accessor :TurnaroundTimeHoursFrom
    attr_accessor :TurnaroundTimeHoursTo
    attr_accessor :JobName
    attr_accessor :ExternalId
    attr_accessor :JobDifficulty
    attr_accessor :Username

    def initialize(option_hash={})
      @CreationDateFrom = nil
      @CreationDateTo = nil
      @StartDateFrom = nil
      @StartDateTo = nil
      @DueDateFrom = nil
      @DueDateTo = nil
      @CompleteDateFrom = nil
      @CompleteDateTo = nil
      @JobStatus = nil
      @Fidelity = nil
      @Priority = nil
      @TurnaroundTimeHoursFrom = nil
      @TurnaroundTimeHoursTo = nil
      @JobName = nil
      @ExternalId = nil
      @JobDifficulty = nil
      @Username = nil
      populate_from_hash(option_hash)
    end
  end
end