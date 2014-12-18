﻿using Cielo24;
using Cielo24.JSON;
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
        private Guid jobId = Guid.Empty;
        private Guid taskId = Guid.Empty;
        private Uri sampleVideoUri = new Uri("http://techslides.com/demos/sample-videos/small.mp4");
        private string sampleVideoFilePath = "C:\\path\\to\\file.mp4";

        [TestInitialize]
        public new void Initialize()
        {
            base.Initialize();
            if (this.jobId.Equals(Guid.Empty))
            {
                this.jobId = this.actions.CreateJob(apiToken).JobId;
            }
        }

        [TestMethod]
        public void testOptions()
        {
            CaptionOptions options = new CaptionOptions();
            options.CaptionBySentence = true;
            options.ForceCase = Case.upper;
            String[] array = new String[] { "build_url=true", "dfxp_header=header" };
            options.PopulateFromArray(array);
            Assert.AreEqual("build_url=true&caption_by_sentence=true&dfxp_header=header&force_case=upper", options.ToQuery().ToLower());
        }

        [TestMethod]
        public void testCreateJob()
        {
            CreateJobResult result = this.actions.CreateJob(this.apiToken, "test_name", "en");
            Assert.AreEqual(32, result.JobId.ToString("N").Length);
            Assert.AreEqual(32, result.TaskId.ToString("N").Length);
        }

        [TestMethod]
        public void testAuthorizeJob()
        {
            this.actions.AuthorizeJob(this.apiToken, this.jobId);
            this.jobId = Guid.Empty;
        }

        [TestMethod]
        public void testDeleteJob()
        {
            this.taskId = this.actions.DeleteJob(this.apiToken, this.jobId);
            Assert.AreEqual(32, this.taskId.ToString("N").Length);
            this.jobId = Guid.Empty;
        }

        [TestMethod]
        public void testGetJobInfo()
        {
            JobInfo info = this.actions.GetJobInfo(this.apiToken, this.jobId);
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
            this.actions.AddMediaToJob(this.apiToken, this.jobId, this.sampleVideoUri);
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
            this.actions.AddMediaToJob(this.apiToken, this.jobId, this.sampleVideoUri);
            this.taskId = this.actions.PerformTranscription(this.apiToken, this.jobId, Fidelity.STANDARD, Priority.STANDARD);
            Assert.AreEqual(32, this.taskId.ToString("N").Length);
        }

        [TestMethod]
        public void testAddMediaToJobUrl()
        {
            this.taskId = this.actions.AddMediaToJob(this.apiToken, this.jobId, this.sampleVideoUri);
            Assert.AreEqual(32, this.taskId.ToString("N").Length);
        }

        [TestMethod]
        public void testAddMediaToJobEmbedded()
        {
            this.jobId = this.actions.CreateJob(this.apiToken).JobId;
            this.taskId = this.actions.AddEmbeddedMediaToJob(this.apiToken, this.jobId, this.sampleVideoUri);
            Assert.AreEqual(32, this.taskId.ToString("N").Length);
        }

        [TestMethod]
        public void testAddMediaToJobFile()
        {
            FileStream fs = new FileStream(this.sampleVideoFilePath, FileMode.Open);
            this.jobId = this.actions.CreateJob(this.apiToken).JobId;
            this.taskId = this.actions.AddMediaToJob(this.apiToken, this.jobId, fs);
            Assert.AreEqual(32, this.taskId.ToString("N").Length);
        }
    }
}
