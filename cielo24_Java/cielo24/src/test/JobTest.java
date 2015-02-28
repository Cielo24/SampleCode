package test;

import static org.junit.Assert.*;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

import org.junit.Before;
import org.junit.Test;

import cielo24.Enums.*;
import cielo24.json.*;
import cielo24.options.CaptionOptions;
import cielo24.utils.Guid;
import cielo24.utils.WebException;

public class JobTest extends ActionsTest {

    protected Guid jobId = null;
    protected Guid taskId = null;
    protected String sampleVideoUri = "http://techslides.com/demos/sample-videos/small.mp4";
    protected String sampleVideoFilePath = "C:\\path\\to\\file.mp4";

    @Before
    public void setUp() throws Exception {
        super.setUp();
        // Always start with a fresh job
        this.jobId = actions.createJob(apiToken).jobId;
    }

    @Test
    public void testOptions() {
        CaptionOptions options = new CaptionOptions();
        options.captionBySentence = true;
        options.forceCase = Case.upper;
        String[] array = new String[] { "build_url=true", "dfxp_header=header" };
        options.populateFromArray(array);
        // Can only assert length because Hashtable produces different order each time
        assertEquals("build_url=true&caption_by_sentence=true&dfxp_header=header&force_case=upper".length(), options.toQuery().length());
    }

    @Test
    public void testCreateJob() throws IOException, WebException {
        CreateJobResult result = this.actions.createJob(this.apiToken, "test_name", "en");
        assertEquals(32, result.jobId.toString().length());
        assertEquals(32, result.taskId.toString().length());
    }

    @Test
    public void testAuthorizeJob() throws IOException, WebException {
        this.actions.authorizeJob(this.apiToken, this.jobId);
    }

    @Test
    public void testDeleteJob() throws IOException, WebException {
        this.taskId = this.actions.deleteJob(this.apiToken, this.jobId);
        assertEquals(32, this.taskId.toString().length());
    }

    @Test
    public void testGetJobInfo() throws IOException, WebException {
        this.actions.getJobInfo(this.apiToken, this.jobId);
    }

    @Test
    public void testGetJobList() throws IOException, WebException {
        this.actions.getJobList(this.apiToken, null);
    }

    @Test
    public void testGetElementList() throws IOException, WebException {
        this.actions.getElementList(this.apiToken, this.jobId);
    }

    @Test
    public void testGetListOfElementLists() throws IOException, WebException {
        this.actions.getListOfElementLists(this.apiToken, this.jobId);
    }

    @Test
    public void testGetMedia() throws MalformedURLException, IOException, WebException {
        // Add media to job first
        this.actions.addEmbeddedMediaToJob(this.apiToken, this.jobId, new URL(this.sampleVideoUri));
        // Test get media
        this.actions.getMedia(this.apiToken, this.jobId);
    }

    @Test
    public void testGetTranscript() throws IOException, WebException {
        this.actions.getTranscript(this.apiToken, this.jobId);
    }

    @Test
    public void testGetCaption() throws IOException, WebException {
        this.actions.getCaption(this.apiToken, this.jobId, CaptionFormat.SRT);
    }

    @Test
    public void testGetCaptionBuildUrl() throws IOException, WebException {
        CaptionOptions options = new CaptionOptions();
        options.buildUrl = true;
        String response = this.actions.getCaption(this.apiToken, this.jobId, CaptionFormat.SRT, options);
        new URL(response); // Will throw an exception if response is not a valid URL
    }

    @Test
    public void testPerformTranscription() throws IOException, WebException {
        this.actions.addEmbeddedMediaToJob(this.apiToken, this.jobId, new URL(this.sampleVideoUri));
        this.taskId = this.actions.performTranscription(this.apiToken, this.jobId, Fidelity.PROFESSIONAL, Priority.STANDARD);
        assertEquals(32, this.taskId.toString().length());
    }

    @Test
    public void testAddMediaToJobUrl() throws MalformedURLException, IOException, WebException {
        this.taskId = this.actions.addEmbeddedMediaToJob(this.apiToken, this.jobId, new URL(this.sampleVideoUri));
        assertEquals(32, this.taskId.toString().length());
    }

    @Test
    public void testAddMediaToJobEmbedded() throws MalformedURLException, IOException, WebException {
        this.taskId = this.actions.addEmbeddedMediaToJob(this.apiToken, this.jobId, new URL(this.sampleVideoUri));
        assertEquals(32, this.taskId.toString().length());
    }

    @Test
    public void testAddMediaToJobFile() throws IOException, WebException {
        File sampleVideoFile = new File(sampleVideoFilePath);
        this.taskId = this.actions.addMediaToJob(this.apiToken, this.jobId, sampleVideoFile);
        assertEquals(32, this.taskId.toString().length());
    }
}