module Cielo24
  class BaseOptions

    def get_hash
      hash = {}
      self.instance_variables.each{ |var|
        value = self.instance_variable_get(var)
        if !value.nil?
          hash[var.to_s.delete("@")] = self.instance_variable_get(var)
        end
      }
      return hash
    end

    def to_query
      hash = get_hash
      array = Array.new()
      hash.each do |key, value|
        array.push(key + '=' + value.to_s)
      end
      return array.join("&")
    end

    def populate_from_key_value_pair(key, value)
      # Iterate over instance variables
      self.instance_variables.each{ |var|
        if var.to_s.delete("@") == key
          self.instance_variable_set(var, value)
          break
        end
      }
    end

    def populate_from_hash(hash)
      hash.each do |key, value|
        populate_from_key_value_pair(key, value)
      end
    end
  end

  class CommonOptions < BaseOptions

    attr_accessor :characters_per_caption_line
    attr_accessor :elementlist_version
    attr_accessor :emit_speaker_change_token_as
    attr_accessor :mask_profanity
    attr_accessor :remove_sounds_list
    attr_accessor :remove_sound_references
    attr_accessor :replace_slang
    attr_accessor :sound_boundaries

    def initialize(characters_per_caption_line: nil,
                   elementlist_version: nil,
                   emit_speaker_change_token_as: nil,
                   mask_profanity: nil,
                   remove_sounds_list: nil,
                   remove_sound_references: nil,
                   replace_slang: nil,
                   sound_boundaries: nil)
      @characters_per_caption_line = characters_per_caption_line
      @elementlist_version = elementlist_version
      @emit_speaker_change_token_as = emit_speaker_change_token_as
      @mask_profanity = mask_profanity
      @remove_sounds_list = remove_sounds_list
      @remove_sound_references = remove_sound_references
      @replace_slang = replace_slang
      @sound_boundaries = sound_boundaries
    end
  end

  class TranscriptionOptions < CommonOptions

    attr_accessor :create_paragraphs
    attr_accessor :newlines_after_paragraph
    attr_accessor :newlines_after_sentence
    attr_accessor :timecode_every_paragraph
    attr_accessor :timecode_format
    attr_accessor :time_code_interval
    attr_accessor :timecode_offset

    def initialize(create_paragraphs: nil,
                   newlines_after_paragraph: nil,
                   newlines_after_sentence: nil,
                   timecode_every_paragraph: nil,
                   timecode_format: nil,
                   time_code_interval: nil,
                   timecode_offset: nil)
      @create_paragraphs = create_paragraphs
      @newlines_after_paragraph = newlines_after_paragraph
      @newlines_after_sentence = newlines_after_sentence
      @timecode_every_paragraph = timecode_every_paragraph
      @timecode_format = timecode_format
      @time_code_interval = time_code_interval
      @timecode_offset = timecode_offset
    end
  end

  class CaptionOptions < CommonOptions

    attr_accessor :build_url
    attr_accessor :caption_words_min
    attr_accessor :caption_by_sentence
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
    attr_accessor :minimum_merge_gap_interval
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
    attr_accessor :srt_print
    attr_accessor :strip_square_brackets
    attr_accessor :utf8_mark

    def initialize(build_url: nil,
                   caption_words_min: nil,
                   caption_by_sentence: nil,
                   dfxp_header: nil,
                   disallow_dangling: nil,
                   display_effects_speaker_as: nil,
                   display_speaker_id: nil,
                   force_case: nil,
                   include_dfxp_metadata: nil,
                   layout_target_caption_length_ms: nil,
                   line_break_on_sentence: nil,
                   line_ending_format: nil,
                   lines_per_caption: nil,
                   maximum_caption_duration: nil,
                   merge_gap_interval: nil,
                   minimum_caption_length_ms: nil,
                   minimum_gap_between_captions_ms: nil,
                   minimum_merge_gap_interval: nil,
                   qt_seamless: nil,
                   silence_max_ms: nil,
                   single_speaker_per_caption: nil,
                   sound_threshold: nil,
                   sound_tokens_by_caption: nil,
                   sound_tokens_by_line: nil,
                   sound_tokens_by_caption_list: nil,
                   sound_tokens_by_line_list: nil,
                   speaker_on_new_line: nil,
                   srt_format: nil,
                   srt_print: nil,
                   strip_square_brackets: nil,
                   utf8_mark: nil)
      @build_url = build_url
      @caption_words_min = caption_words_min
      @caption_by_sentence = caption_by_sentence
      @dfxp_header = dfxp_header
      @disallow_dangling = disallow_dangling
      @display_effects_speaker_as = display_effects_speaker_as
      @display_speaker_id = display_speaker_id
      @force_case = force_case
      @include_dfxp_metadata = include_dfxp_metadata
      @layout_target_caption_length_ms = layout_target_caption_length_ms
      @line_break_on_sentence = line_break_on_sentence
      @line_ending_format = line_ending_format
      @lines_per_caption = lines_per_caption
      @maximum_caption_duration = maximum_caption_duration
      @merge_gap_interval = merge_gap_interval
      @minimum_caption_length_ms = minimum_caption_length_ms
      @minimum_gap_between_captions_ms = minimum_gap_between_captions_ms
      @minimum_merge_gap_interval = minimum_merge_gap_interval
      @qt_seamless = qt_seamless
      @silence_max_ms = silence_max_ms
      @single_speaker_per_caption = single_speaker_per_caption
      @sound_threshold = sound_threshold
      @sound_tokens_by_caption = sound_tokens_by_caption
      @sound_tokens_by_line = sound_tokens_by_line
      @sound_tokens_by_caption_list = sound_tokens_by_caption_list
      @sound_tokens_by_line_list = sound_tokens_by_line_list
      @speaker_on_new_line = speaker_on_new_line
      @srt_format = srt_format
      @srt_print = srt_print
      @strip_square_brackets = strip_square_brackets
      @utf8_mark = utf8_mark
    end
  end

  class PerformTranscriptionOptions < BaseOptions

    attr_accessor :customer_approval_steps
    attr_accessor :customer_approval_tool
    attr_accessor :custom_metadata
    attr_accessor :notes
    attr_accessor :return_iwp
    attr_accessor :speaker_id

    def initialize(customer_approval_steps: nil,
                   customer_approval_tool: nil,
                   custom_metadata: nil,
                   notes: nil,
                   return_iwp: nil,
                   speaker_id: nil)
      @customer_approval_steps = customer_approval_steps
      @customer_approval_tool = customer_approval_tool
      @custom_metadata = custom_metadata
      @notes = notes
      @return_iwp = return_iwp
      @speaker_id = speaker_id
    end
  end
end