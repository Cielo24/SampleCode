# encoding: utf-8
from json import JSONDecoder
from os import fstat
from urllib import urlencode
from web_utils import WebUtils


class Actions(object):

    API_VERSION = 1
    LOGIN_PATH = "/api/account/login"
    LOGOUT_PATH = "/api/account/logout"
    UPDATE_PASSWORD_PATH = "/api/account/update_password"
    GENERATE_API_KEY_PATH = "/api/account/generate_api_key"
    REMOVE_API_KEY_PATH = "/api/account/remove_api_key"
    CREATE_JOB_PATH = "/api/job/new"
    AUTHORIZE_JOB_PATH = "/api/job/authorize"
    DELETE_JOB_PATH = "/api/job/del"
    GET_JOB_INFO_PATH = "/api/job/info"
    GET_JOB_LIST_PATH = "/api/job/list"
    ADD_MEDIA_TO_JOB_PATH = "/api/job/add_media"
    ADD_EMBEDDED_MEDIA_TO_JOB_PATH = "/api/job/add_media_url"
    GET_MEDIA_PATH = "/api/job/media"
    PERFORM_TRANSCRIPTION = "/api/job/perform_transcription"
    GET_TRANSCRIPT_PATH = "/api/job/get_transcript"
    GET_CAPTION_PATH = "/api/job/get_caption"
    GET_ELEMENT_LIST_PATH = "/api/job/get_elementlist"
    GET_LIST_OF_ELEMENT_LISTS_PATH = "/api/job/list_elementlists"

    def __init__(self, base_url="https://api.cielo24.com"):
        self.base_url = base_url

    ### ACCESS CONTROL ###

    def login(self, username, password=None, api_securekey=None, use_headers=False):
        self.__assert_argument(username, "Username")
        # Password or API Secure Key must be supplied but not both
        if password is None and api_securekey is None:
            raise ValueError("Password or API Secure Key must be supplied for login.")

        query_dict = self.__init_version_dict()
        headers = dict()

        if use_headers:
            headers['x-auth-user'] = username
            if password is not None:
                headers['x-auth-key'] = password
            if api_securekey is not None:
                headers['x-auth-securekey'] = api_securekey
        else:
            query_dict['username'] = username
            if password is not None:
                query_dict['password'] = password
            if api_securekey is not None:
                query_dict['securekey'] = api_securekey

        response = WebUtils.get_json(self.base_url, self.LOGIN_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict, headers)
        return response['ApiToken']

    def logout(self, api_token):
        query_dict = self.__init_access_req_dict(api_token)
        # Nothing returned
        WebUtils.http_request(self.base_url, self.LOGOUT_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)

    def update_password(self, api_token, new_password):
        self.__assert_argument(new_password, "New Password")
        query_dict = self.__init_access_req_dict(api_token)
        query_dict['new_password'] = new_password
        # Nothing returned
        WebUtils.http_request(self.base_url, self.UPDATE_PASSWORD_PATH, 'POST', WebUtils.BASIC_TIMEOUT, None, None, urlencode(query_dict))

    def generate_api_key(self, api_token, username, force_new=False):
        self.__assert_argument(username, "Username")
        query_dict = self.__init_access_req_dict(api_token)
        query_dict['account_id'] = username
        query_dict['force_new'] = force_new

        response = WebUtils.get_json(self.base_url, self.GENERATE_API_KEY_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)
        return response["ApiKey"]

    def remove_api_key(self, api_token, api_securekey):
        self.__assert_argument(api_securekey, "API Secure Key")
        query_dict = self.__init_access_req_dict(api_token)
        query_dict['api_securekey'] = api_securekey
        # Nothing returned
        WebUtils.http_request(self.base_url, self.REMOVE_API_KEY_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)

    ### JOB CONTROL ###

    def create_job(self, api_token, job_name=None, language="en", external_id=None, sub_account=None):
        self.__assert_argument(language, "Language")
        query_dict = self.__init_access_req_dict(api_token)

        query_dict['language'] = language
        if job_name is not None:
            query_dict['job_name'] = job_name
        if external_id is not None:
            query_dict['external_id'] = external_id
        if sub_account is not None:  # username parameter named sub_account for clarity
            query_dict['username'] = sub_account

        response = WebUtils.get_json(self.base_url, self.CREATE_JOB_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)
        # Return a hash with JobId and TaskId
        return response

    def authorize_job(self, api_token, job_id):
        query_dict = self.__init_job_req_dict(api_token, job_id)
        # Nothing returned
        WebUtils.http_request(self.base_url, self.AUTHORIZE_JOB_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)

    def delete_job(self, api_token, job_id):
        query_dict = self.__init_job_req_dict(api_token, job_id)
        response = WebUtils.get_json(self.base_url, self.DELETE_JOB_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)
        return response["TaskId"]

    def get_job_info(self, api_token, job_id):
        query_dict = self.__init_job_req_dict(api_token, job_id)
        response = WebUtils.get_json(self.base_url, self.GET_JOB_INFO_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)
        return response

    def get_job_list(self, api_token, options=None):
        query_dict = self.__init_access_req_dict(api_token)
        if options is not None:
            query_dict.update(options.get_dict())
        response = WebUtils.get_json(self.base_url, self.GET_JOB_LIST_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)
        return response

    def add_media_to_job_file(self, api_token, job_id, media_file):
        self.__assert_argument(media_file, "Media File")
        query_dict = self.__init_job_req_dict(api_token, job_id)
        file_size = fstat(media_file.fileno()).st_size
        response = WebUtils.get_json(self.base_url, self.ADD_MEDIA_TO_JOB_PATH, 'POST', WebUtils.UPLOAD_TIMEOUT, query_dict, {'Content-Type': 'video/mp4', 'Content-Length': file_size}, media_file)
        return response["TaskId"]

    def add_media_to_job_url(self, api_token, job_id, media_url):
        return self.__send_media_url(api_token, job_id, media_url, self.ADD_MEDIA_TO_JOB_PATH)

    def add_media_to_job_embedded(self, api_token, job_id, media_url):
        return self.__send_media_url(api_token, job_id, media_url, self.ADD_EMBEDDED_MEDIA_TO_JOB_PATH)

    def get_media(self, api_token, job_id):
        query_dict = self.__init_job_req_dict(api_token, job_id)
        response = WebUtils.get_json(self.base_url, self.GET_MEDIA_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)
        return response["MediaUrl"]

    def perform_transcription(self,
                              api_token,
                              job_id,
                              fidelity,
                              priority=None,
                              callback_url=None,
                              turnaround_hours=None,
                              target_language=None,
                              options=None):
        self.__assert_argument(fidelity, "Fidelity")
        query_dict = self.__init_job_req_dict(api_token, job_id)
        query_dict['transcription_fidelity'] = fidelity
        if priority is not None:
            query_dict['priority'] = priority
        if callback_url is not None:
            query_dict['callback_url'] = callback_url
        if turnaround_hours is not None:
            query_dict['turnaround_hours'] = turnaround_hours
        if target_language is not None:
            query_dict['target_language'] = target_language
        if options is not None:
            query_dict.update(options.get_dict())

        response = WebUtils.get_json(self.base_url, self.PERFORM_TRANSCRIPTION, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)
        return response["TaskId"]

    def get_transcript(self, api_token, job_id, transcript_options=None):
        query_dict = self.__init_job_req_dict(api_token, job_id)
        if transcript_options is not None:
            query_dict.update(transcript_options.get_dict())
        # Returns raw transcript text
        return WebUtils.http_request(self.base_url, self.GET_TRANSCRIPT_PATH, 'GET', WebUtils.DOWNLOAD_TIMEOUT, query_dict)

    def get_caption(self, api_token, job_id, caption_format, caption_options=None):
        self.__assert_argument(caption_format, "Caption Format")
        query_dict = self.__init_job_req_dict(api_token, job_id)
        query_dict['caption_format'] = caption_format
        if caption_options is not None:
            query_dict.update(caption_options.get_dict())

        response = WebUtils.http_request(self.base_url, self.GET_CAPTION_PATH, 'GET', WebUtils.DOWNLOAD_TIMEOUT, query_dict)
        if (caption_options is not None) and caption_options.build_url:  # If build_url is true
            return JSONDecoder().decode(response)["CaptionUrl"]  # Return Caption URL
        else:
            return response  # Else return raw caption text

    def get_element_list(self, api_token, job_id, elementlist_version=None):
        query_dict = self.__init_job_req_dict(api_token, job_id)
        if elementlist_version is not None:
            query_dict['elementlist_version'] = elementlist_version

        response = WebUtils.get_json(self.base_url, self.GET_ELEMENT_LIST_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)
        return response

    def get_list_of_element_lists(self, api_token, job_id):
        query_dict = self.__init_job_req_dict(api_token, job_id)
        response = WebUtils.get_json(self.base_url, self.GET_LIST_OF_ELEMENT_LISTS_PATH, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)
        return response

    ### PRIVATE HELPER METHODS ###

    def __send_media_url(self, api_token, job_id, media_url, path):
        self.__assert_argument(media_url, "Media URL")
        query_dict = self.__init_job_req_dict(api_token, job_id)
        query_dict['media_url'] = media_url
        response = WebUtils.get_json(self.base_url, path, 'GET', WebUtils.BASIC_TIMEOUT, query_dict)
        return response["TaskId"]

    def __init_job_req_dict(self, api_token, job_id):
        self.__assert_argument(job_id, "Job ID")
        return dict(self.__init_access_req_dict(api_token).items() + {'job_id': job_id}.items())

    def __init_access_req_dict(self, api_token):
        self.__assert_argument(api_token, "API Token")
        return dict(self.__init_version_dict().items() + {'api_token': api_token}.items())

    def __init_version_dict(self):
        return {'v': self.API_VERSION}

    def __assert_argument(self, arg, arg_name):
        if arg is None:
            raise ValueError("Invalid argument - " + arg_name)