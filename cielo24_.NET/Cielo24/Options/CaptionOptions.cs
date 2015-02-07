using Cielo24.JSON;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cielo24.Options
{
    public class CaptionOptions : CommonOptions
    {
        [QueryName("build_url")]
        public bool? BuildUrl { get; set; }
        [QueryName("caption_words_min")]
        public int? CaptionWordsMin { get; set; }
        [QueryName("caption_by_sentence")]
        public bool? CaptionBySentence { get; set; }
        [QueryName("characters_per_caption_line")]
        public int? CharactersPerCaptionLine { get; set; }
        [QueryName("dfxp_header")]
        public string DfxpHeader { get; set; }
        [QueryName("disallow_dangling")]
        public bool? DisallowDangling { get; set; }
        [QueryName("display_effects_speaker_as")]
        public string EffectsSpeaker { get; set; }
        [QueryName("display_speaker_id")]
        public SpeakerId? DisplayedSpeakerId { get; set; }
        [QueryName("force_case")]
        public Case? ForceCase { get; set; }
        [QueryName("include_dfxp_metadata")]
        public bool? IncludeDfxpMetadata { get; set; }
        [QueryName("layout_target_caption_length_ms")]
        public int? LayoutTargetCaptionLengthMs { get; set; }
        [QueryName("line_break_on_sentence")]
        public bool? LineBreakOnSentence { get; set; }
        [QueryName("line_ending_format")]
        public LineEnding? LineEndingFormat { get; set; }
        [QueryName("lines_per_caption")]
        public int? LinesPerCaption { get; set; }
        [QueryName("maximum_caption_duration")]
        public int? MaximumCaptionDuration { get; set; }
        [QueryName("merge_gap_interval")]
        public int? MergeGapInterval { get; set; }
        [QueryName("minimum_caption_length_ms")]
        public int? MinimumCaptionLengthMs { get; set; }
        [QueryName("minimum_gap_between_captions_ms")]
        public int? MinimumGapBetweenCaptionsMs { get; set; }
        [QueryName("minimum_merge_gap_interval")]
        public int? MinimumMergeGapInterval { get; set; }
        [QueryName("qt_seamless")]
        public bool? QtSeamless { get; set; }
        [QueryName("silence_max_ms")]
        public int? SilenceMaxMs { get; set; }
        [QueryName("single_speaker_per_caption")]
        public bool? SingleSpeakerPerCaption { get; set; }
        [QueryName("sound_threshold")]
        public int? SoundThreshold { get; set; }
        [QueryName("sound_tokens_by_caption")]
        public bool? SoundTokensByCaption { get; set; }
        [QueryName("sound_tokens_by_line")]
        public bool? SoundTokensByLine { get; set; }
        [QueryName("sound_tokens_by_caption_list")]
        public List<Tag> SoundTokensByCaptionList { get; set; }
        [QueryName("sound_tokens_by_line_list")]
        public List<Tag> SoundTokensByLineList { get; set; }
        [QueryName("speaker_on_new_line")]
        public bool? SpeakerOnNewLine { get; set; }
        [QueryName("srt_format")]
        public string SrtFormat { get; set; }
        [QueryName("strip_square_brackets")]
        public bool? StripSquareBrackets { get; set; }
        [QueryName("utf8_mark")]
        public bool? Utf8Mark { get; set; }

        public CaptionOptions(
            DateTime? elementListVersion = null,
            string speakerChangeToken = null,
            bool? maskProfanity = null,
            bool? removeDisfluencies = null,
            List<Tag> removeSoundsList = null,
            bool? removeSoundReferences = null,
            bool? replaceSlang = null,
            char[] soundBoundaries = null,
            bool? buildUri = null,
            int? captionWordsMin = null,
            bool? captionBySentence = null,
            int? charactersPerCaptionLine = null,
            string dfxpHeader = null,
            bool? disallowDangling = null,
            string effectsSpeaker = null,
            SpeakerId? displaySpeakerId = null,
            Case? forceCase = null,
            bool? includeDfxpMetadata = null,
            int? layoutDefaultCaptionLengthMs = null,
            bool? lineBreakOnSentence = null,
            LineEnding? lineEndingFormat = null,
            int? linesPerCaption = null,
            int? maximumCaptionDuration = null,
            int? mergeGapInterval = null,
            int? minimumCaptionLengthMs = null,
            int? minimumGapBetweenCaptionsMs = null,
            int? minimumMergeGapInterval = null,
            bool? qtSeamless = null,
            int? silenceMaxMs = null,
            bool? singleSpeakerPerCaption = null,
            int? soundThreshold = null,
            bool? soundTokensByCaption = null,
            bool? soundTokensByLine = null,
            List<Tag> soundTokensByCaptionList = null,
            List<Tag> soundTokensByLineList = null,
            bool? speakerOnNewLine = null,
            string srtFormat = null,
            bool? stripSquareBrackets = null,
            bool? utf8_mark = null)
            : base(elementListVersion,
                   speakerChangeToken,
                   maskProfanity,
                   removeDisfluencies,
                   removeSoundsList,
                   removeSoundReferences,
                   replaceSlang,
                   soundBoundaries)
        {
            this.BuildUrl = buildUri;
            this.CaptionWordsMin = captionWordsMin;
            this.CaptionBySentence = captionBySentence;
            this.CharactersPerCaptionLine = charactersPerCaptionLine;
            this.DfxpHeader = dfxpHeader;
            this.DisallowDangling = disallowDangling;
            this.EffectsSpeaker = effectsSpeaker;
            this.DisplayedSpeakerId = displaySpeakerId;
            this.ForceCase = forceCase;
            this.IncludeDfxpMetadata = includeDfxpMetadata;
            this.LayoutTargetCaptionLengthMs = layoutDefaultCaptionLengthMs;
            this.LineBreakOnSentence = lineBreakOnSentence;
            this.LineEndingFormat = lineEndingFormat;
            this.LinesPerCaption = linesPerCaption;
            this.MaximumCaptionDuration = maximumCaptionDuration;
            this.MergeGapInterval = mergeGapInterval;
            this.MinimumCaptionLengthMs = minimumCaptionLengthMs;
            this.MinimumGapBetweenCaptionsMs = minimumGapBetweenCaptionsMs;
            this.MinimumMergeGapInterval = minimumMergeGapInterval;
            this.QtSeamless = qtSeamless;
            this.SilenceMaxMs = silenceMaxMs;
            this.SingleSpeakerPerCaption = singleSpeakerPerCaption;
            this.SoundThreshold = soundThreshold;
            this.SoundTokensByCaption = soundTokensByCaption;
            this.SoundTokensByLine = soundTokensByLine;
            this.SoundTokensByCaptionList = soundTokensByCaptionList;
            this.SoundTokensByLineList = soundTokensByLineList;
            this.SpeakerOnNewLine = speakerOnNewLine;
            this.SrtFormat = srtFormat;
            this.StripSquareBrackets = stripSquareBrackets;
            this.Utf8Mark = utf8_mark;
        }
    }
}
