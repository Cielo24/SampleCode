<?php

require_once("ActionsTest.php");

class AccessTest extends ActionsTest {
        
    public function testLoginPasswordNoHeaders() {
        // Username, password, no headers
        $this->apiToken = $this->actions->login($this->username, $this->password, false);
        $this->assertEquals(32, strlen($this->apiToken));
    }

    public function testLoginPasswordHeaders() {
        // Username, password, headers
        $this->apiToken = $this->actions->login($this->username, $this->password, true);
        $this->assertEquals(32, strlen($this->apiToken));
    }

    public function testLoginSecureKeyNoHeaders() {
        // Username, secure key, no headers
        $this->apiToken = $this->actions->login($this->username, $this->secureKey, false);
        $this->assertEquals(32, strlen($this->apiToken));
    }

    public function testLoginSecureKeyHeaders() {
        // Username, secure key, headers
        $this->apiToken = $this->actions->login($this->username, $this->secureKey, true);
        $this->assertEquals(32, strlen($this->apiToken));
    }

    public function testLogout() {
        // Logout
        $this->actions->logout($this->apiToken);
        $this->apiToken = null;
    }

    public function testGenerateApiKey() {
        $this->secureKey = $this->actions->generateAPIKey($this->apiToken, $this->username, false);
        $this->assertEquals(32, strlen($this->secureKey));
    }

    public function testGenerateApiKeyForceNew() {
        $this->secureKey = $this->actions->generateAPIKey($this->apiToken, $this->username, true);
        $this->assertEquals(32, strlen($this->secureKey));
        $this->actions->removeAPIKey($this->apiToken, $this->secureKey);
    }

    public function testRemoveApiKey() {
        $this->actions->removeAPIKey($this->apiToken, $this->secureKey);
        $this->secureKey = null;
    }

    public function testUpdatePassword() {
        $this->actions->UpdatePassword($this->apiToken, $this->newPassword);
        $this->actions->UpdatePassword($this->apiToken, $this->password);
    }
}