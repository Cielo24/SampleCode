<?php

require_once("WebUtils.php");

class Actions {

    public $BASE_URL = "https://api.cielo24.com";
    const API_VERSION = 1;

    const LOGIN_PATH = "/api/account/login";
    const LOGOUT_PATH = "/api/account/logout";
    const UPDATE_PASSWORD_PATH = "/api/account/update_password";
    const GENERATE_API_KEY_PATH = "/api/account/generate_api_key";
    const REMOVE_API_KEY_PATH = "/api/account/remove_api_key";
    const CREATE_JOB_PATH = "/api/job/new";
    const AUTHORIZE_JOB_PATH = "/api/job/authorize";
    const DELETE_JOB_PATH = "/api/job/del";
    const GET_JOB_INFO_PATH = "/api/job/info";
    const GET_JOB_LIST_PATH = "/api/job/list";
    const ADD_MEDIA_TO_JOB_PATH = "/api/job/add_media";
    const ADD_EMBEDDED_MEDIA_TO_JOB_PATH = "/api/job/add_media_url";
    const GET_MEDIA_PATH = "/api/job/media";
    const PERFORM_TRANSCRIPTION = "/api/job/perform_transcription";
    const GET_TRANSCRIPT_PATH = "/api/job/get_transcript";
    const GET_CAPTION_PATH = "/api/job/get_caption";
    const GET_ELEMENT_LIST_PATH = "/api/job/get_elementlist";
    const GET_LIST_OF_ELEMENT_LISTS_PATH = "/api/job/list_elementlists";

    public function __construct() { }

    public function __call($name, $arguments) {
        // TODO
    }

    /// ACCESS CONTROL ///

    /* Performs a Login action. If useHeaders is true, puts username and password into HTTP headers */
    public function login($username, $password = null, $api_securekey = null, $use_headers = false) {
        $this->_assertArgument($username, "Username");

        # Password or API Secure Key must be supplied but not both
        if ($password == null and $api_securekey == null) {
            throw new InvalidArgumentException("Password or API Secure Key must be supplied for login.");
        }

        $query_dict = $this->_initVersionDict();
        $headers = array();

        if ($use_headers) {
            $headers["x-auth-user"] = $username;
            if ($password != null) {
                $headers["x-auth-key"] = $password;
            }
            if ($api_securekey != null) {
                $headers["x-auth-securekey"] = $api_securekey;
            }
        } else {
            $query_dict["username"] = $username;
            if ($password != null) {
                $query_dict["password"] = $password;
            }
            if ($api_securekey != null) {
                $query_dict["securekey"] = $api_securekey;
            }
        }

        $response = WebUtils::getJson($this->BASE_URL, Actions::LOGIN_PATH, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict, $headers);
        return $response["ApiToken"];
    }

