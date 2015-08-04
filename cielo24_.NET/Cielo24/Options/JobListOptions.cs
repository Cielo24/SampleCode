﻿using Cielo24.JSON;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Cielo24.Options
{
    public class JobListOptions : BaseOptions
    {
        [QueryName("CreateDateFrom")]
        public DateTime? CreateDateFrom { get; set; }
        [QueryName("CreateDateTo")]
        public DateTime? CreateDateTo { get; set; }
        [QueryName("StartDateFrom")]
        public DateTime? StartDateFrom { get; set; }
        [QueryName("StartDateTo")]
        public DateTime? StartDateTo { get; set; }
        [QueryName("DueDateFrom")]
        public DateTime? DueDateFrom { get; set; }
        [QueryName("DueDateTo")]
        public DateTime? DueDateTo { get; set; }
        [QueryName("CompleteDateFrom")]
        public DateTime? CompleteDateFrom { get; set; }
        [QueryName("CompleteDateTo")]
        public DateTime? CompleteDateTo { get; set; }
        [QueryName("JobStatus")]
        public JobStatus? JobStatus { get; set; }
        [QueryName("Fidelity")]
        public Fidelity? Fidelity { get; set; }
        [QueryName("Priority")]
        public Priority? Priority { get; set; }
        [QueryName("TurnaroundTimeHoursFrom")]
        public int? TurnaroundTimeHoursFrom { get; set; }
        [QueryName("TurnaroundTimeHoursTo")]
        public int? TurnaroundTimeHoursTo { get; set; }
        [QueryName("JobName")]
        public string JobName { get; set; }
        [QueryName("ExternalId")]
        public string ExternalId { get; set; }
        [QueryName("JobDifficulty")]
        public JobDifficulty? JobDifficulty { get; set; }
        [QueryName("Username")]
        public string SubAccount { get; set; }

        public JobListOptions(DateTime? createDateFrom = null,
                              DateTime? createDateTo = null,
                              DateTime? startDateFrom = null,
                              DateTime? startDateTo = null,
                              DateTime? dueDateFrom = null,
                              DateTime? dueDateTo = null,
                              DateTime? completeDateFrom = null,
                              DateTime? completeDateTo = null,
                              JobStatus? jobStatus = null,
                              Fidelity? fidelity = null,
                              Priority? priority = null,
                              int? turnaroundTimeHoursFrom = null,
                              int? turnaroundTimeHoursTo = null,
                              string jobName = null,
                              string externalId = null,
                              JobDifficulty? jobDifficulty = null,
                              string subAccount = null)
        {
            this.CreateDateFrom = createDateFrom;
            this.CreateDateTo = createDateTo;
            this.StartDateFrom = startDateFrom;
            this.StartDateTo = startDateTo;
            this.DueDateFrom = dueDateFrom;
            this.DueDateTo = dueDateTo;
            this.CompleteDateFrom = completeDateFrom;
            this.CompleteDateTo = completeDateTo;
            this.JobStatus = jobStatus;
            this.Fidelity = fidelity;
            this.Priority = priority;
            this.TurnaroundTimeHoursFrom = turnaroundTimeHoursFrom;
            this.TurnaroundTimeHoursTo = turnaroundTimeHoursTo;
            this.JobName = jobName;
            this.ExternalId = externalId;
            this.JobDifficulty = jobDifficulty;
            this.SubAccount = subAccount;
        }
    }
}
