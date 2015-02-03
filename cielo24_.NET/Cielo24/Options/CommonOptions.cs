using Cielo24.JSON;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cielo24.Options
{
    /* Options found in both Transcript and Caption options
     * All of the option properties are nullable. Properties that are null are ignored by the ToQuery() method
     * and are not part of the resulting query string. */
    public abstract class CommonOptions : BaseOptions
    {
        [QueryName("elementlist_version")]
        public DateTime? ElementListVersion { get; set; }
        [QueryName("emit_speaker_change_token_as")]
        public string SpeakerChangeToken { get; set; }
        [QueryName("mask_profanity")]
        public bool? MaskProfanity { get; set; }
        [QueryName("remove_disfluencies")]
        public bool? RemoveDisfluences { get; set; }
        [QueryName("remove_sounds_list")]
        public List<Tag> RemoveSoundsList { get; set; }
        [QueryName("remove_sound_references")]
        public bool? RemoveSoundReferences { get; set; }
        [QueryName("replace_slang")]
        public bool? ReplaceSlang { get; set; }
        [QueryName("sound_boundaries")]
        public char[] SoundBoundaries { get; set; }

        public CommonOptions(DateTime? elementListVersion = null,
                             string speakerChangeToken = null,
                             bool? maskProfanity = null,
                             bool? removeDisfluencies = null,
                             List<Tag> removeSoundsList = null,
                             bool? removeSoundReferences = null,
                             bool? replaceSlang = null,
                             char[] soundBoundaries = null)
        {
            this.ElementListVersion = elementListVersion;
            this.SpeakerChangeToken = speakerChangeToken;
            this.MaskProfanity = maskProfanity;
            this.RemoveDisfluences = removeDisfluencies;
            this.RemoveSoundsList = removeSoundsList;
            this.RemoveSoundReferences = removeSoundReferences;
            this.ReplaceSlang = replaceSlang;
            this.SoundBoundaries = soundBoundaries;
        }
    }
}