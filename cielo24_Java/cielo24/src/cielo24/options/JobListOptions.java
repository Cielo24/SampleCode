package cielo24.options;

import cielo24.utils.MicroDate;
import cielo24.utils.QueryName;
import cielo24.Enums.*;

public class JobListOptions extends BaseOptions {

    @QueryName("CreationDateFrom")
    public MicroDate creationDateFrom = null;
    @QueryName("CreationDateTo")
    public MicroDate creationDateTo = null;
    @QueryName("StartDateFrom")
    public MicroDate startDateFrom = null;
    @QueryName("StartDateTo")
    public MicroDate startDateTo = null;
    @QueryName("DueDateFrom")
    public MicroDate dueDateFrom = null;
    @QueryName("DueDateTo")
    public MicroDate dueDateTo = null;
    @QueryName("CompleteDateFrom")
    public MicroDate completeDateFrom = null;
    @QueryName("CompleteDateTo")
    public MicroDate completeDateTo = null;
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
