<?php

require_once("ActionsTest.php");
require_once("../src/cielo24/options/CaptionOptions.php");
require_once("../src/cielo24/Enums.php");

class JobTest extends ActionsTest {

    private $jobId = null;
    private $taskId = null;

    public function setUp()
    {
        parent::setUp();
        // Always start with a fresh job
        $this->jobId = $this->actions->createJob($this->apiToken, "PHP_test_job")["JobId"];
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
        $this->actions->addMediaToJobUrl($this->apiToken, $this->jobId, $this->config->sampleVideoUri);
        // Test get media
        $uri = $this->actions->getMedia($this->apiToken, $this->jobId);
        if (!filter_var($uri, FILTER_VALIDATE_URL)) {
            $this->fail("Did not receive a URL back.");
        }
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
        if (!filter_var($response, FILTER_VALIDATE_URL)) {
            $this->fail("Did not receive a URL back.");
        }
    }

    public function testPerformTranscription()
    {
        $this->actions->addMediaToJobUrl($this->apiToken, $this->jobId, $this->config->sampleVideoUri);
        $this->taskId = $this->actions->performTranscription($this->apiToken, $this->jobId, Fidelity::PREMIUM, Priority::STANDARD);
        $this->assertEquals(32, strlen($this->taskId));
    }

    public function testAddMediaToJobUrl()
    {
        $this->taskId = $this->actions->addMediaToJobUrl($this->apiToken, $this->jobId, $this->config->sampleVideoUri);
        $this->assertEquals(32, strlen($this->taskId));
    }

    public function testAddMediaToJobEmbedded()
    {
        $this->taskId = $this->actions->addMediaToJobEmbedded($this->apiToken, $this->jobId, $this->config->sampleVideoUri);
        $this->assertEquals(32, strlen($this->taskId));
    }

    public function testAddMediaToJobFile()
    {
        $this->taskId = $this->actions->addMediaToJobFile($this->apiToken, $this->jobId, $this->config->sampleVideoFilePath);
        $this->assertEquals(32, strlen($this->taskId));
    }
}