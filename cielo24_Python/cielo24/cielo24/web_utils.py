# encoding: utf-8
from httplib import HTTPConnection
from urllib import urlencode
from urlparse import urlparse
from json import JSONDecoder
from logging import getLogger


class WebUtils(object):

    BASIC_TIMEOUT = 60           # seconds (1 minute)
    DOWNLOAD_TIMEOUT = 300       # seconds (5 minutes)
    UPLOAD_TIMEOUT = 60*60*24*7  # seconds (1 week)
    LOGGER = getLogger('web_utils')

    @staticmethod
    def get_json(base_uri, path, method, timeout, query={}, headers={}, body=None):
        response = WebUtils.http_request(base_uri, path, method, timeout, query, headers, body)
        return JSONDecoder().decode(response)

    @staticmethod
    def http_request(base_uri, path, method, timeout, query={}, headers={}, body=None):
        if query is None:
            query = {}
        if headers is None:
            headers = {}
        http_connection = HTTPConnection(urlparse(base_uri).netloc, timeout=timeout)
        query_string = ('?' + urlencode(query)) if len(query) else ''
        # Will raise an error on timeout
        http_connection.request(method, path + query_string, body=body, headers=headers)
        WebUtils.LOGGER.info(base_uri + path + query_string)  # Log URL

        response = http_connection.getresponse()
        if response.status == 200 or response.status == 204:  # OK or NO_CONTENT
            return response.read()
        else:
            json = JSONDecoder().decode(response.read())
            raise WebError(json['ErrorType'], json['ErrorComment'])


class WebError(StandardError):
    def __init__(self, error_type, comment):
        self.message = comment
        self.error_type = error_type

    def __str__(self):
        return self.error_type + ' - ' + self.message
