using System;
using System.IO;
using System.Net;
using System.Linq;
using System.Text;
using System.Diagnostics;
using System.Security.Principal;
using System.Collections.Generic;
using Cielo24.JSON;
using Cielo24.JSON.ElementList;
using Cielo24.JSON.Job;
using Cielo24.Options;

namespace Cielo24
{
    public class Actions
    {
        public const int VERSION = 1;
        private string BASE_URL = "https://api.cielo24.com";
        public string ServerUrl { get { return this.BASE_URL; } set { this.BASE_URL = value; } }
        private WebUtils web = new WebUtils();

        private const string LOGIN_PATH = "/api/account/login";
        private const string LOGOUT_PATH = "/api/account/logout";
        private const string UPDATE_PASSWORD_PATH = "/api/account/update_password";
        private const string GENERATE_API_KEY_PATH = "/api/account/generate_api_key";
        private const string REMOVE_API_KEY_PATH = "/api/account/remove_api_key";
        private const string CREATE_JOB_PATH = "/api/job/new";
        private const string AUTHORIZE_JOB_PATH = "/api/job/authorize";
        private const string DELETE_JOB_PATH = "/api/job/del";
        private const string GET_JOB_INFO_PATH = "/api/job/info";
        private const string GET_JOB_LIST_PATH = "/api/job/list";
        private const string ADD_MEDIA_TO_JOB_PATH = "/api/job/add_media";
        private const string ADD_EMBEDDED_MEDIA_TO_JOB_PATH = "/api/job/add_media_url";
        private const string GET_MEDIA_PATH = "/api/job/media";
        private const string PERFORM_TRANSCRIPTION = "/api/job/perform_transcription";
        private const string GET_TRANSCRIPT_PATH = "/api/job/get_transcript";
        private const string GET_CAPTION_PATH = "/api/job/get_caption";
        private const string GET_ELEMENT_LIST_PATH = "/api/job/get_elementlist";
        private const string GET_LIST_OF_ELEMENT_LISTS_PATH = "/api/job/list_elementlists";

        public Actions() { }

        public Actions(String uri)
        {
            this.BASE_URL = uri;
        }

        /// ACCESS CONTROL ///

        /* Performs a Login action. If useHeaders is true, puts username and password into HTTP headers */
        public Guid Login(string username, string password, bool useHeaders = false)
        {
            this.AssertArgument(username, "Username");
            this.AssertArgument(password, "Password");

            Dictionary<string, string> queryDictionary = InitVersionDict();
            Dictionary<string, string> headers = new Dictionary<string, string>();

            if (useHeaders)
            {
                headers.Add("x-auth-user", username);
                headers.Add("x-auth-key", password);
            }
            else
            {
                queryDictionary.Add("username", username);
                queryDictionary.Add("password", password);
            }

            Uri requestUri = Utils.BuildUri(BASE_URL, LOGIN_PATH, queryDictionary);
            string serverResponse = web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.BASIC_TIMEOUT, headers);
            Dictionary<string, string> response = Utils.Deserialize<Dictionary<string, string>>(serverResponse);

            return new Guid(response["ApiToken"]);
        }

        /* Performs a Login action. If useHeaders is true, puts securekey into HTTP headers */
        public Guid Login(string username, Guid securekey, bool useHeaders = false)
        {
            this.AssertArgument(username, "Username");

            Dictionary<string, string> queryDictionary = InitVersionDict();
            Dictionary<string, string> headers = new Dictionary<string, string>();

            if (useHeaders)
            {
                headers.Add("x-auth-user", username);
                headers.Add("x-auth-securekey", securekey.ToString("N"));
            }
            else
            {
                queryDictionary.Add("username", username);
                queryDictionary.Add("securekey", securekey.ToString("N"));
            }

            Uri requestUri = Utils.BuildUri(BASE_URL, LOGIN_PATH, queryDictionary);
            string serverResponse = web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.BASIC_TIMEOUT, headers);
            Dictionary<string, string> response = Utils.Deserialize<Dictionary<string, string>>(serverResponse);

