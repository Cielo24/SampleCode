package cielo24.options;

import cielo24.utils.NanoDate;
import cielo24.utils.QueryName;
import cielo24.Enums.*;

public class JobListOptions extends BaseOptions {

    @QueryName("CreationDateFrom")
    public NanoDate creationDateFrom = null;
    @QueryName("CreationDateTo")
    public NanoDate creationDateTo = null;
    @QueryName("StartDateFrom")
    public NanoDate startDateFrom = null;
    @QueryName("StartDateTo")
    public NanoDate startDateTo = null;
    @QueryName("DueDateFrom")
    public NanoDate dueDateFrom = null;
    @QueryName("DueDateTo")
    public NanoDate dueDateTo = null;
    @QueryName("CompleteDateFrom")
    public NanoDate completeDateFrom = null;
    @QueryName("CompleteDateTo")
    public NanoDate completeDateTo = null;
    @QueryName("JobStatus")
    public JobStatus jobStatus = null;
    @QueryName("Fidelity")
    public Fidelity fidelity = null;
    @QueryName("Priority")
    public Priority priority = null;
    @QueryName("TurnaroundTimeHoursFrom")
    public Integer turnaroundTimeHoursFrom = null;
    @QueryName("TurnaroundTimeHoursTo")
    public Integer turnaroundTimeHoursTo = null;
    @QueryName("username")
    public String subAccount = null;
}
