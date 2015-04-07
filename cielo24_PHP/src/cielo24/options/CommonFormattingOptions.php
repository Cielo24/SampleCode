<?php

require_once("BaseOptions.php");

/* Options found in both Transcript and Caption options
 * All of the option properties are nullable. Properties that are null are ignored by the toQuery() method
 * and are not part of the resulting query string.
 */
abstract class CommonFormattingOptions extends BaseOptions
{
    public $elementlist_version;
    public $emit_speaker_change_token_as;
    public $mask_profanity;
    public $remove_disfluencies;
    public $remove_sounds_list;
    public $remove_sound_references;
    public $replace_slang;
    public $sound_boundaries;

    public function __construct(DateTime $elementListVersion = null,
                                $speakerChangeToken = null,
                                $maskProfanity = null,
                                $removeDisfluencies = null,
                                array $removeSoundsList = null,
                                $removeSoundReferences = null,
                                $replaceSlang = null,
                                array $soundBoundaries = null)
    {
        $this->elementlist_version = $elementListVersion;
        $this->emit_speaker_change_token_as = $speakerChangeToken;
        $this->mask_profanity = $maskProfanity;
        $this->remove_disfluencies = $removeDisfluencies;
        $this->remove_sounds_list = $removeSoundsList;
        $this->remove_sound_references = $removeSoundReferences;
        $this->replace_slang = $replaceSlang;
        $this->sound_boundaries = $soundBoundaries;
    }
}