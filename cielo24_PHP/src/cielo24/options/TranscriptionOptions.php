<?php

require_once("CommonFormattingOptions.php");

class TranscriptOptions extends CommonFormattingOptions
{
    public $create_paragraphs;
    public $newlines_after_paragraph;
    public $newlines_after_sentence;
    public $timecode_every_paragraph;
    public $timecode_format;
    public $timecode_interval;
    public $timecode_offset;

                                // Common Options
    public function __construct(DateTime $elementListVersion = null,
                                $speakerChangeToken = null,
                                $maskProfanity = null,
                                $removeDisfluencies = null,
                                array $removeSoundsList = null,
                                $removeSoundReferences = null,
                                $replaceSlang = null,
                                array $soundBoundaries = null,
                                // Transcription Options
                                $createParagraphs = null,
                                $newLinesAfterParagraph = null,
                                $newLinesAfterSentence = null,
                                $timecodeEveryParagraph = null,
                                $timecodeFormat = null,
                                $timecodeInterval = null,
                                $timecodeOffset = null)
    {
        parent::__construct($elementListVersion,
                            $speakerChangeToken,
                            $maskProfanity,
                            $removeDisfluencies,
                            $removeSoundsList,
                            $removeSoundReferences,
                            $replaceSlang,
                            $soundBoundaries);

        $this->create_paragraphs = $createParagraphs;
        $this->newlines_after_paragraph = $newLinesAfterParagraph;
        $this->newlines_after_sentence = $newLinesAfterSentence;
        $this->timecode_every_paragraph = $timecodeEveryParagraph;
        $this->timecode_format = $timecodeFormat;
        $this->timecode_interval = $timecodeInterval;
        $this->timecode_offset = $timecodeOffset;
    }
}
