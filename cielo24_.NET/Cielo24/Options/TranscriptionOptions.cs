using Cielo24.JSON;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cielo24.Options
{
    public class TranscriptOptions : CommonOptions
    {
        [QueryName("create_paragraphs")]
        public bool? CreateParagraphs { get; set; }
        [QueryName("newlines_after_paragraph")]
        public int? NewLinesAfterParagraph { get; set; }
        [QueryName("newlines_after_sentence")]
        public int? NewLinesAfterSentence { get; set; }
        [QueryName("timecode_every_paragraph")]
        public bool? TimeCodeEveryParagraph { get; set; }
        [QueryName("timecode_format")]
        public string TimeCodeFormat { get; set; }
        [QueryName("timecode_interval")]
        public int? TimeCodeInterval { get; set; }
        [QueryName("timecode_offset")]
        public int? TimeCodeOffset { get; set; }

        public TranscriptOptions(DateTime? elementListVersion = null,
                                 string speakerChangeToken = null,
                                 bool? maskProfanity = null,
                                 bool? removeDisfluencies = null,
                                 List<Tag> removeSoundsList = null,
                                 bool? removeSoundReferences = null,
                                 bool? replaceSlang = null,
                                 char[] soundBoundaries = null,
                                 bool? createParagraphs = null,
                                 int? newLinesAfterParagraph = null,
                                 int? newLinesAfterSentence = null,
                                 bool? timecodeEveryParagraph = null,
                                 string timecodeFormat = null,
                                 int? timecodeInterval = null,
                                 int? timecodeOffset = null)
            : base(elementListVersion, speakerChangeToken, maskProfanity, removeDisfluencies, removeSoundsList, removeSoundReferences, replaceSlang, soundBoundaries)
        {
            this.CreateParagraphs = createParagraphs;
            this.NewLinesAfterParagraph = newLinesAfterParagraph;
            this.NewLinesAfterSentence = newLinesAfterSentence;
            this.TimeCodeEveryParagraph = timecodeEveryParagraph;
            this.TimeCodeFormat = timecodeFormat;
            this.TimeCodeInterval = timecodeInterval;
            this.TimeCodeOffset = timecodeOffset;
        }
    }
}
