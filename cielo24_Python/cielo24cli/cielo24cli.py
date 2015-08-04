#!/usr/bin/env python

from compago import *
from cielo24.enums import Fidelity, Priority, Language, CaptionFormat
from cielo24.actions import Actions
from cielo24.web_utils import WebUtils
from logging import StreamHandler
from os.path import abspath
from cielo24.options import PerformTranscriptionOptions, CaptionOptions, TranscriptOptions
from json import dumps

app = Application()


@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-H', dest='headers', required=False, help="Use headers", default=False, action='store_true')
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def login(username,
          password,
          api_securekey,
          server_url,
          headers,
          verbose_mode):
    print "Performing a login action..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = actions.login(username, password, api_securekey, headers)
    print "API token: " + token


@app.option('-N', dest='api_token', required=True, help="The API token of the current session")
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def logout(api_token,
           server_url,
           verbose_mode):
    print "Performing a logout action..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    actions.logout(api_token)
    print "Logged out successfully"


@app.option('-f', dest='fidelity', required=False, help="Fidelity: " + ', '.join(Fidelity.str_list()), default=Fidelity.PREMIUM)
@app.option('-P', dest='priority', required=False, help="Priority: " + ', '.join(Priority.str_list()), default=Priority.STANDARD)
@app.option('-l', dest='source_language', required=False, help="Source language: " + ', '.join(Language.str_list()), default=Language.ENGLISH)
@app.option('-t', dest='target_language', required=False, help="Target language: " + ', '.join(Language.str_list()), default=Language.ENGLISH)
@app.option('-n', dest='job_name', required=False, help="Job name")
@app.option('-J', dest='job_options', required=False, help="Job option (usage -J k1:v1 -J k2:v2 ...)", action='append')  #TODO help
@app.option('-T', dest='turn_around_hours', required=False, help="Turn around hours")
@app.option('-C', dest='callback_url', required=False, help="Callback URL")
@app.option('-m', dest='media_url', required=False, help="Media URL")
@app.option('-M', dest='media_file', required=False, help="Local media file")
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def create(username,
           password,
           api_securekey,
           api_token,
           server_url,
           verbose_mode,
           fidelity,
           priority,
           source_language,
           target_language,
           job_name,
           job_options,
           turn_around_hours,
           callback_url,
           media_url,
           media_file):
    if media_url is None and media_file is None:
        print "Media URL or local file path must be supplied"
        exit(1)

    print "Creating job..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    json = actions.create_job(token, job_name, source_language)
    print "Job ID: " + json['JobId']
    print "Task ID: " + json['TaskId']

    print "Adding media..."
    if not media_url is None:
        task_id = actions.add_media_to_job_url(token, json['JobId'], media_url)
    elif not media_file is None:
        file = open(abspath(media_file), "r")
        task_id = actions.add_media_to_job_file(token, json['JobId'], file)
    else:
        raise ValueError("Media URL or local file path must be supplied")
    print "Task ID: " + task_id

    print "Performing transcription..."
    # Parse option hash
    job_opts = PerformTranscriptionOptions()
    job_opts.populate_from_list(job_options)
    task_id = actions.perform_transcription(token, json['JobId'], fidelity, priority, callback_url, turn_around_hours, target_language, job_opts)
    print "Task ID: " + task_id


@app.option('-j', dest='job_id', required=True, help="Job Id")
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def delete(job_id,
           username,
           password,
           api_securekey,
           api_token,
           server_url,
           verbose_mode):
    print "Deleting job..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    task_id = actions.delete_job(token, job_id)
    print "Task ID: " + task_id


@app.option('-j', dest='job_id', required=True, help="Job Id")
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def authorize(job_id,
              username,
              password,
              api_securekey,
              api_token,
              server_url,
              verbose_mode):
    print "Authorizing job..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    actions.authorize_job(token, job_id)
    print "Authorized successfully"


@app.option('-j', dest='job_id', required=True, help="Job Id")
@app.option('-m', dest='media_url', required=False, help="Media URL")
@app.option('-M', dest='media_file', required=False, help="Local media file")
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def add_media_to_job(job_id,
                     media_url,
                     media_file,
                     username,
                     password,
                     api_securekey,
                     api_token,
                     server_url,
                     verbose_mode):
    print "Adding media to job..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    if not media_url is None:
        task_id = actions.add_media_to_job_url(token, job_id, media_url)
    elif not media_file is None:
        file = open(abspath(media_file), "r")
        task_id = actions.add_media_to_job_file(token, job_id, file)
    else:
        raise ValueError("Media URL or local file path must be supplied")
    print "Task ID: " + task_id


@app.option('-j', dest='job_id', required=True, help="Job Id")
@app.option('-m', dest='media_url', required=True, help="Media URL")
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def add_embedded_media_to_job(job_id,
                              media_url,
                              username,
                              password,
                              api_securekey,
                              api_token,
                              server_url,
                              verbose_mode):
    print "Adding embedded media to job..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    task_id = actions.add_media_to_job_embedded(token, job_id, media_url)
    print "Task ID: " + task_id


# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def get_job_list(username,
         password,
         api_securekey,
         api_token,
         server_url,
         verbose_mode):
    print "Retrieving list..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    json = actions.get_job_list(token)
    print dumps(json, indent=4, separators=(',', ': '))


