package test;


import cielo24.Enums.*;
import cielo24.json.Job;
import cielo24.json.JobList;
import cielo24.utils.Guid;
import cielo24.utils.WebException;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.net.URL;

public class SequentialClass extends ActionsTest {

    protected Guid jobId = null;
    protected String sampleVideoUri = "http://techslides.com/demos/sample-videos/small.mp4";
    protected String sampleVideoFilePath = "C:\\path\\to\\file.mp4";

    @Before
    public void setUp() throws Exception {
        // Do nothing - we want to be able to control when we login/logout etc.
    }

    @Test
    public void testSequence() throws IOException, WebException {
        // Login, generate API key, logout
        this.apiToken = this.actions.login(this.username, this.password);
        this.secureKey = this.actions.generateAPIKey(this.apiToken, this.username, true);
        this.actions.logout(this.apiToken);
        this.apiToken = null;

        // Login using API key
        this.apiToken = this.actions.login(this.username, this.secureKey);

        // Create a job using a media URL
        this.jobId = this.actions.createJob(this.apiToken, "Java_test_job", Languages.en.toString()).jobId;
        this.actions.addMediaToJob(this.apiToken, this.jobId, new URL(this.sampleVideoUri));

        // Assert JobList and JobInfo data
        JobList list = this.actions.getJobList(this.apiToken, null);
        assertTrue("JobId not found in JobList", this.containsJob(this.jobId, list));
        Job job = this.actions.getJobInfo(this.apiToken, this.jobId);
        assertEquals("Wrong JobId found in JobInfo", this.jobId, job.jobId);

        // Logout
        this.actions.logout(this.apiToken);
        this.apiToken = null;

        // Login/logout/change password
        this.apiToken = this.actions.login(this.username, this.password);
        this.actions.updatePassword(this.apiToken, this.newPassword);
        this.actions.logout(this.apiToken);
        this.apiToken = null;

        // Change password back
        this.apiToken = this.actions.login(this.username, this.newPassword);
        this.actions.updatePassword(this.apiToken, this.password);
        this.actions.logout(this.apiToken);
        this.apiToken = null;

        // Login using API key
        this.apiToken = this.actions.login(this.username, this.secureKey);

        // Delete job and assert JobList data
        this.actions.deleteJob(this.apiToken, this.jobId);
        JobList list2 = this.actions.getJobList(this.apiToken);
        assertFalse("JobId should not be in JobList", this.containsJob(this.jobId, list2));

        // Delete current API key and try to re-login (should fail)
        this.actions.removeAPIKey(this.apiToken, this.secureKey);
        this.actions.logout(this.apiToken);
        this.apiToken = null;

        try
        {
            this.apiToken = this.actions.login(this.username, this.secureKey);
            fail("Should not be able to login using invalid API key");
        }
        catch (WebException e)
        {
            assertEquals("Unexpected error type", ErrorType.ACCOUNT_UNPRIVILEGED.toString(), e.getErrorType());
        }
    }

    private boolean containsJob(Guid jobId, JobList list)
    {
        for(Job j : list.activeJobs)
        {
            if(j.jobId.equals(jobId))
            {
                return true;
            }
        }
        return false;
    }
}
