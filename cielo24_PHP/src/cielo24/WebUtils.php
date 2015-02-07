<?php

class WebUtils {
    const BASIC_TIMEOUT = 60;           # seconds
    const DOWNLOAD_TIMEOUT = 300;       # seconds
    const UPLOAD_TIMEOUT = 604800;      # seconds (7 days)

    public static function getJson($base_uri, $path, $method, $timeout, $query=array(), $headers=array(), $body=null) {
        $response = WebUtils::httpRequest($base_uri, $path, $method, $timeout, $query, $headers, $body);
        return json_decode($response->getBody(), true);
    }

    public static function httpRequest($base_uri, $path, $method, $timeout, $query=array(), $headers=array(), $body=null) {
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
        $http_request = new HttpRequest($url, $method, array("timeout" => $timeout));
        $http_request->setHeaders($headers);
        $http_request->setBody($body);
        $response = $http_request->send();

        if ($response->getResponseCode() == 200 or $response->getResponseCode() == 204) {
            return $response->getBody();
        } else {
            $json = json_decode($response->getBody(), true);
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