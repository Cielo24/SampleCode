<?php

use GuzzleHttp\Client;
use GuzzleHttp\Psr7\Request;
use GuzzleHttp\Exception\RequestException;

class WebUtils
{
    const BASIC_TIMEOUT = 60;           // seconds (1 minute)
    const DOWNLOAD_TIMEOUT = 300;       // seconds (5 minutes)
    const UPLOAD_TIMEOUT = 604800;      // seconds (1 week)

    public static function getJson($base_uri, $path, $method, $timeout, $query = array(), $headers = array(), $body = null)
    {
        $response = WebUtils::httpRequest($base_uri, $path, $method, $timeout, $query, $headers, $body);
        return json_decode($response, true);
    }

    public static function httpRequest($base_uri, $path, $method, $timeout, $query = array(), $headers = array(), $body = null)
    {
        if ($query == null) {
            $query = array();
        }
        if ($headers == null) {
            $headers = array();
        }

        $url = $base_uri . $path;
        // Append query to url if it's not empty
        $url .= (count($query) > 0) ? "?" . http_build_query($query) : "";

        $http_client = new Client(["timeout" => $timeout]);
        $http_request = new Request($method, $url, $headers, $body);

        try {
            $response = $http_client->send($http_request);
            return $response->getBody();
        } catch (RequestException $e) {
            $json = json_decode($e->getResponse()->getBody(), true);
            throw new WebError($json["ErrorType"], $json["ErrorComment"]);
        }
    }
}

class WebError extends Exception
{
    public $errorType;
    public $errorComment;

    public function __construct($type, $comment)
    {
        parent::__construct();
        $this->errorType = $type;
        $this->errorComment = $comment;
    }

    public function __toString()
    {
        return __CLASS__ . ": " . $this->errorType . " - " . $this->errorComment;
    }
}