@app.option('-j', dest='job_id', required=True, help="Job Id")
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def list_elementlists(job_id,
                      username,
                      password,
                      api_securekey,
                      api_token,
                      server_url,
                      verbose_mode):
    print "Listing Element Lists..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    array = actions.get_list_of_element_lists(token, job_id)
    print dumps(array, indent=4, separators=(',', ': '))


@app.option('-j', dest='job_id', required=True, help="Job Id")
@app.option('-O', dest='caption_options', required=False, help="Caption/transcript options (usage -O k1:v1 -O k2:v2 ...)", action='append')
@app.option('-c', dest='caption_format', required=False, help="Caption format: " + ', '.join(CaptionFormat.str_list()), default=CaptionFormat.SRT)
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False, help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def get_caption(job_id,
                caption_options,
                caption_format,
                username,
                password,
                api_securekey,
                api_token,
                server_url,
                verbose_mode):
    print "Getting caption..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    # Parse options
    caption_opts = CaptionOptions()
    caption_opts.populate_from_list(caption_options)
    caption = actions.get_caption(token, job_id, caption_format, caption_opts)
    print caption


@app.option('-j', dest='job_id', required=True, help="Job Id")
@app.option('-O', dest='caption_options', required=False, help="Caption/transcript options (usage -O k1:v1 -O k2:v2 ...)", action='append')
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def get_transcript(job_id,
                   caption_options,
                   username,
                   password,
                   api_securekey,
                   api_token,
                   server_url,
                   verbose_mode):
    print "Getting transcript..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    # Parse options
    transcription_opts = TranscriptOptions()
    transcription_opts.populate_from_list(caption_options)
    transcript = actions.get_transcript(token, job_id, transcription_opts)
    print transcript


@app.option('-j', dest='job_id', required=True, help="Job Id")
@app.option('-e', dest='elementlist_version', required=False, help="ElementList version", default=None)
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def get_elementlist(job_id,
                    username,
                    password,
                    api_securekey,
                    api_token,
                    server_url,
                    verbose_mode,
                    elementlist_version):
    print "Getting ELement List..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    json = actions.get_element_list(token, job_id, elementlist_version)
    print dumps(json, indent=4, separators=(',', ': '))


@app.option('-j', dest='job_id', required=True, help="Job Id")
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def get_media(job_id,
              username,
              password,
              api_securekey,
              api_token,
              server_url,
              verbose_mode):
    print "Getting media..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    url = actions.get_media(token, job_id)
    print url


@app.option('-F', dest='force_new', required=False, help="Force new key", default=False, action='store_true')
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-k', dest='api_securekey', required=False,help="The API Secure Key",  default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def generate_api_key(force_new,
                     username,
                     password,
                     api_securekey,
                     api_token,
                     server_url,
                     verbose_mode):
    print "Generating API key..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    key = actions.generate_api_key(token, username, force_new)
    print "API Secure Key: " + key


@app.option('-k', dest='api_securekey', required=True, help="The API Key to remove")
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def remove_api_key(api_securekey,
                   username,
                   password,
                   api_token,
                   server_url,
                   verbose_mode):
    print "Removing API key..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    actions.remove_api_key(token, api_securekey)
    print "The key was successfully removed."


@app.option('-d', dest='new_password', required=True, help="New password")
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-k', dest='api_securekey', required=False, help="The API Key to remove")
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def update_password(new_password,
                    username,
                    password,
                    api_securekey,
                    api_token,
                    server_url,
                    verbose_mode):
    print "Updating password..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    actions.update_password(token, new_password)
    print "Password was updated successfully."


@app.option('-j', dest='job_id', required=True, help="Job Id")
# Always required (hidden)
@app.option('-u', dest='username', required=True, help="cielo24 username")
@app.option('-p', dest='password', required=False, help="cielo24 password", default=None)
@app.option('-N', dest='api_token', required=False, help="The API token of the current session", default=None)
@app.option('-k', dest='api_securekey', required=False, help="The API Key to remove")
@app.option('-s', dest='server_url', required=False, help="cielo24 server URL [https://api.cielo24.com]", default="http://api.cielo24.com")
@app.option('-v', dest='verbose_mode', required=False, help="Verbose mode", default=False, action='store_true')
def job_info(job_id,
             username,
             password,
             api_securekey,
             api_token,
             server_url,
             verbose_mode):
    print "Getting Job Info..."
    __set_verbose(verbose_mode)
    actions = __initialize_actions(server_url)
    token = __get_token(actions, username, password, api_securekey, api_token)
    json = actions.get_job_info(token, job_id)
    print dumps(json, indent=4, separators=(',', ': '))


### PRIVATE HELPERS ###

def __initialize_actions(server_url):
    return Actions(server_url)


def __set_verbose(verbose_mode):
    if verbose_mode:
        WebUtils.LOGGER.addHandler(StreamHandler())
        WebUtils.LOGGER.setLevel(20)


def __get_token(actions, username, password, api_securekey, api_token):
    return __login(actions, username, password, api_securekey) if (api_token is None) else api_token


def __login(actions, username, password, securekey):
    if username is None:
        raise ValueError("Username was not supplied.")
    return actions.login(username, password, securekey, True)


if __name__ == '__main__':
    app.run()
