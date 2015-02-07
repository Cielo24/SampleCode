<?php

require_once("../src/cielo24/Actions.php");

class ActionsTest extends PHPUnit_Framework_TestCase {

    protected $actions;
    protected $username = "api_test";
    protected $password = "api_test";
    protected $newPassword = "api_test_new";
    protected $apiToken = null;
    protected $secureKey = null;

    public function setUp() {
        $this->actions = new Actions();
        $this->actions->BASE_URL = "http://sandbox-dev.cielo24.com";
        if ($this->apiToken == null) {
            $this->apiToken = $this->actions->login($this->username, $this->password, true);
        }
        if ($this->secureKey == null) {
            $this->secureKey = $this->actions->generateAPIKey($this->apiToken, $this->username, true);
        }
    }
}