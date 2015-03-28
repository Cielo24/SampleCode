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
        if ($this->apiToken == null) {
            $this->apiToken = $this->actions->login($this->config->username, $this->config->password, true);
        }
        if ($this->secureKey == null) {
            $this->secureKey = $this->actions->generateAPIKey($this->apiToken, $this->config->username, true);
        }
    }
}