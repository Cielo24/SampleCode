using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cielo24.JSON.ElementList
{
    public class TimeRange
    {
        [JsonProperty("start_time")]
        public int? StartTime { get; set; }      // Milliseconds
        [JsonProperty("end_time")]
        public int? EndTime { get; set; }        // Milliseconds
    }
}
