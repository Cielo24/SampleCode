using Cielo24.JSON;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cielo24.Options
{
    public class PerformTranscriptionOptions : BaseOptions
    {
        [QueryName("customer_approval_steps")]
        public List<CustomerApprovalStep> CustomerApprovalSteps { get; set; }
        [QueryName("customer_approval_tool")]
        public CustomerApprovalTool? CustomerApprovalTool { get; set; }
        [QueryName("custom_metadata")]
        public string CustomMetadata { get; set; }
        [QueryName("generate_media_intelligence_for_iwp")]
        public bool? GenerateMediaIntelligenceForIWP { get; set; }
        [QueryName("notes")]
        public string Notes { get; set; }
        [QueryName("return_iwp")]
        public List<Fidelity> ReturnIWP { get; set; }
        [QueryName("speaker_id")]
        public bool? SpeakerId { get; set; }

        public PerformTranscriptionOptions(List<CustomerApprovalStep> customerApprovalStep = null,
                                           CustomerApprovalTool? customerApprovalTool = null,
                                           string customMetadata = null,
                                           bool? generateMediaIntelligenceForIWP = null,
                                           string notes = null,
                                           List<Fidelity> returnIWP = null,
                                           bool? speakerId = null)
        {
            this.CustomerApprovalSteps = customerApprovalStep;
            this.CustomerApprovalTool = customerApprovalTool;
            this.CustomMetadata = customMetadata;
            this.GenerateMediaIntelligenceForIWP = generateMediaIntelligenceForIWP;
            this.Notes = notes;
            this.ReturnIWP = returnIWP;
            this.SpeakerId = speakerId;
        }
    }
}
