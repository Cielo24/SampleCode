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
        [JsonProperty("JobStatus")]
        public JobStatus? JobStatus { get; set; }
        [JsonProperty("Priority")]
        public Priority? Priority { get; set; }
        [JsonProperty("Fidelity")]
        public Fidelity? Fidelity { get; set; }
        [JsonProperty("JobLanguage")]
        public string JobLanguage { get; set; }
        [JsonProperty("TargetLanguage")]
        public string TargetLanguage { get; set; }
        [JsonProperty("CreationTime")]
        public DateTime? CreationTime { get; set; }
        [JsonProperty("DueDate")]
        public DateTime? DueDate { get; set; }
        [JsonProperty("TurnaroundTimeHours")]
        public int? TurnaroundTimeHours { get; set; }
        [JsonProperty("StartTime")]
        public DateTime? StartTime { get; set; }
        [JsonProperty("CompletedTime")]
        public DateTime? CompletedTime { get; set; }
    }
}