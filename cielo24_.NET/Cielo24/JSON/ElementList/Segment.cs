using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json;

namespace Cielo24.JSON.ElementList
{
    public class Segment : JsonBase
    {
        [JsonProperty("speaker_change")]
        public bool? SpeakerChange { get; set; }
        [JsonProperty("speaker_id")]
        public int? SpeakerId { get; set; }
        [JsonProperty("interpolated")]
        public bool? Interpolated { get; set; }
        [JsonProperty("start_time")]
        public int? StartTime { get; set; }
        [JsonProperty("end_time")]
        public int? EndTime { get; set; }
        [JsonProperty("sequences")]
        public List<Sequence> Sequences { get; set; }
        [JsonProperty("style")]
        public string Style { get; set; }
    }
}
