module Cielo24
  class Actions

    require 'uri'
    require 'hashie'
    require_relative 'web_utils'
    require_relative 'enums'
    require 'json'
    include Errno
    include Hashie
    include Cielo24

    attr_accessor :base_url

    API_VERSION = 1
    LOGIN_PATH = '/api/account/login'
    LOGOUT_PATH = '/api/account/logout'
    UPDATE_PASSWORD_PATH = '/api/account/update_password'
    GENERATE_API_KEY_PATH = '/api/account/generate_api_key'
    REMOVE_API_KEY_PATH = '/api/account/remove_api_key'
    CREATE_JOB_PATH = '/api/job/new'
    AUTHORIZE_JOB_PATH = '/api/job/authorize'
    DELETE_JOB_PATH = '/api/job/del'
    GET_JOB_INFO_PATH = '/api/job/info'
    GET_JOB_LIST_PATH = '/api/job/list'
    ADD_MEDIA_TO_JOB_PATH = '/api/job/add_media'
    ADD_EMBEDDED_MEDIA_TO_JOB_PATH = '/api/job/add_media_url'
    GET_MEDIA_PATH = '/api/job/media'
    PERFORM_TRANSCRIPTION = '/api/job/perform_transcription'
    GET_TRANSCRIPT_PATH = '/api/job/get_transcript'
    GET_CAPTION_PATH = '/api/job/get_caption'
    GET_ELEMENT_LIST_PATH = '/api/job/get_elementlist'
    GET_LIST_OF_ELEMENT_LISTS_PATH = '/api/job/list_elementlists'

    def initialize(base_url='https://api.cielo24.com')
      @base_url = base_url
    end

    ######################
    ### ACCESS CONTROL ###
    ######################

    def login(username, password=nil, api_securekey=nil, use_headers=false)
      assert_argument(username, 'Username')
      raise ArgumentError.new('Password or API Secure Key must be supplied for login.') if (password.nil? and api_securekey.nil?)

      query_hash = init_version_dict
      headers = Hash.new

      if use_headers
        headers[:'x-auth-user'] = username
        headers[:'x-auth-password'] = password unless password.nil?
        headers[:'x-auth-securekey'] = api_securekey unless api_securekey.nil?
      else
        query_hash[:username] = username
        query_hash[:password] = password unless password.nil?
        query_hash[:securekey] = api_securekey unless api_securekey.nil?
      end

      response = WebUtils.get_json(@base_url + LOGIN_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash, headers)
      return response['ApiToken']
    end

    def logout(api_token)
      query_hash = init_access_req_dict(api_token)
      # Nothing returned
      WebUtils.http_request(@base_url + LOGOUT_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
    end

    def update_password(api_token, new_password, sub_account=nil)
      assert_argument(new_password, 'New Password')
      query_hash = init_access_req_dict(api_token)
      query_hash[:new_password] = new_password
      # username parameter named sub_account for clarity
      query_hash[:username] = sub_account unless sub_account.nil?
      # Nothing returned
      WebUtils.http_request(@base_url + UPDATE_PASSWORD_PATH, 'POST', WebUtils::BASIC_TIMEOUT, nil, nil, query_hash)
    end

    def generate_api_key(api_token, username, force_new=false)
      assert_argument(username, 'Username')
      query_hash = init_access_req_dict(api_token)
      query_hash[:account_id] = username
      query_hash[:force_new] = force_new
      response = WebUtils.get_json(@base_url + GENERATE_API_KEY_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
      return response['ApiKey']
    end

    def remove_api_key(api_token, api_securekey)
      assert_argument(api_securekey, 'API Secure Key')
      query_hash = init_access_req_dict(api_token)
      query_hash[:api_securekey] = api_securekey
      # Nothing returned
      WebUtils.http_request(@base_url + REMOVE_API_KEY_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
    end

    ###################
    ### JOB CONTROL ###
    ###################

    def create_job(api_token, job_name=nil, language=Language::ENGLISH, external_id=nil, sub_account=nil)
      query_hash = init_access_req_dict(api_token)
      query_hash[:job_name] = job_name unless job_name.nil?
      query_hash[:language] = language unless language.nil?
      query_hash[:external_id] = external_id unless external_id.nil?
      # username parameter named sub_account for clarity
      query_hash[:username] = sub_account unless sub_account.nil?

      response = WebUtils.get_json(@base_url + CREATE_JOB_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
      # Return a hash with JobId and TaskId
      return Mash.new(response)
    end

    def authorize_job(api_token, job_id)
      query_hash = init_job_req_dict(api_token, job_id)
      # Nothing returned
      WebUtils.http_request(@base_url + AUTHORIZE_JOB_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
    end

    def delete_job(api_token, job_id)
      query_hash = init_job_req_dict(api_token, job_id)
      response = WebUtils.get_json(@base_url + DELETE_JOB_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
      return response['TaskId']
    end

    def get_job_info(api_token, job_id)
      query_hash = init_job_req_dict(api_token, job_id)
      response = WebUtils.get_json(@base_url + GET_JOB_INFO_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
      return Mash.new(response)
    end

    def get_job_list(api_token, options=nil)
      query_hash = init_access_req_dict(api_token)
      query_hash.merge!(options.get_hash) unless options.nil?
      response = WebUtils.get_json(@base_url + GET_JOB_LIST_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
      return Mash.new(response)
    end

    def add_media_to_job_file(api_token, job_id, media_file)
      assert_argument(media_file, 'Media File')
      query_hash = init_job_req_dict(api_token, job_id)
      file_size = File.size(media_file.path)
      response = WebUtils.get_json(@base_url + ADD_MEDIA_TO_JOB_PATH, 'POST', nil, query_hash,
                                   {'Content-Type' => 'video/mp4', 'Content-Length' => file_size}, media_file)
      return response['TaskId']
    end

    def add_media_to_job_url(api_token, job_id, media_url)
      return send_media_url(api_token, job_id, media_url, ADD_MEDIA_TO_JOB_PATH)
    end

    def add_media_to_job_embedded(api_token, job_id, media_url)
      return send_media_url(api_token, job_id, media_url, ADD_EMBEDDED_MEDIA_TO_JOB_PATH)
    end

    def get_media(api_token, job_id)
      query_hash = init_job_req_dict(api_token, job_id)
      response = WebUtils.get_json(@base_url + GET_MEDIA_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
      return response['MediaUrl']
    end

    def perform_transcription(api_token,
                              job_id,
                              fidelity,
                              priority=nil,
                              callback_uri=nil,
                              turnaround_hours=nil,
                              target_language=nil,
                              options=nil)
      assert_argument(fidelity, 'Fidelity')
      query_hash = init_job_req_dict(api_token, job_id)
      query_hash[:transcription_fidelity] = fidelity
      query_hash[:priority] = priority unless priority.nil?
      query_hash[:callback_url] = callback_uri unless callback_uri.nil?
      query_hash[:turnaround_hours] = turnaround_hours unless turnaround_hours.nil?
      query_hash[:target_language] = target_language unless target_language.nil?
      query_hash[:options] = options.get_hash.to_json unless options.nil?

      response = WebUtils.get_json(@base_url + PERFORM_TRANSCRIPTION, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
      return response['TaskId']
    end

    def get_transcript(api_token, job_id, transcript_options=nil)
      query_hash = init_job_req_dict(api_token, job_id)
      query_hash.merge!(transcript_options.get_hash) unless transcript_options.nil?
      # Returns raw transcript text
      return WebUtils.http_request(@base_url + GET_TRANSCRIPT_PATH, 'GET', WebUtils::DOWNLOAD_TIMEOUT, query_hash)
    end

    def get_caption(api_token, job_id, caption_format, caption_options=nil)
      assert_argument(caption_format, 'Caption Format')
      query_hash = init_job_req_dict(api_token, job_id)
      query_hash[:caption_format] = caption_format
      query_hash.merge!(caption_options.get_hash) unless caption_options.nil?

      response = WebUtils.http_request(@base_url + GET_CAPTION_PATH, 'GET', WebUtils::DOWNLOAD_TIMEOUT, query_hash)
      if not caption_options.nil? and caption_options.build_url # If build_url is true
        return JSON.parse(response)['CaptionUrl']
      else
        return response # Else return raw caption text
      end
    end

    def get_element_list(api_token, job_id, elementlist_version=nil)
      query_hash = init_job_req_dict(api_token, job_id)
      query_hash[:elementlist_version] = elementlist_version unless elementlist_version.nil?
      response = WebUtils.get_json(@base_url + GET_ELEMENT_LIST_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
      return Mash.new(response)
    end

    def get_list_of_element_lists(api_token, job_id)
      query_hash = init_job_req_dict(api_token, job_id)
      response = WebUtils.get_json(@base_url + GET_LIST_OF_ELEMENT_LISTS_PATH, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
      return response
    end

    ##############################
    ### PRIVATE HELPER METHODS ###
    ##############################
    private

    def send_media_url(api_token, job_id, media_url, path)
      assert_argument(media_url, 'Media URL')
      query_hash = init_job_req_dict(api_token, job_id)
      query_hash[:media_url] = media_url
      response = WebUtils.get_json(@base_url + path, 'GET', WebUtils::BASIC_TIMEOUT, query_hash)
      return response['TaskId']
    end

    def init_job_req_dict(api_token, job_id)
      assert_argument(job_id, 'Job ID')
      init_access_req_dict(api_token).merge({job_id: job_id})
    end

    def init_access_req_dict(api_token)
      assert_argument(api_token, 'API Token')
      init_version_dict.merge({api_token: api_token})
    end

    def init_version_dict()
      {v: API_VERSION}
    end

    def assert_argument(arg, arg_name)
      if arg.nil?
        raise ArgumentError.new('Invalid argument - ' + arg_name)
      end
    end
  end
end