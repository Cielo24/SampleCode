using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json;

namespace Cielo24.JSON.ElementList
{
    public class ElementListVersion : JsonBase
    {
        [JsonProperty("version")]
        public DateTime? Version { get; set; }
        [JsonProperty("iwp_name")]
        public string IWPName { get; set; }
    }
}
