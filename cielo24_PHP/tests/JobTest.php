<?php

require_once("ActionsTest.php");
require_once("../src/cielo24/options/CaptionOptions.php");
require_once("../src/cielo24/Enums.php");

class JobTest extends ActionsTest
{
    private $jobId = null;
    private $taskId = null;
    private $sampleVideoUri = "http://techslides.com/demos/sample-videos/small.mp4";
    private $sampleVideoFilePath = "C:\\path\\to\\file.mp4";

    public function setUp()
    {
        parent::setUp();
        // Always start with a fresh job
        $this->jobId = $this->actions->createJob($this->apiToken)["JobId"];
    }

    public function testOptions()
    {
        // TODO
        //$options = new CaptionOptions();
        //$options->caption_by_sentence = true;
        //$options->force_case = TextCase::UPPER;
        //$this->assertEquals("build_url=true&caption_by_sentence=true&dfxp_header=header&force_case=upper", options . ToQuery() . ToLower());
    }


    public function testCreateJob()
    {
        $result = $this->actions->createJob($this->apiToken, "test_name", "en");
        $this->assertEquals(32, strlen($result["JobId"]));
        $this->assertEquals(32, strlen($result["TaskId"]));
    }


    public function testAuthorizeJob()
    {
        $this->actions->authorizeJob($this->apiToken, $this->jobId);
    }


    public function testDeleteJob()
    {
        $this->taskId = $this->actions->deleteJob($this->apiToken, $this->jobId);
        $this->assertEquals(32, strlen($this->taskId));
    }

    public function testGetJobInfo()
    {
        $info = $this->actions->getJobInfo($this->apiToken, $this->jobId);
    }

    public function testGetJobList()
    {
        $list = $this->actions->getJobList($this->apiToken);
    }

    public function testGetElementList()
    {
        $list = $this->actions->getElementList($this->apiToken, $this->jobId);
    }

    public function testGetListOfElementLists()
    {
        $list = $this->actions->getListOfElementLists($this->apiToken, $this->jobId);
    }

    public function testGetMedia()
    {
        // Add media to job first
        $this->actions->addMediaToJob($this->apiToken, $this->jobId, $this->sampleVideoUri);
        // Test get media
        $uri = $this->actions->getMedia($this->apiToken, $this->jobId);
    }

    public function testGetTranscript()
    {
        $this->actions->getTranscript($this->apiToken, $this->jobId);
    }

    public function testGetCaption()
    {
        $this->actions->getCaption($this->apiToken, $this->jobId, CaptionFormat::SRT);
    }

    public function testGetCaptionBuildUrl()
    {
        $options = new CaptionOptions();
        $options->build_url = true;
        $response = $this->actions->getCaption($this->apiToken, $this->jobId, CaptionFormat::SRT, $options);
        if(!filter_var($response, FILTER_VALIDATE_URL)){
            $this->fail("Did not receive a URL back.");
        }
    }

    public function testPerformTranscription()
    {
        $this->actions->addMediaToJob($this->apiToken, $this->jobId, $this->sampleVideoUri);
        $this->taskId = $this->actions->performTranscription($this->apiToken, $this->jobId, Fidelity::PREMIUM, Priority::STANDARD);
        $this->assertEquals(32, strlen($this->taskId));
    }

    public function testAddMediaToJobUrl()
    {
        $this->taskId = $this->actions->addMediaToJob($this->apiToken, $this->jobId, $this->sampleVideoUri);
        $this->assertEquals(32, strlen($this->taskId));
    }

    public function testAddMediaToJobEmbedded()
    {
        $this->taskId = $this->actions->addEmbeddedMediaToJob($this->apiToken, $this->jobId, $this->sampleVideoUri);
        $this->assertEquals(32, strlen($this->taskId));
    }

    public function testAddMediaToJobFile()
    {
        // TODO
        //FileStream fs = new FileStream($this->sampleVideoFilePath, FileMode . Open);
        //$this->taskId = $this->actions->addMediaToJob($this->apiToken, $this->jobId, fs);
        //$this->assertEquals(32, strlen($this->taskId));
    }
}