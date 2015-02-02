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
        [JsonProperty("MediaLengthSeconds")]
        public int? MediaLengthSeconds { get; set; }
        [JsonProperty("ExternalID")]
        public String ExternalID { get; set; }
        [JsonProperty("Priority")]
        public Priority? Priority { get; set; }
        [JsonProperty("Fidelity")]
        public Fidelity? Fidelity { get; set; }
        [JsonProperty("TurnaroundTimeHours")]
        public int? TurnaroundTimeHours { get; set; }
        [JsonProperty("JobStatus")]
        public JobStatus? JobStatus { get; set; }
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
        [JsonProperty("ReturnTargets")]
        public Dictionary<String, String> ReturnTargets { get; set; }
        [JsonProperty("Options")]
        public Dictionary<String, String> Options { get; set; }

        // BACKWARD COMPATABILITY //
        [JsonProperty("JobLanguage")]
        [Obsolete("This property is obsolete; use SourceLanguage property instead.")]
        public string JobLanguage { get; set; }
        [JsonProperty("CreationTime")]
        [Obsolete("This property is obsolete; use CreationDate property instead.")]
        public DateTime? CreationTime { get; set; }
        [JsonProperty("StartTime")]
        [Obsolete("This property is obsolete; use StartDate property instead.")]
        public DateTime? StartTime { get; set; }
        [JsonProperty("CompletedTime")]
        [Obsolete("This property is obsolete; use CompletedDate property instead.")]
        public DateTime? CompletedTime { get; set; }
    }
}