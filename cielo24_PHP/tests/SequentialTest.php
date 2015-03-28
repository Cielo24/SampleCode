<?php

require_once("../src/cielo24/Enums.php");
require_once("Config.php");
require_once("ActionsTest.php");

class SequentialTest extends ActionsTest {

    protected $jobId = null;

    public function setUp()
    {
        $this->config = new Config();
        $this->actions = new Actions($this->config->serverUrl);
    }

    public function testSequence()
    {
        // Login, generate API key, logout
        $this->apiToken = $this->actions->login($this->config->username, $this->config->password);
        $this->secureKey = $this->actions->generateAPIKey($this->apiToken, $this->config->username, true);
        $this->actions->logout($this->apiToken);
        $this->apiToken = null;

        // Login using API key
        $this->apiToken = $this->actions->login($this->config->username, null, $this->secureKey);

        // Create a job using a media URL
        $this->jobId = $this->actions->createJob($this->apiToken, "PHP_test_job")["JobId"];
        $this->actions->addMediaToJobUrl($this->apiToken, $this->jobId, $this->config->sampleVideoUri);

        // Assert JobList and JobInfo data
        $job_list = $this->actions->getJobList($this->apiToken);
        $this->assertTrue($this->_containsJob($this->jobId, $job_list), "JobId not found in JobList");
        $job = $this->actions->getJobInfo($this->apiToken, $this->jobId);
        $this->assertEquals($this->jobId, $job["JobId"], "Wrong JobId found in JobInfo");

        // Logout
        $this->actions->logout($this->apiToken);
        $this->apiToken = null;

        // Login/logout/change password
        $this->apiToken = $this->actions->login($this->config->username, $this->config->password);
        $this->actions->updatePassword($this->apiToken, $this->config->newPassword);
        $this->actions->logout($this->apiToken);
        $this->apiToken = null;

        // Change password back
        $this->apiToken = $this->actions->login($this->config->username, $this->config->newPassword);
        $this->actions->updatePassword($this->apiToken, $this->config->password);
        $this->actions->logout($this->apiToken);
        $this->apiToken = null;

        // Login using API key
        $this->apiToken = $this->actions->login($this->config->username, null, $this->secureKey);

        // Delete job and assert JobList data
        $this->actions->deleteJob($this->apiToken, $this->jobId);
        $job_list2 = $this->actions->getJobList($this->apiToken);
        $this->assertFalse($this->_containsJob($this->jobId, $job_list2), "JobId should not be in JobList");

        // Delete current API key and try to re-login (should fail)
        $this->actions->removeAPIKey($this->apiToken, $this->secureKey);
        $this->actions->logout($this->apiToken);
        $this->apiToken = null;

        try
        {
            $this->apiToken = $this->actions->login($this->config->username, null, $this->secureKey);
            $this->fail("Should not be able to login using invalid API key");
        }
        catch (WebError $e)
        {
            $this->assertEquals(ErrorType::ACCOUNT_UNPRIVILEGED, $e->errorType, "Unexpected error type");
        }
    }

    private function _containsJob($job_id, $list)
    {
        foreach($list["ActiveJobs"] as $j)
        {
            if($j["JobId"] === ($job_id))
            {
                return true;
            }
        }
        return false;
    }
}