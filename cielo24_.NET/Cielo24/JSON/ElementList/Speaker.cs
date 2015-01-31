using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json;

namespace Cielo24.JSON.ElementList
{
    public class Speaker : JsonBase
    {
        [JsonProperty("name")]
        public string Name { get; set; }
        [JsonProperty("id")]
        public int? Id { get; set; }
        [JsonProperty("gender")]
        public SpeakerGender? Gender { get; set; }
    }
}