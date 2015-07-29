using Cielo24;
using Cielo24.JSON;
using Cielo24.JSON.ElementList;
using Cielo24.JSON.Job;
using Cielo24.Options;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UnitTest
{
    [TestClass]
    public class JobTest : ActionsTest
    {
        protected Guid jobId = Guid.Empty;
        protected Guid taskId = Guid.Empty;

        [TestInitialize]
        public override void Initialize()
        {
            base.Initialize();
            // Always start with a fresh job
            this.jobId = this.actions.CreateJob(this.apiToken).JobId;
        }

        [TestMethod]
        public void testOptions()
        {
            CaptionOptions options = new CaptionOptions();
            options.CaptionBySentence = true;
            options.ForceCase = Case.UPPER;
            String[] array = new String[] { "build_url=true", "dfxp_header=header" };
            options.PopulateFromArray(array);
            Assert.AreEqual("build_url=true&caption_by_sentence=true&dfxp_header=header&force_case=upper", options.ToQuery().ToLower());
        }

        [TestMethod]
        public void testCreateJob()
        {
            CreateJobResult result = this.actions.CreateJob(this.apiToken, "test_name", Language.ENGLISH);
            Assert.AreEqual(32, result.JobId.ToString("N").Length);
            Assert.AreEqual(32, result.TaskId.ToString("N").Length);
        }

        [TestMethod]
        public void testAuthorizeJob()
        {
            this.actions.AuthorizeJob(this.apiToken, this.jobId);
        }

        [TestMethod]
        public void testDeleteJob()
        {
            this.taskId = this.actions.DeleteJob(this.apiToken, this.jobId);
            Assert.AreEqual(32, this.taskId.ToString("N").Length);
        }

        [TestMethod]
        public void testGetJobInfo()
        {
            Job info = this.actions.GetJobInfo(this.apiToken, this.jobId);
        }

        [TestMethod]
        public void testGetJobList()
        {
            JobList list = this.actions.GetJobList(this.apiToken);
        }

        [TestMethod]
        public void testGetElementList()
        {
            ElementList list = this.actions.GetElementList(this.apiToken, this.jobId);
        }

        [TestMethod]
        public void testGetListOfElementLists()
        {
            List<ElementListVersion> list = this.actions.GetListOfElementLists(this.apiToken, this.jobId);
        }

        [TestMethod]
        public void testGetMedia()
        {
            // Add media to job first
            this.actions.AddMediaToJob(this.apiToken, this.jobId, this.config.sampleVideoUri);
            // Test get media
            Uri uri = this.actions.GetMedia(this.apiToken, this.jobId);
        }

        [TestMethod]
        public void testGetTranscript()
        {
            this.actions.GetTranscript(this.apiToken, this.jobId);
        }

        [TestMethod]
        public void testGetCaption()
        {
            this.actions.GetCaption(this.apiToken, this.jobId, CaptionFormat.SRT);
        }

        [TestMethod]
        public void testGetCaptionBuildUrl()
        {
            CaptionOptions options = new CaptionOptions(buildUri:true);
            string response = this.actions.GetCaption(this.apiToken, this.jobId, CaptionFormat.SRT, options);
            Uri uri = new Uri(response);
        }

        [TestMethod]
        public void testPerformTranscription()
        {
            this.actions.AddMediaToJob(this.apiToken, this.jobId, this.config.sampleVideoUri);
            Uri callback_uri = new Uri("http://fake-callback.com/action?api_token=1234&job_id={job_id}");
            this.taskId = this.actions.PerformTranscription(this.apiToken, this.jobId, Fidelity.PREMIUM, Priority.STANDARD, callback_uri);
            Assert.AreEqual(32, this.taskId.ToString("N").Length);
        }

        [TestMethod]
        public void testPerformTranscriptionCallbackUrlEncoding()
        {
            Uri callbackUri = new Uri("http://fake-callback.com/action?api_token=1234&job_id={job_id}");
            string encodedUri = "callback_url=http:%2F%2Ffake-callback.com%2Faction%3Fapi_token%3D1234%26job_id%3D{job_id}";
            this.actions.AddMediaToJob(this.apiToken, this.jobId, this.config.sampleVideoUri);
            this.taskId = this.actions.PerformTranscription(this.apiToken, this.jobId, Fidelity.PREMIUM, Priority.STANDARD, callbackUri);
            // Last log entry will contain the callback to perform_transcription
            Assert.IsTrue(memoryTarget.Logs.Last().Contains(encodedUri));
        }

        [TestMethod]
        public void testAddMediaToJobUrl()
        {
            this.taskId = this.actions.AddMediaToJob(this.apiToken, this.jobId, this.config.sampleVideoUri);
            Assert.AreEqual(32, this.taskId.ToString("N").Length);
        }

        [TestMethod]
        public void testAddMediaToJobEmbedded()
        {
            this.taskId = this.actions.AddEmbeddedMediaToJob(this.apiToken, this.jobId, this.config.sampleVideoUri);
            Assert.AreEqual(32, this.taskId.ToString("N").Length);
        }

        [TestMethod]
        public void testAddMediaToJobFile()
        {
            FileStream fs = new FileStream(this.config.sampleVideoFilePath, FileMode.Open);
            this.taskId = this.actions.AddMediaToJob(this.apiToken, this.jobId, fs);
            Assert.AreEqual(32, this.taskId.ToString("N").Length);
        }
    }
}
