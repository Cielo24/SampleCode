module Cielo24
  class WebUtils

    require 'json'
    require 'httpclient'
    require 'timeout'
    include JSON

    BASIC_TIMEOUT = 60     # seconds
    DOWNLOAD_TIMEOUT = 300 # seconds
    @@LAST_URL = "none" # For logging purposes

    def self.LAST_URL
      return @@LAST_URL
    end

    def self.get_json(uri, method, timeout, query=nil, headers=nil, body=nil)
      response = http_request(uri, method, timeout, query, headers, body)
      return JSON.parse(response)
    end

    def self.http_request(uri, method, timeout, query=nil, headers=nil, body=nil)
      http_client = HTTPClient.new
      http_client.cookie_manager = nil
      http_client.send_timeout = 60*60*24*7 # HTTPClient default timeout set to 7 days, our own timeout handler is down below
      @@LAST_URL = uri + (query.nil? ? "" : "?" + URI.encode_www_form(query))

      # Timeout block:
      begin
        # Error is raised if the following block fails to execute in 'timeout' sec:
        Timeout.timeout(timeout) { # nil timeout = infinite

          response = http_client.request(method, uri, query, body, headers, nil)
          # Handle web errors
          if response.status_code == 200 or response.status_code == 204
            return response.body
          else
            json = JSON.parse(response.body)
            raise WebError.new(json["ErrorType"], json["ErrorComment"])
          end

        }
      rescue Timeout::Error
        raise TimeoutError.new("The HTTP session has timed out.")
      end
    end
  end

  class WebError < StandardError
    attr_reader :type
    def initialize(type, comment)
      super(comment)
      @type = type
    end

    def to_s
      return @type + " - " + super.to_s
    end
  end

  class TimeoutError < StandardError
    def initialize(message)
      super(message)
    end
  end
end