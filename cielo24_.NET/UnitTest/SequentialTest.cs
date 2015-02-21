using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Cielo24.JSON.Job;
using Cielo24;
using Cielo24.JSON;

namespace UnitTest
{
    [TestClass]
    public class SequentialTest : ActionsTest
    {
        protected Guid jobId = Guid.Empty;
        protected Uri sampleVideoUri = new Uri("http://techslides.com/demos/sample-videos/small.mp4");
        protected string sampleVideoFilePath = "C:\\path\\to\\file.mp4";

        [TestInitialize]
        public void InitializeSequential()
        {
            // Do nothing - we want to be able to control when we login/logout etc.
        }

        [TestMethod]
        public void testSequence()
        {
            // Login, generate API key, logout
            this.apiToken = this.actions.Login(this.username, this.password);
            this.secureKey = this.actions.GenerateAPIKey(this.apiToken, this.username, true);
            this.actions.Logout(this.apiToken);
            this.apiToken = Guid.Empty;

            // Login using API key
            this.apiToken = this.actions.Login(this.username, this.secureKey);

            // Create a job using a media URL
            this.jobId = this.actions.CreateJob(this.apiToken, ".NET_test_job").JobId;
            this.actions.AddMediaToJob(this.apiToken, this.jobId, this.sampleVideoUri);

            // Assert JobList and JobInfo data
            JobList list = this.actions.GetJobList(this.apiToken);
            Assert.IsTrue(this.containsJob(this.jobId, list));
            Job job = this.actions.GetJobInfo(this.apiToken, this.jobId);
            Assert.AreEqual(this.jobId, job.JobId);

            // Logout
            this.actions.Logout(this.apiToken);
            this.apiToken = Guid.Empty;

            // Login/logout/change password 
            this.apiToken = this.actions.Login(this.username, this.password);
            this.actions.UpdatePassword(this.apiToken, this.newPassword);
            this.actions.Logout(this.apiToken);
            this.apiToken = Guid.Empty;

            // Change password back
            this.apiToken = this.actions.Login(this.username, this.newPassword);
            this.actions.UpdatePassword(this.apiToken, this.password);
            this.actions.Logout(this.apiToken);
            this.apiToken = Guid.Empty;

            // Login using API key
            this.apiToken = this.actions.Login(this.username, this.secureKey);

            // Delete job and assert JobList data
            this.actions.DeleteJob(this.apiToken, this.jobId);
            JobList list2 = this.actions.GetJobList(this.apiToken);
            Assert.IsFalse(this.containsJob(this.jobId, list2));

            // Delete current API key and try to re-login (should fail)
            this.actions.RemoveAPIKey(this.apiToken, this.secureKey);
            this.actions.Logout(this.apiToken);
            this.apiToken = Guid.Empty;

            try
            {
                this.apiToken = this.actions.Login(this.username, this.secureKey);
                Assert.Fail();
            }
            catch (EnumWebException e)
            {
                Assert.AreEqual(ErrorType.ACCOUNT_UNPRIVILEGED.ToString(), e.ErrorType);
            }
        }

        private bool containsJob(Guid jobId, JobList list)
        {
            foreach(Job j in list.ActiveJobs)
            {
                if(j.JobId.Equals(jobId))
                {
                    return true;
                }
            }
            return false;
        }
    }
}
