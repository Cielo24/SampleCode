using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cielo24.JSON.ElementList
{
    public class ElementList : JsonBase
    {
        [JsonProperty("version")]
        public int? Version { get; set; }
        [JsonProperty("start_time")]
        public int? StartTime { get; set; }      // Milliseconds
        [JsonProperty("end_time")]
        public int? EndTime { get; set; }        // Milliseconds
        [JsonProperty("language")]
        public string Language { get; set; }
        [JsonProperty("segments")]
        public List<Segment> Segments { get; set; }
        [JsonProperty("speakers")]
        public List<Speaker> Speakers { get; set; }
        [JsonProperty("keywords")]
        public Dictionary<String, MetaToken> Keywords { get; set; }
        [JsonProperty("topics")]
        public Dictionary<String, MetaToken> Topics { get; set; }
        [JsonProperty("entities")]
        public Dictionary<String, MetaToken> Entities { get; set; }
    }
}