    /* Performs a Logout action */
    public function logout($api_token) {
        $query_dict = $this->_initAccessReqDict($api_token);
        // Nothing returned
        WebUtils::httpRequest($this->BASE_URL, Actions::LOGOUT_PATH, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
    }

    /* Updates password */
    public function updatePassword($api_token, $new_password) {
        $this->_assertArgument($new_password, "New Password");

        $query_dict = $this->_initAccessReqDict($api_token);
        $query_dict["new_password"] = $new_password;
        // Nothing returned
        WebUtils::httpRequest($this->BASE_URL, Actions::UPDATE_PASSWORD_PATH, HTTP_METH_POST, WebUtils::BASIC_TIMEOUT, null, null, http_build_query($query_dict));
    }

    /* Returns a new Secure API key */
    public function generateAPIKey($api_token, $username, $force_new = false) {
        $this->_assertArgument($username, "Username");

        $query_dict = $this->_initAccessReqDict($api_token);
        $query_dict["account_id"] = $username;
        $query_dict["force_new"] = ($force_new) ? 'true' : 'false';

        $response = WebUtils::getJson($this->BASE_URL, Actions::GENERATE_API_KEY_PATH, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
        return $response["ApiKey"];
    }

    /* Deactivates the supplied Secure API key */
    public function removeAPIKey($api_token, $api_securekey) {
        $query_dict = $this->_initAccessReqDict($api_token);
        $query_dict["api_securekey"] = $api_securekey;
        // Nothing returned
        WebUtils::httpRequest($this->BASE_URL, Actions::REMOVE_API_KEY_PATH, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
    }

    /// JOB CONTROL ///

    /* Creates a new job. Returns an array of Guids where 'JobId' is the 0th element and 'TaskId' is the 1st element */
    public function createJob($api_token, $job_name = null, $language = "en") {
        $query_dict = $this->_initAccessReqDict($api_token);
        if($job_name) {
            $query_dict["job_name"] = $job_name;
        }
        $query_dict["language"] = ($language == null) ? "en" : $language;

        $response = WebUtils::getJson($this->BASE_URL, Actions::CREATE_JOB_PATH, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
        // Return a hash with JobId and TaskId
        return $response;
    }

    /* Authorizes a job with job_id */
    public function authorizeJob($api_token, $job_id) {
        $query_dict = $this->_initJobReqDict($api_token, $job_id);
        // Nothing returned\
        WebUtils::httpRequest($this->BASE_URL, Actions::AUTHORIZE_JOB_PATH, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
    }

    /* Deletes a job with job_id */
    public function deleteJob($api_token, $job_id) {
        $query_dict = $this->_initJobReqDict($api_token, $job_id);
        $response = WebUtils::getJson($this->BASE_URL, Actions::DELETE_JOB_PATH, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
        return $response["TaskId"];
    }

    /* Gets information about a job with job_id */
    public function getJobInfo($api_token, $job_id) {
        $query_dict = $this->_initJobReqDict($api_token, $job_id);
        $response = WebUtils::getJson($this->BASE_URL, Actions::GET_JOB_INFO_PATH, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
        return $response;
    }

    /* Gets a list of jobs */
    public function getJobList($api_token) {
        $query_dict = $this->_initAccessReqDict($api_token);
        $response = WebUtils::getJson($this->BASE_URL, Actions::GET_JOB_LIST_PATH, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
        return $response;
    }

    /* Uploads a file from fileStream to job with job_id */
    public function addMediaToJobFile($api_token, $job_id, $file_stream) {


    }

    /* Provides job with job_id a url to media */
    public function addMediaToJobUrl($api_token, $job_id, $media_url) {
        return $this->_sendMediaUrl($api_token, $job_id, $media_url, Actions::ADD_MEDIA_TO_JOB_PATH);
    }

    /* Provides job with job_id a url to media */
    public function addMediaToJobEmbedded($api_token, $job_id, $media_url) {
        return $this->_sendMediaUrl($api_token, $job_id, $media_url, Actions::ADD_EMBEDDED_MEDIA_TO_JOB_PATH);
    }

    /* Helper method for AddMediaToJob and AddEmbeddedMediaToJob methods */
    private function _sendMediaUrl($api_token, $job_id, $media_url, $path) {
        $this->_assertArgument($media_url, "Media URL");
        $query_dict = $this->_initJobReqDict($api_token, $job_id);
        $query_dict['media_url'] = $media_url;

        $response = WebUtils::getJson($this->BASE_URL, $path, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
        return $response["TaskId"];
    }

    /* Returns a Uri to the media from job with job_id */
    public function getMedia($api_token, $job_id) {
        $query_dict = $this->_initJobReqDict($api_token, $job_id);
        $response = WebUtils::getJson($this->BASE_URL, Actions::GET_MEDIA_PATH, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
        return $response["MediaUrl"];
    }

    /* Makes a PerformTranscription call */
    public function performTranscription($api_token,
                                          $job_id,
                                          $fidelity,
                                          $priority,
                                          $callback_uri = null,
                                          $turnaround_hours = null,
                                          $target_language = null,
                                          $options = null) {
        $query_dict = $this->_initJobReqDict($api_token, $job_id);
        $query_dict["transcription_fidelity"] = $fidelity;
        $query_dict["priority"] = $priority;
		if ($callback_uri != null) {
            $query_dict["callback_url"] = $callback_uri;
        }
		if ($turnaround_hours != null) {
            $query_dict["turnaround_hours"] = $turnaround_hours;
        }
		if ($target_language != null) {
            $query_dict["target_language"] = $target_language;
        }
		if ($options != null) {
            $query_dict += $options->getDictionary();
        }

        $response = WebUtils::getJson($this->BASE_URL, Actions::PERFORM_TRANSCRIPTION, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
		return $response["TaskId"];
    }

    /* Returns a transcript from a job with job_id */
    public function getTranscript($api_token, $job_id, $transcript_options = null) {
        $query_dict = $this->_initJobReqDict($api_token, $job_id);
        if ($transcript_options != null) {
            $query_dict += $transcript_options->getDictionary();
        }
        # Return raw transcript text
        return WebUtils::httpRequest($this->BASE_URL, Actions::GET_TRANSCRIPT_PATH, HttpRequest::METH_GET, WebUtils::BASIC_TIMEOUT, $query_dict);
    }

    /* Returns a caption from a job with job_id OR if buildUri is true, returns a string representation of the uri */
    public function getCaption($api_token, $job_id, $caption_format, $caption_options = null) {
        $query_dict = $this->_initJobReqDict($api_token, $job_id);
        $query_dict['caption_format'] = $caption_format;
		if ($caption_options != null) {
            $query_dict += $caption_options->getDictionary();
        }

        $response = WebUtils::httpRequest($this->BASE_URL, Actions::GET_CAPTION_PATH, HttpRequest::METH_GET, WebUtils::DOWNLOAD_TIMEOUT, $query_dict);

		if ($caption_options != null && $caption_options->build_url != null && $caption_options->build_url) {
            $json = json_decode($response, true);
			return $json["CaptionUrl"];
		}

		return $response; // Caption text
    }

    /* Returns an element list */
    public function getElementList($api_token, $job_id, $element_list_version = null) {

    }

    /* Returns a list of elements lists */
    public function getListOfElementLists($api_token, $job_id) {

    }

    /// PRIVATE HELPER METHODS ///

    private function get_job_response($api_token, $job_id, $path) {
        return null;
    }

    /* Returns a dictionary with version, api_token and job_id key-value pairs (parameters used in almost every job-control action). */
    private function _initJobReqDict($api_token, $job_id) {
        $this->_assertArgument($api_token, "Job ID");
        $dict = $this->_initAccessReqDict($api_token);
        $dict["job_id"] = $job_id;
        return $dict;
    }

    /* Returns a dictionary with version and api_token key-value pairs (parameters used in almost every access-control action). */
    private function _initAccessReqDict($api_token) {
        $this->_assertArgument($api_token, "API Token");
        $dict = $this->_initVersionDict();
        $dict["api_token"] = $api_token;
        return $dict;
    }

    /* Returns a dictionary with version key-value pair (parameter used in every action). */
    private function _initVersionDict() {
        return array("v" => Actions::API_VERSION);
    }

    /* If arg is invalid (null or empty), throws an InvalidArgumentException */
    private function _assertArgument($arg, $arg_name) {
        if ($arg == null) { throw new InvalidArgumentException("Invalid " . $arg_name); }
        elseif (gettype($arg) == "string" and strlen($arg) == 0) { throw new InvalidArgumentException("Invalid " . $arg_name); }
    }
}