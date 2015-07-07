<?php

require_once("../src/cielo24/Actions.php");
require_once("Config.php");

class ActionsTest extends PHPUnit_Framework_TestCase
{
    protected $actions;
    protected $config;
    protected $apiToken = null;
    protected $secureKey = null;

    public function setUp()
    {
        $this->config = new Config();
        $this->actions = new Actions($this->config->serverUrl);
        // Start with a fresh session each time
        $this->apiToken = $this->actions->login($this->config->username, $this->config->password, true);
        $this->secureKey = $this->actions->generateAPIKey($this->apiToken, $this->config->username, true);
    }
}