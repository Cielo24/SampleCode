using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cielo24.JSON
{
    public class Task : JsonBase
    {
        [JsonProperty("TaskId")]
        public Guid TaskId { get; set; }
        [JsonProperty("TaskType")]
        public TaskType? TaskType { get; set; }
        [JsonProperty("TaskRequestTime")]
        public DateTime? TaskRequestTime { get; set; }
        [JsonProperty("TaskCompletionTime")]
        public DateTime? TaskCompletionTime { get; set; }
        [JsonProperty("TaskInfo")]
        public string TaskInfo { get; set; }
        [JsonProperty("TaskStatus")]
        public TaskStatus? TaskStatus { get; set; }
    }
}
