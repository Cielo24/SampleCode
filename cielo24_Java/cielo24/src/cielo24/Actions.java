package cielo24;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.lang.reflect.Type;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;

import cielo24.WebUtils.HttpMethod;
import cielo24.json.CreateJobResult;
import cielo24.json.ElementList;
import cielo24.json.ElementListVersion;
import cielo24.json.JobInfo;
import cielo24.json.JobList;
import cielo24.options.CaptionOptions;
import cielo24.options.PerformTranscriptionOptions;
import cielo24.options.TranscriptOptions;
import cielo24.utils.Dictionary;
import cielo24.utils.Guid;
import cielo24.utils.NanoDate;
import cielo24.utils.WebException;
import cielo24.Enums.*;

public class Actions {

	public String serverUrl = "https://api.cielo24.com";
	private WebUtils web = new WebUtils();
	
	private final static int API_VERSION = 1;
	private final static String LOGIN_PATH = "/api/account/login";
	private final static String LOGOUT_PATH = "/api/account/logout";
	private final static String UPDATE_PASSWORD_PATH = "/api/account/update_password";
	private final static String GENERATE_API_KEY_PATH = "/api/account/generate_api_key";
	private final static String REMOVE_API_KEY_PATH = "/api/account/remove_api_key";
	private final static String CREATE_JOB_PATH = "/api/job/new";
	private final static String AUTHORIZE_JOB_PATH = "/api/job/authorize";
	private final static String DELETE_JOB_PATH = "/api/job/del";
	private final static String GET_JOB_INFO_PATH = "/api/job/info";
	private final static String GET_JOB_LIST_PATH = "/api/job/list";
	private final static String ADD_MEDIA_TO_JOB_PATH = "/api/job/add_media";
	private final static String ADD_EMBEDDED_MEDIA_TO_JOB_PATH = "/api/job/add_media_url";
	private final static String GET_MEDIA_PATH = "/api/job/media";
	private final static String PERFORM_TRANSCRIPTION = "/api/job/perform_transcription";
	private final static String GET_TRANSCRIPTION_PATH = "/api/job/get_transcript";
	private final static String GET_CAPTION_PATH = "/api/job/get_caption";
	private final static String GET_ELEMENT_LIST_PATH = "/api/job/get_elementlist";
	private final static String GET_LIST_OF_ELEMENT_LISTS_PATH = "/api/job/list_elementlists";

	public Actions() {}

	public Actions(String url) {
		this.serverUrl = url;
	}

	/// ACCESS CONTROL ///

	/* Performs a Login action. If useHeaders is true, puts username and password into HTTP headers */
	public Guid login(String username, String password, boolean useHeaders) throws IOException, WebException {
		this.assertArgument(username, "Username");
		this.assertArgument(password, "Password");

		Dictionary<String, String> queryDictionary = initVersionDict();
		Dictionary<String, String> headers = new Dictionary<String, String>();

		if (!useHeaders) {
			queryDictionary.add("username", username);
			queryDictionary.add("password", password);
		} else {
			headers.add("x-auth-user", username);
			headers.add("x-auth-key", password);
		}

		URL requestURL = Utils.buildURL(serverUrl, LOGIN_PATH, queryDictionary);
		String serverResponse = web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT, headers);
		HashMap<String, String> response = Utils.deserialize(serverResponse, Utils.hashMapType);

