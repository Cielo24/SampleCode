package test;

import static org.junit.Assert.*;

import java.io.File;
import java.net.URL;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import cielo24.Actions;
import cielo24.Enums.CaptionFormat;
import cielo24.Enums.Case;
import cielo24.Enums.Fidelity;
import cielo24.Enums.Priority;
import cielo24.json.CreateJobResult;
import cielo24.json.ElementList;
import cielo24.json.ElementListVersion;
import cielo24.json.JobInfo;
import cielo24.json.JobList;
import cielo24.options.CaptionOptions;
import cielo24.utils.Guid;

public class ActionsTest {

	Actions actions = null;
	String username = "api_test";
	String password = "api_test";
	String newPassword = "api_test_new";
	Guid apiToken = null;
	Guid jobId = null;
	Guid taskId = null;
	Guid secureKey = null;
	String sampleVideoUrl = "http://techslides.com/demos/sample-videos/small.mp4";
	String sampleVideoFilePath = "C:\\path\\to\\file.mp4";

	@Test
	public void testOptions() {
		try {
			CaptionOptions co = new CaptionOptions();
			co.captionBySentence = true;
			co.forceCase = Case.upper;
			String[] array = new String[] { "build_url=true", "dfxp_header=header" };
			co.populateFromArray(array);
			assertEquals("build_url=true&caption_by_sentence=true&dfxp_header=header&force_case=upper", co.toQuery());
		} catch (Exception e) {
			e.printStackTrace();
			fail("Test failed: " + e.getMessage());
		}
	}

	@Test
	public void testLoginAndLogout() {
		try {
			// Username, password, no headers
			apiToken = actions.login(username, password, false);
			assertEquals(32, apiToken.toString().length());
			// Username, password, headers
			apiToken = actions.login(username, password, true);
			assertEquals(32, apiToken.toString().length());
			// Username, secure key, no headers
			secureKey = actions.generateAPIKey(apiToken, username, false);
			apiToken = actions.login(username, secureKey, false);
			assertEquals(32, apiToken.toString().length());
			// Username, secure key, headers
			apiToken = actions.login(username, secureKey, true);
			assertEquals(32, apiToken.toString().length());
			// Logout
			actions.logout(apiToken);
		} catch (Exception e) {
			e.printStackTrace();
			fail("Test failed: " + e.getMessage());
		}
		apiToken = null;
	}

	@Test
	public void testGenerateAndRemoveApiKey() {
		try {
			secureKey = actions.generateAPIKey(apiToken, username, false);
			assertEquals(32, secureKey.toString().length());
			secureKey = actions.generateAPIKey(apiToken, username, true);
			assertEquals(32, secureKey.toString().length());
			actions.removeAPIKey(apiToken, secureKey);
		} catch (Exception e) {
			e.printStackTrace();
			fail("Test failed: " + e.getMessage());
		}
	}

	@Test
	public void testUpdatePassword() {
		try {
			actions.updatePassword(apiToken, newPassword);
			actions.updatePassword(apiToken, password);
		} catch (Exception e) {
			e.printStackTrace();
			fail("Test failed: " + e.getMessage());
		}
	}

	@Test
	public void testCreateJob() {
		try {
			CreateJobResult result = actions.createJob(apiToken, "testname", "en");
			assertEquals(32, result.jobId.toString().length());
			assertEquals(32, result.taskId.toString().length());
		} catch (Exception e) {
			e.printStackTrace();
			fail("Test failed: " + e.getMessage());
		}
	}

	@Test
	public void testAuthorizeJob() {
		try {
			actions.authorizeJob(apiToken, jobId);
		} catch (Exception e) {
			e.printStackTrace();
			fail("Test failed: " + e.getMessage());
		}
		jobId = null;
	}

	@Test
	public void testDeleteJob(){
		try {
			taskId = actions.deleteJob(apiToken,jobId);
			assertEquals(32, taskId.toString().length());
		} catch (Exception e) {
			e.printStackTrace();
			fail("Test failed: " + e.getMessage());
		}
		jobId = null;
	}

	@Test
	public void testGets(){
		try {
			Logger.getGlobal().log(Level.INFO, "testing getJobInfo()");
			JobInfo info = actions.getJobInfo(apiToken, jobId);
			Logger.getGlobal().log(Level.INFO, "testing getJobList()");
			JobList list = actions.getJobList(apiToken);
			Logger.getGlobal().log(Level.INFO, "testing getElementList()");
			ElementList list2 = actions.getElementList(apiToken, jobId);
			Logger.getGlobal().log(Level.INFO, "testing getListOfElementLists()");
			ArrayList<ElementListVersion> list3 = actions.getListOfElementLists(apiToken, jobId);
			Logger.getGlobal().log(Level.INFO, "testing getMedia()");
			URL url = actions.getMedia(apiToken, jobId);
		} catch (Exception e) {
			e.printStackTrace();
			fail("Test failed: " + e.getMessage());
		}
	}

	@Test
	public void testGetText() {
		try {
			actions.getCaption(apiToken, jobId, CaptionFormat.SRT);
			actions.getTranscript(apiToken, jobId);
		} catch (Exception e) {
			e.printStackTrace();
			fail("Test failed: " + e.getMessage());
		}
	}

	@Test
	public void testPerformTranscription(){
		try {
			actions.addMediaToJob(apiToken, jobId, new URL(sampleVideoUrl));
			taskId = actions.performTranscription(apiToken, jobId, Fidelity.STANDARD, Priority.STANDARD);
			assertEquals(32, taskId.toString().length());
		} catch (Exception e) {
			e.printStackTrace();
			fail("Test failed: " + e.getMessage());
		}
	}

	@Test
	public void testAddData(){
		try {
			File sampleVideoFile = new File(sampleVideoFilePath);
            taskId = actions.addMediaToJob(apiToken, jobId, new URL(sampleVideoUrl));
			assertEquals(32, taskId.toString().length());
			jobId = actions.createJob(apiToken).jobId;
			taskId = actions.addEmbeddedMediaToJob(apiToken, jobId, new URL(sampleVideoUrl));
			assertEquals(32, taskId.toString().length());
			jobId = actions.createJob(apiToken).jobId;
			taskId = actions.addMediaToJob(apiToken,jobId, sampleVideoFile);
			assertEquals(32, taskId.toString().length());
		} catch (Exception e) {
			e.printStackTrace();
			fail("Test failed: " + e.getMessage());
		}
	}

	@Before
	public void setUp() throws Exception {
		this.actions = new Actions("http://sandbox-dev.cielo24.com");
		if (this.apiToken == null){
			this.apiToken = actions.login(username, password, true);
		}
		if (this.jobId == null){
			this.jobId = actions.createJob(apiToken).jobId;
		}
	}

	@After
	public void tearDown() throws Exception {
		// Do nothing
	}
}