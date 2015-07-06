using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cielo24.JSON.ElementList
{
    public class MetaToken
    {
        [JsonProperty("display_name")]
        public string DisplayName { get; set; }
        [JsonProperty("url")]
        public Uri Uri { get; set; }
        [JsonProperty("time_ranges")]
        public List<TimeRange> TimeRanges { get; set; }
    }
}
