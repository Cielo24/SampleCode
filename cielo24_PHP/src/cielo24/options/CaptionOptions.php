<?php

require_once("CommonFormattingOptions.php");

class CaptionOptions extends CommonFormattingOptions
{
    public $build_url;
    public $caption_words_min;
    public $caption_by_sentence;
    public $characters_per_caption_line;
    public $dfxp_header;
    public $disallow_dangling;
    public $display_effects_speaker_as;
    public $display_speaker_id;
    public $force_case;
    public $include_dfxp_metadata;
    public $layout_target_caption_length_ms;
    public $line_break_on_sentence;
    public $line_ending_format;
    public $lines_per_caption;
    public $maximum_caption_duration;
    public $merge_gap_interval;
    public $minimum_caption_length_ms;
    public $minimum_gap_between_captions_ms;
    public $minimum_merge_gap_interval;
    public $qt_seamless;
    public $silence_max_ms;
    public $single_speaker_per_caption;
    public $sound_threshold;
    public $sound_tokens_by_caption;
    public $sound_tokens_by_line;
    public $sound_tokens_by_caption_list;
    public $sound_tokens_by_line_list;
    public $speaker_on_new_line;
    public $srt_format;
    public $strip_square_brackets;
    public $utf8_mark;

                                // Common Options
    public function __construct(DateTime $elementListVersion = null,
                                $speakerChangeToken = null,
                                $maskProfanity = null,
                                $removeDisfluencies = null,
                                array $removeSoundsList = null,
                                $removeSoundReferences = null,
                                $replaceSlang = null,
                                array $soundBoundaries = null,
                                // Caption Options
                                $buildUri = null,
                                $captionWordsMin = null,
                                $captionBySentence = null,
                                $charactersPerCaptionLine = null,
                                $dfxpHeader = null,
                                $disallowDangling = null,
                                $effectsSpeaker = null,
                                $displaySpeakerId = null,
                                $forceCase = null,
                                $includeDfxpMetadata = null,
                                $layoutDefaultCaptionLengthMs = null,
                                $lineBreakOnSentence = null,
                                $lineEndingFormat = null,
                                $linesPerCaption = null,
                                $maximumCaptionDuration = null,
                                $mergeGapInterval = null,
                                $minimumCaptionLengthMs = null,
                                $minimumGapBetweenCaptionsMs = null,
                                $minimumMergeGapInterval = null,
                                $qtSeamless = null,
                                $silenceMaxMs = null,
                                $singleSpeakerPerCaption = null,
                                $soundThreshold = null,
                                $soundTokensByCaption = null,
                                $soundTokensByLine = null,
                                array $soundTokensByCaptionList = null,
                                array $soundTokensByLineList = null,
                                $speakerOnNewLine = null,
                                $srtFormat = null,
                                $stripSquareBrackets = null,
                                $utf8_mark = null)
    {
        parent::__construct($elementListVersion,
                            $speakerChangeToken,
                            $maskProfanity,
                            $removeDisfluencies,
                            $removeSoundsList,
                            $removeSoundReferences,
                            $replaceSlang,
                            $soundBoundaries);

        $this->build_url = $buildUri;
        $this->caption_words_min = $captionWordsMin;
        $this->caption_by_sentence = $captionBySentence;
        $this->characters_per_caption_line = $charactersPerCaptionLine;
        $this->dfxp_header = $dfxpHeader;
        $this->disallow_dangling = $disallowDangling;
        $this->display_effects_speaker_as = $effectsSpeaker;
        $this->display_speaker_id = $displaySpeakerId;
        $this->force_case = $forceCase;
        $this->include_dfxp_metadata = $includeDfxpMetadata;
        $this->layout_target_caption_length_ms = $layoutDefaultCaptionLengthMs;
        $this->line_break_on_sentence = $lineBreakOnSentence;
        $this->line_ending_format = $lineEndingFormat;
        $this->lines_per_caption = $linesPerCaption;
        $this->maximum_caption_duration = $maximumCaptionDuration;
        $this->merge_gap_interval = $mergeGapInterval;
        $this->minimum_caption_length_ms = $minimumCaptionLengthMs;
        $this->minimum_gap_between_captions_ms = $minimumGapBetweenCaptionsMs;
        $this->minimum_merge_gap_interval = $minimumMergeGapInterval;
        $this->qt_seamless = $qtSeamless;
        $this->silence_max_ms = $silenceMaxMs;
        $this->single_speaker_per_caption = $singleSpeakerPerCaption;
        $this->sound_threshold = $soundThreshold;
        $this->sound_tokens_by_caption = $soundTokensByCaption;
        $this->sound_tokens_by_line = $soundTokensByLine;
        $this->sound_tokens_by_caption_list = $soundTokensByCaptionList;
        $this->sound_tokens_by_line_list = $soundTokensByLineList;
        $this->speaker_on_new_line = $speakerOnNewLine;
        $this->srt_format = $srtFormat;
        $this->strip_square_brackets = $stripSquareBrackets;
        $this->utf8_mark = $utf8_mark;
    }
}