            return new Guid(response["ApiToken"]);
        }

        /* Performs a Logout action */
        public void Logout(Guid apiToken)
        {
            Dictionary<string, string> queryDictionary = this.InitAccessReqDict(apiToken);
            Uri requestUri = Utils.BuildUri(BASE_URL, LOGOUT_PATH, queryDictionary);
            web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.BASIC_TIMEOUT); // Nothing returned
        }

        /* Updates password */
        public void UpdatePassword(Guid apiToken, string newPassword)
        {
            this.AssertArgument(newPassword, "New Password");

            Dictionary<string, string> queryDictionary = this.InitAccessReqDict(apiToken);
            queryDictionary.Add("new_password", newPassword);

            Uri requestUri = Utils.BuildUri(BASE_URL, UPDATE_PASSWORD_PATH, queryDictionary);
            web.HttpRequest(requestUri, HttpMethod.POST, WebUtils.BASIC_TIMEOUT, Utils.ToQuery(queryDictionary)); // Nothing returned
        }

        /* Returns a new Secure API key */
        public Guid GenerateAPIKey(Guid apiToken, string username, bool forceNew = false)
        {
            this.AssertArgument(username, "Username");

            Dictionary<string, string> queryDictionary = this.InitAccessReqDict(apiToken);
            queryDictionary.Add("account_id", username);
            queryDictionary.Add("force_new", forceNew.ToString());

            Uri requestUri = Utils.BuildUri(BASE_URL, GENERATE_API_KEY_PATH, queryDictionary);
            string serverResponse = web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
            Dictionary<string, string> response = Utils.Deserialize<Dictionary<string, string>>(serverResponse);

            return new Guid(response["ApiKey"]);
        }

        /* Deactivates the supplied Secure API key */
        public void RemoveAPIKey(Guid apiToken, Guid apiSecurekey)
        {
            this.AssertArgument(apiSecurekey, "API Secure Key");
            Dictionary<string, string> queryDictionary = this.InitAccessReqDict(apiToken);
            queryDictionary.Add("api_securekey", apiSecurekey.ToString("N"));

            Uri requestUri = Utils.BuildUri(BASE_URL, REMOVE_API_KEY_PATH, queryDictionary);
            web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.BASIC_TIMEOUT); // Nothing returned
        }


        /// JOB CONTROL ///

        /* Creates a new job. Returns an array of Guids where 'JobId' is the 0th element and 'TaskId' is the 1st element */
        public CreateJobResult CreateJob(Guid apiToken, string jobName = null, string language = "en", string externalId = null, string subAccount = null)
        {
            Dictionary<string, string> queryDictionary = this.InitAccessReqDict(apiToken);
            if (jobName != null) { queryDictionary.Add("job_name", jobName); }
            if (externalId != null) { queryDictionary.Add("external_id", externalId); }
            if (subAccount != null) { queryDictionary.Add("username", subAccount); } // username parameter named sub_account for clarity
            queryDictionary.Add("language", language);

            Uri requestUri = Utils.BuildUri(BASE_URL, CREATE_JOB_PATH, queryDictionary);
            string serverResponse = web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
            CreateJobResult response = Utils.Deserialize<CreateJobResult>(serverResponse);

            return response;
        }

        /* Authorizes a job with jobId */
        public void AuthorizeJob(Guid apiToken, Guid jobId)
        {
            Dictionary<string, string> queryDictionary = InitJobReqDict(apiToken, jobId);
            Uri requestUri = Utils.BuildUri(BASE_URL, AUTHORIZE_JOB_PATH, queryDictionary);
            web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.BASIC_TIMEOUT); // Nothing returned
        }

        /* Deletes a job with jobId */
        public Guid DeleteJob(Guid apiToken, Guid jobId)
        {
            Dictionary<string, string> response = GetJobResponse<Dictionary<string, string>>(apiToken, jobId, DELETE_JOB_PATH);
            return new Guid(response["TaskId"]);
        }

        /* Gets information about a job with jobId */
        public JobInfo GetJobInfo(Guid apiToken, Guid jobId)
        {
            return GetJobResponse<JobInfo>(apiToken, jobId, GET_ELEMENT_LIST_PATH);
        }

        /* Gets a list of jobs */
        public JobList GetJobList(Guid apiToken, JobListOptions options = null)
        {
            Dictionary<string, string> queryDictionary = InitAccessReqDict(apiToken);
            if (options != null) { queryDictionary = Utils.DictConcat(queryDictionary, options.GetDictionary()); }

            Uri requestUri = Utils.BuildUri(BASE_URL, GET_JOB_LIST_PATH, queryDictionary);
            string serverResponse = web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
            JobList jobList = Utils.Deserialize<JobList>(serverResponse);

            return jobList;
        }

        /* Uploads a file from fileStream to job with jobId */
        public Guid AddMediaToJob(Guid apiToken, Guid jobId, Stream fileStream)
        {
            this.AssertArgument(fileStream, "File");

            Dictionary<string, string> queryDictionary = InitJobReqDict(apiToken, jobId);
            Uri requestUri = Utils.BuildUri(BASE_URL, ADD_MEDIA_TO_JOB_PATH, queryDictionary);
            string serverResponse = web.UploadData(requestUri, fileStream, "video/mp4");
            Dictionary<string, string> response = Utils.Deserialize<Dictionary<string, string>>(serverResponse);

            return new Guid(response["TaskId"]);
        }

        /* Provides job with jobId a url to media */
        public Guid AddMediaToJob(Guid apiToken, Guid jobId, Uri mediaUrl)
        {
            return SendMediaUrl(apiToken, jobId, mediaUrl, ADD_MEDIA_TO_JOB_PATH);
        }

        /* Provides job with jobId a url to media */
        public Guid AddEmbeddedMediaToJob(Guid apiToken, Guid jobId, Uri mediaUrl)
        {
            return SendMediaUrl(apiToken, jobId, mediaUrl, ADD_EMBEDDED_MEDIA_TO_JOB_PATH);
        }

        /* Returns a Uri to the media from job with jobId */
        public Uri GetMedia(Guid apiToken, Guid jobId)
        {
            Dictionary<string, string> response = GetJobResponse<Dictionary<string, string>>(apiToken, jobId, GET_MEDIA_PATH);
            return new Uri(response["MediaUrl"]);
        }

        /* Makes a PerformTranscription call */
        public Guid PerformTranscription(Guid apiToken,
                                         Guid jobId,
                                         Fidelity fidelity,
                                         Priority priority,
                                         Uri callback_uri = null,
                                         int? turnaround_hours = null,
                                         string targetLanguage = null,
                                         PerformTranscriptionOptions options = null)
        {
            Dictionary<string, string> queryDictionary = InitJobReqDict(apiToken, jobId);
            queryDictionary.Add("transcription_fidelity", fidelity.ToString());
            queryDictionary.Add("priority", priority.ToString());
            if (callback_uri != null) { queryDictionary.Add("callback_url", Utils.EncodeUrl(callback_uri)); }
            if (turnaround_hours != null) { queryDictionary.Add("turnaround_hours", turnaround_hours.ToString()); }
            if (targetLanguage != null) { queryDictionary.Add("target_language", targetLanguage); }
            if (options != null) { queryDictionary = Utils.DictConcat(queryDictionary, options.GetDictionary()); }

            Uri requestUri = Utils.BuildUri(BASE_URL, PERFORM_TRANSCRIPTION, queryDictionary);
            string serverResponse = web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
            Dictionary<string, string> response = Utils.Deserialize<Dictionary<string, string>>(serverResponse);

            return new Guid(response["TaskId"]);
        }

        /* Returns a transcript from a job with jobId */
        public string GetTranscript(Guid apiToken, Guid jobId, TranscriptOptions transcriptOptions = null)
        {
            Dictionary<string, string> queryDictionary = InitJobReqDict(apiToken, jobId);
            if (transcriptOptions != null) { queryDictionary = Utils.DictConcat(queryDictionary, transcriptOptions.GetDictionary()); }

            Uri requestUri = Utils.BuildUri(BASE_URL, GET_TRANSCRIPT_PATH, queryDictionary);
            return web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.DOWNLOAD_TIMEOUT); // Transcript text
        }

        /* Returns a caption from a job with jobId OR if buildUri is true, returns a string representation of the uri */
        public string GetCaption(Guid apiToken, Guid jobId, CaptionFormat captionFormat, CaptionOptions captionOptions = null)
        {
            Dictionary<string, string> queryDictionary = InitJobReqDict(apiToken, jobId);
            queryDictionary.Add("caption_format", captionFormat.ToString());
            if (captionOptions != null) { queryDictionary = Utils.DictConcat(queryDictionary, captionOptions.GetDictionary()); }

            Uri requestUri = Utils.BuildUri(BASE_URL, GET_CAPTION_PATH, queryDictionary);
            string serverResponse = web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.DOWNLOAD_TIMEOUT);
            if (captionOptions != null && captionOptions.BuildUrl.Equals(true))
            {
                Dictionary<string, string> response = Utils.Deserialize<Dictionary<string, string>>(serverResponse);
                return response["CaptionUrl"];
            }

            return serverResponse; // Caption text
        }

        /* Returns an element list */
        public ElementList GetElementList(Guid apiToken, Guid jobId, DateTime? elementListVersion = null)
        {
            Dictionary<string, string> queryDictionary = InitJobReqDict(apiToken, jobId);
            if (elementListVersion != null) { queryDictionary.Add("elementlist_version", ((DateTime)elementListVersion).ToString("yyyy-MM-ddTHH:mm:ss.fffffffzzz")); }

            Uri requestUri = Utils.BuildUri(BASE_URL, GET_ELEMENT_LIST_PATH, queryDictionary);
            String serverResponse = web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.DOWNLOAD_TIMEOUT);
            return Utils.Deserialize<ElementList>(serverResponse);
        }

        /* Returns a list of elements lists */
        public List<ElementListVersion> GetListOfElementLists(Guid apiToken, Guid jobId)
        {
            return GetJobResponse<List<ElementListVersion>>(apiToken, jobId, GET_LIST_OF_ELEMENT_LISTS_PATH);
        }


        /// PRIVATE HELPER METHODS ///

        /* Helper method for AddMediaToJob and AddEmbeddedMediaToJob methods */
        private Guid SendMediaUrl(Guid apiToken, Guid jobId, Uri mediaUrl, string path)
        {
            this.AssertArgument(mediaUrl, "Media URL");

            Dictionary<string, string> queryDictionary = InitJobReqDict(apiToken, jobId);
            queryDictionary.Add("media_url", Utils.EncodeUrl(mediaUrl));

            Uri requestUri = Utils.BuildUri(BASE_URL, path, queryDictionary);
            string serverResponse = web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
            Dictionary<string, string> response = Utils.Deserialize<Dictionary<string, string>>(serverResponse);

            return new Guid(response["TaskId"]);
        }

        private T GetJobResponse<T>(Guid apiToken, Guid jobId, String path)
        {
            Dictionary<String, String> queryDictionary = InitJobReqDict(apiToken, jobId);
            Uri requestUri = Utils.BuildUri(BASE_URL, path, queryDictionary);
            String serverResponse = web.HttpRequest(requestUri, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
            return Utils.Deserialize<T>(serverResponse);
        }

        /* Returns a dictionary with version, api_token and job_id key-value pairs (parameters used in almost every job-control action). */
        private Dictionary<string, string> InitJobReqDict(Guid apiToken, Guid jobId)
        {
            this.AssertArgument(jobId, "Job Id");
            Dictionary<string, string> queryDictionary = this.InitAccessReqDict(apiToken);
            queryDictionary.Add("job_id", jobId.ToString("N"));
            return queryDictionary;
        }

        /* Returns a dictionary with version and api_token key-value pairs (parameters used in almost every access-control action). */
        private Dictionary<string, string> InitAccessReqDict(Guid apiToken)
        {
            this.AssertArgument(apiToken, "API Token");
            Dictionary<string, string> queryDictionary = InitVersionDict();
            queryDictionary.Add("api_token", apiToken.ToString("N"));
            return queryDictionary;
        }

        /* Returns a dictionary with version key-value pair (parameter used in every action). */
        private Dictionary<string, string> InitVersionDict()
        {
            Dictionary<string, string> queryDictionary = new Dictionary<string, string>();
            queryDictionary.Add("v", VERSION.ToString());
            return queryDictionary;
        }

        /* If arg is invalid (null or empty), throws an ArgumentException */
        private void AssertArgument(string arg, string arg_name)
        {
            if (arg == null || arg.Equals("")) { throw new ArgumentException("Invalid " + arg_name); }
        }

        private void AssertArgument(Guid arg, string arg_name)
        {
            if (arg.Equals(Guid.Empty)) { throw new ArgumentException("Invalid " + arg_name); }
        }

        private void AssertArgument(object arg, string arg_name)
        {
            if (arg == null) { throw new ArgumentException("Invalid " + arg_name); }
        }
    }
}