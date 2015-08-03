using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json;

namespace Cielo24.JSON.ElementList
{
    public class Token : JsonBase
    {
        [JsonProperty("interpolated")]
        public bool? Interpolated { get; set; }
        [JsonProperty("start_time")]
        public int? StartTime { get; set; }      // Milliseconds
        [JsonProperty("end_time")]
        public int? EndTime { get; set; }        // Milliseconds
        [JsonProperty("value")]
        public string Value { get; set; }
        [JsonProperty("type")]
        public TokenType? Type { get; set; }
        [JsonProperty("display_as")]
        public string DisplayValue { get; set; }
        [JsonProperty("tags")]
        public List<Tag?> Tags { get; set; }
        [JsonProperty("style")]
        public string Style { get; set; }
    }
}