		return new Guid(response.get("ApiToken"));
	}

	/* Performs a Login action. If useHeaders is true, puts securekey into HTTP headers */
	public Guid login(String username, Guid securekey, boolean useHeaders) throws IOException, WebException {
		this.assertArgument(username, "Username");

		Dictionary<String, String> queryDictionary = initVersionDict();
		Dictionary<String, String> headers = new Dictionary<String, String>();

		if (!useHeaders) {
			queryDictionary.add("username", username);
			queryDictionary.add("securekey", securekey.toString());
		} else {
			headers.add("x-auth-user", username);
			headers.add("x-auth-securekey", securekey.toString());
		}

		URL requestURL = Utils.buildURL(serverUrl, LOGIN_PATH, queryDictionary);
		String serverResponse = web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT, headers);
		HashMap<String, String> response = Utils.deserialize(serverResponse, Utils.hashMapType);

		return new Guid(response.get("ApiToken"));
	}

	/* Performs a Logout action */
	public void logout(Guid apiToken) throws IOException, WebException {
		Dictionary<String, String> queryDictionary = this.initAccessReqDict(apiToken);
		URL requestURL = Utils.buildURL(serverUrl, LOGOUT_PATH, queryDictionary);
		web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT); // Nothing returned
	}

	/* Updates password */
	public void updatePassword(Guid apiToken, String newPassword) throws IOException, WebException {
		this.assertArgument(newPassword, "New Password");

		Dictionary<String, String> queryDictionary = this.initAccessReqDict(apiToken);
		queryDictionary.add("new_password", newPassword);

		URL requestURL = Utils.buildURL(serverUrl, UPDATE_PASSWORD_PATH, queryDictionary);
		web.httpRequest(requestURL, HttpMethod.POST, WebUtils.BASIC_TIMEOUT, Utils.toQuery(queryDictionary)); // Nothing returned
	}

	/* Returns a new Secure API key */
	public Guid generateAPIKey(Guid apiToken, String username, boolean forceNew) throws IOException, WebException {
		this.assertArgument(username, "Username");

		Dictionary<String, String> queryDictionary = this.initAccessReqDict(apiToken);
		queryDictionary.add("account_id", username);
		queryDictionary.add("force_new", Boolean.toString(forceNew));

		URL requestURL = Utils.buildURL(serverUrl, GENERATE_API_KEY_PATH, queryDictionary);
		String serverResponse = web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
		HashMap<String, String> response = Utils.deserialize(serverResponse, Utils.hashMapType);

		return new Guid(response.get("ApiKey"));
	}

	/* Deactivates the supplied Secure API key */
	public void removeAPIKey(Guid apiToken, Guid apiSecurekey) throws IOException, WebException {
		Dictionary<String, String> queryDictionary = this.initAccessReqDict(apiToken);
		queryDictionary.add("api_securekey", apiSecurekey.toString());

		URL requestURL = Utils.buildURL(serverUrl, REMOVE_API_KEY_PATH, queryDictionary);
		web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT); // Nothing returned
	}

	/// JOB CONTROL ///

	/* Creates a new job. Returns an array of Guids where 'JobId' is the 0th element and 'TaskId' is the 1st element */
	public CreateJobResult createJob(Guid apiToken, String jobName, String language) throws IOException, WebException {
		Dictionary<String, String> queryDictionary = this.initAccessReqDict(apiToken);
		if (jobName != null) {
			queryDictionary.add("job_name", jobName);
		}
		queryDictionary.add("language", language);

		URL requestURL = Utils.buildURL(serverUrl, CREATE_JOB_PATH, queryDictionary);
		String serverResponse = web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
		CreateJobResult response = Utils.deserialize(serverResponse, CreateJobResult.class);

		return response;
	}

	/* Authorizes a job with jobId */
	public void authorizeJob(Guid apiToken, Guid jobId) throws IOException, WebException {
		Dictionary<String, String> queryDictionary = initJobReqDict(apiToken, jobId);
		URL requestURL = Utils.buildURL(serverUrl, AUTHORIZE_JOB_PATH, queryDictionary);
		web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT); // Nothing returned
	}

	/* Deletes a job with jobId */
	public Guid deleteJob(Guid apiToken, Guid jobId) throws IOException, WebException {
		HashMap<String, String> response = getJobResponse(apiToken, jobId, DELETE_JOB_PATH, Utils.hashMapType);
		return new Guid(response.get("TaskId"));
	}

	/* Gets information about a job with jobId */
	public JobInfo getJobInfo(Guid apiToken, Guid jobId) throws IOException, WebException {
		return getJobResponse(apiToken, jobId, GET_JOB_INFO_PATH, JobInfo.class);
	}

	/* Gets a list of jobs */
	public JobList getJobList(Guid apiToken) throws IOException, WebException {
		Dictionary<String, String> queryDictionary = initAccessReqDict(apiToken);
		URL requestURL = Utils.buildURL(serverUrl, GET_JOB_LIST_PATH, queryDictionary);
		String serverResponse = web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
		JobList jobList = Utils.deserialize(serverResponse, JobList.class);
		return jobList;
	}

	/* Uploads a file from fileStream to job with jobId */
	public Guid addMediaToJob(Guid apiToken, Guid jobId, File file) throws IOException, WebException {
		this.assertArgument(file, "Local Media File");
		BufferedInputStream stream = new BufferedInputStream(new FileInputStream(file));

		Dictionary<String, String> queryDictionary = initJobReqDict(apiToken, jobId);
		URL requestURL = Utils.buildURL(serverUrl, ADD_MEDIA_TO_JOB_PATH, queryDictionary);
		String serverResponse = web.uploadData(requestURL, stream, "video/mp4", file.length());
		HashMap<String, String> response = Utils.deserialize(serverResponse, Utils.hashMapType);

		return new Guid(response.get("TaskId"));
	}

	/* Provides job with jobId a url to media */
	public Guid addMediaToJob(Guid apiToken, Guid jobId, URL mediaUrl) throws IOException, WebException {
		return sendMediaUrl(apiToken, jobId, mediaUrl, ADD_MEDIA_TO_JOB_PATH);
	}

	/* Provides job with jobId a url to media */
	public Guid addEmbeddedMediaToJob(Guid apiToken, Guid jobId, URL mediaUrl) throws IOException, WebException {
		return sendMediaUrl(apiToken, jobId, mediaUrl, ADD_EMBEDDED_MEDIA_TO_JOB_PATH);
	}

	/* Returns a URL to the media from job with jobId */
	public URL getMedia(Guid apiToken, Guid jobId) throws IOException, WebException {
		HashMap<String, String> response = getJobResponse(apiToken, jobId, GET_MEDIA_PATH, Utils.hashMapType);
		return new URL(response.get("MediaUrl"));
	}

	/* Makes a PerformTranscription call */
	public Guid performTranscription(Guid apiToken,
									 Guid jobId,
									 Fidelity fidelity,
									 Priority priority,
									 URL callback_uri,
									 Integer turnaround_hours,
									 String targetLanguage,
									 PerformTranscriptionOptions options)
									 throws IOException, WebException {
		Dictionary<String, String> queryDictionary = initJobReqDict(apiToken, jobId);
		queryDictionary.add("transcription_fidelity", fidelity.toString());
		queryDictionary.add("priority", priority.toString());
		if (callback_uri != null) {
			queryDictionary.add("callback_url", Utils.encodeUrl(callback_uri));
		}
		if (turnaround_hours != null) {
			queryDictionary.add("turnaround_hours", turnaround_hours.toString());
		}
		if (targetLanguage != null) {
			queryDictionary.add("target_language", targetLanguage);
		}
		if (options != null) {
			queryDictionary.addAll(options.GetDictionary());
		}

		URL requestURL = Utils.buildURL(serverUrl, PERFORM_TRANSCRIPTION, queryDictionary);
		String serverResponse = web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
		HashMap<String, String> response = Utils.deserialize(serverResponse, Utils.hashMapType);

		return new Guid(response.get("TaskId"));
	}

	/* Returns a transcript from a job with jobId */
	public String getTranscript(Guid apiToken,
								Guid jobId,
								TranscriptOptions transcriptOptions)
								throws IOException, WebException {
		Dictionary<String, String> queryDictionary = initJobReqDict(apiToken, jobId);
		if (transcriptOptions != null) {
			queryDictionary.addAll(transcriptOptions.GetDictionary());
		}

		URL requestURL = Utils.buildURL(serverUrl, GET_TRANSCRIPTION_PATH, queryDictionary);
		return web.httpRequest(requestURL, HttpMethod.GET, WebUtils.DOWNLOAD_TIMEOUT); // Transcript text
	}

	/* Returns a caption from a job with jobId OR if buildURL is true, returns a String representation of the URL */
	public String getCaption(Guid apiToken,
							 Guid jobId,
							 CaptionFormat captionFormat,
							 CaptionOptions captionOptions)
							 throws IOException, WebException {
		Dictionary<String, String> queryDictionary = initJobReqDict(apiToken, jobId);
		queryDictionary.add("caption_format", captionFormat.toString());
		if (captionOptions != null) {
			queryDictionary.addAll(captionOptions.GetDictionary());
		}

		URL requestURL = Utils.buildURL(serverUrl, GET_CAPTION_PATH, queryDictionary);
		String serverResponse = web.httpRequest(requestURL, HttpMethod.GET, WebUtils.DOWNLOAD_TIMEOUT);
		if (captionOptions != null && captionOptions.buildUrl != null && captionOptions.buildUrl) {
			HashMap<String, String> response = Utils.deserialize(serverResponse, Utils.hashMapType);
			return response.get("CaptionUrl");
		}

		return serverResponse; // Caption text
	}

	/* Returns an element list */
	public ElementList getElementList(Guid apiToken, Guid jobId, NanoDate elementListVersion) throws IOException, WebException {
		Dictionary<String, String> queryDictionary = initJobReqDict(apiToken, jobId);
		if (elementListVersion != null) {
			queryDictionary.add("elementlist_version", elementListVersion.toString());
		}

		URL requestURL = Utils.buildURL(serverUrl, GET_ELEMENT_LIST_PATH, queryDictionary);
		String serverResponse = web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
		return Utils.deserialize(serverResponse, ElementList.class);
	}

	/* Returns a list of elements lists */
	public ArrayList<ElementListVersion> getListOfElementLists(Guid apiToken, Guid jobId) throws IOException, WebException {
		return getJobResponse(apiToken, jobId, GET_LIST_OF_ELEMENT_LISTS_PATH, Utils.listELType);
	}

	/// OVERLOADED VERISONS ///
	/////////////////////////////////////////////////////////////////////
	public Guid login(String username, String password) throws IOException, WebException {
		return login(username, password, false);
	}

	public Guid login(String username, Guid securekey) throws IOException, WebException {
		return login(username, securekey, false);
	}

	public Guid generateAPIKey(Guid apiToken, String username) throws IOException, WebException {
		return generateAPIKey(apiToken, username, false);
	}

	public CreateJobResult createJob(Guid apiToken) throws IOException, WebException {
		return createJob(apiToken, null, "en");
	}

	public String getTranscript(Guid apiToken, Guid jobId) throws IOException, WebException {
		return getTranscript(apiToken, jobId, null);
	}

	public String getCaption(Guid apiToken, Guid jobId, CaptionFormat captionFormat)
							 throws IOException, WebException {
		return getCaption(apiToken, jobId, captionFormat, null);
	}

	public ElementList getElementList(Guid apiToken, Guid jobId) throws IOException, WebException {
		return getElementList(apiToken, jobId, null);
	}

	public Guid performTranscription(Guid apiToken, Guid jobId, Fidelity fidelity, Priority priority)
									 throws IOException, WebException {
		return performTranscription(apiToken, jobId, fidelity, priority, null, null, null, null);
	}

	/////////////////////////////////////////////////////////////////////

	/// PRIVATE HELPER METHODS ///

	private <T> T getJobResponse(Guid apiToken, Guid jobId, String path, Type type) throws IOException, WebException {
		Dictionary<String, String> queryDictionary = initJobReqDict(apiToken, jobId);
		URL requestURL = Utils.buildURL(serverUrl, path, queryDictionary);
		String serverResponse = web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
		return Utils.deserialize(serverResponse, type);
	}
	
	/* Helper method for AddMediaToJob and AddEmbeddedMediaToJob methods */
    private Guid sendMediaUrl(Guid apiToken, Guid jobId, URL mediaUrl, String path) throws IOException, WebException {
        this.assertArgument(mediaUrl, "Media URL");

        Dictionary<String, String> queryDictionary = initJobReqDict(apiToken, jobId);
        queryDictionary.add("media_url", Utils.encodeUrl(mediaUrl));

        URL requestURL = Utils.buildURL(serverUrl, path, queryDictionary);
        String serverResponse = web.httpRequest(requestURL, HttpMethod.GET, WebUtils.BASIC_TIMEOUT);
        HashMap<String, String> response = Utils.deserialize(serverResponse, Utils.hashMapType);

        return new Guid(response.get("TaskId"));
    }

	/* Returns a dictionary with version, api_token and job_id key-value pairs (parameters used in almost every job-control action). */
	private Dictionary<String, String> initJobReqDict(Guid apiToken, Guid jobId) {
		this.assertArgument(jobId, "Job Id");
		Dictionary<String, String> queryDictionary = this.initAccessReqDict(apiToken);
		queryDictionary.add("job_id", jobId.toString());
		return queryDictionary;
	}

	/* Returns a dictionary with version and api_token key-value pairs (parameters used in almost every access-control action). */
	private Dictionary<String, String> initAccessReqDict(Guid apiToken) {
		this.assertArgument(apiToken, "API Token");
		Dictionary<String, String> queryDictionary = initVersionDict();
		queryDictionary.add("api_token", apiToken.toString());
		return queryDictionary;
	}

	/* Returns a dictionary with version key-value pair (parameter used in every action). */
	private Dictionary<String, String> initVersionDict() {
		Dictionary<String, String> queryDictionary = new Dictionary<String, String>();
		queryDictionary.add("v", Integer.toString(API_VERSION));
		return queryDictionary;
	}

	/* If arg is invalid (null or empty), throws an IllegalArgumentException */
	private void assertArgument(String arg, String arg_name) {
		if (arg == null || arg.equals("")) {
			throw new IllegalArgumentException("Invalid " + arg_name);
		}
	}

	private void assertArgument(Object arg, String arg_name) {
		if (arg == null) {
			throw new IllegalArgumentException("Invalid " + arg_name);
		}
	}
}