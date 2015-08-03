<?php

require_once("BaseOptions.php");

class PerformTranscriptionOptions extends BaseOptions
{
    public $customer_approval_steps;
    public $customer_approval_tool;
    public $custom_metadata;
    public $generate_media_intelligence_for_iwp;
    public $notes;
    public $return_iwp;
    public $speaker_id;

    public function __construct($customerApprovalSteps = null,
                                $customerApprovalTool = null,
                                $customMetadata = null,
                                $generateMediaIntelligenceForIWP = null,
                                $notes = null,
                                array $returnIWP = null,
                                $speakerId = null)
    {
        $this->customer_approval_steps = $customerApprovalSteps;
        $this->customer_approval_tool = $customerApprovalTool;
        $this->custom_metadata = $customMetadata;
        $this->generate_media_intelligence_for_iwp = $generateMediaIntelligenceForIWP;
        $this->notes = $notes;
        $this->return_iwp = $returnIWP;
        $this->speaker_id = $speakerId;
    }
}