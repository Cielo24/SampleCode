using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json;

namespace Cielo24.JSON.Job
{
    public class JobList : JsonBase
    {
        [JsonProperty("Username")]
        public string Username { get; set; }
        [JsonProperty("ActiveJobs")]
        public List<Job> ActiveJobs { get; set; }
    }
}
