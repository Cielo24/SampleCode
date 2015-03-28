<?php

require_once("ActionsTest.php");

class AccessTest extends ActionsTest
{

    public function testLoginPasswordNoHeaders()
    {
        // Username, password, no headers
        $this->apiToken = $this->actions->login($this->config->username, $this->config->password, null, false);
        $this->assertEquals(32, strlen($this->apiToken));
    }

    public function testLoginPasswordHeaders()
    {
        // Username, password, headers
        $this->apiToken = $this->actions->login($this->config->username, $this->config->password, null, true);
        $this->assertEquals(32, strlen($this->apiToken));
    }

    public function testLoginSecureKeyNoHeaders()
    {
        // Username, secure key, no headers
        $this->apiToken = $this->actions->login($this->config->username, null, $this->secureKey, false);
        $this->assertEquals(32, strlen($this->apiToken));
    }

    public function testLoginSecureKeyHeaders()
    {
        // Username, secure key, headers
        $this->apiToken = $this->actions->login($this->config->username, null, $this->secureKey, true);
        $this->assertEquals(32, strlen($this->apiToken));
    }

    public function testLogout()
    {
        // Logout
        $this->actions->logout($this->apiToken);
        $this->apiToken = null;
    }

    public function testGenerateApiKeyForceNew()
    {
        $this->secureKey = $this->actions->generateAPIKey($this->apiToken, $this->config->username, true);
        $this->assertEquals(32, strlen($this->secureKey));
    }

    public function testGenerateApiKeyNotForceNew()
    {
        $this->secureKey = $this->actions->generateAPIKey($this->apiToken, $this->config->username, false);
        $this->assertEquals(32, strlen($this->secureKey));
    }

    public function testRemoveApiKey()
    {
        $this->actions->removeAPIKey($this->apiToken, $this->secureKey);
        $this->secureKey = null;
    }

    public function testUpdatePassword()
    {
        $this->actions->UpdatePassword($this->apiToken, $this->config->newPassword);
        $this->actions->UpdatePassword($this->apiToken, $this->config->password);
    }
}