using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json;

namespace Cielo24.JSON.ElementList
{
    public class Sequence : JsonBase
    {
        [JsonProperty("interpolated")]
        public bool? Interpolated { get; set; }
        [JsonProperty("start_time")]
        public int? StartTime { get; set; }      // Milliseconds
        [JsonProperty("end_time")]
        public int? EndTime { get; set; }        // Milliseconds
        [JsonProperty("confidence_score")]
        public float? ConfidenceScore { get; set; }
        [JsonProperty("tokens")]
        public List<Token> Tokens { get; set; }
        [JsonProperty("style")]
        public string Style { get; set; }
    }
}