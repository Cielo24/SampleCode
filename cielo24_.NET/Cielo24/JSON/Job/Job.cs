using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json;

namespace Cielo24.JSON.Job
{
    public class Job : JsonBase
    {
        [JsonProperty("JobId")]
        public Guid JobId { get; set; }
        [JsonProperty("JobName")]
        public string JobName { get; set; }
        [JsonProperty("Username")]
        public string Username { get; set; }  // Only used in GetJobList() call
        [JsonProperty("MediaLengthSeconds")]
        public float? MediaLengthSeconds { get; set; }
        [JsonProperty("ExternalID")]
        public String ExternalID { get; set; }
        [JsonProperty("Priority")]
        public Priority? Priority { get; set; }
        [JsonProperty("Fidelity")]
        public Fidelity? Fidelity { get; set; }
        [JsonProperty("JobStatus")]
        public JobStatus JobStatus { get; set; }
        [JsonProperty("SourceLanguage")]
        public string SourceLanguage { get; set; }
        [JsonProperty("TargetLanguage")]
        public string TargetLanguage { get; set; }
        [JsonProperty("CreationDate")]
        public DateTime? CreationDate { get; set; }
        [JsonProperty("StartDate")]
        public DateTime? StartDate { get; set; }
        [JsonProperty("DueDate")]
        public DateTime? DueDate { get; set; }
        [JsonProperty("CompletedDate")]
        public DateTime? CompletedDate { get; set; }
        [JsonProperty("ReturnDate")]
        public DateTime? ReturnDate { get; set; }
        [JsonProperty("AuthorizationDate")]
        public DateTime? AuthorizationDate { get; set; }
        [JsonProperty("JobDiffiulty")]
        public JobDifficulty? JobDiffiulty { get; set; }
        [JsonProperty("ReturnTargets")]
        public Dictionary<String, List<Dictionary<String, Object>>> ReturnTargets { get; set; }
        [JsonProperty("Options")]
        public Dictionary<String, Dictionary<String, Object>> Options { get; set; }
    }
}