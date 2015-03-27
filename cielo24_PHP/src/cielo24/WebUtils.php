<?php

use Httpful\Request;

class WebUtils {
    const BASIC_TIMEOUT = 60;           # seconds
    const DOWNLOAD_TIMEOUT = 300;       # seconds
    const UPLOAD_TIMEOUT = 604800;      # seconds (7 days)

    public static function getJson($base_uri, $path, $method, $timeout, $query=array(), $headers=array(), $body=null) {
        $response = WebUtils::httpRequest($base_uri, $path, $method, $timeout, $query, $headers, $body);
        return json_decode($response, true);
    }

    public static function httpRequest($base_uri, $path, $method, $timeout, $query=array(), $headers=array(), $body=null, $file=null) {
        if ($query == null){
            $query = array();
        }
        if ($headers == null) {
            $headers = array();
        }

        $url = $base_uri . $path;
        if (count($query) > 0) {
            $url .= "?" . http_build_query($query);
        }
        $http_request = Request::init();
        $http_request->uri($url)
                     ->method($method)
                     ->addHeaders($headers)
                     ->body($body)
                     ->timeout($timeout);

        $response = $http_request->send();

        if (!$response->hasErrors()) {
            return $response->$body;
        } else {
            $json = json_decode($response->$body, true);
            throw new WebError($json["ErrorType"], $json["ErrorComment"]);
        }
    }
}

class WebError extends Exception {

    public $errorType;
    public $errorComment;

    public function __construct($type, $comment) {
        parent::__construct();
        $this->errorType = $type;
        $this->errorComment = $comment;
    }

    public function __toString() {
        return $this->errorType . " - " . $this->errorComment;
    }
}