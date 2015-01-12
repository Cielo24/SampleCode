package cielo24.options;

import cielo24.utils.NanoDate;
import cielo24.Enums.*;

public class JobListOptions extends BaseOptions {
    
    public NanoDate CreationDateFrom = null;
    public NanoDate CreationDateTo = null;
    public NanoDate StartDateFrom = null;
    public NanoDate StartDateTo = null;
    public NanoDate DueDateFrom = null;
    public NanoDate DueDateTo = null;
    public NanoDate CompleteDateFrom = null;
    public NanoDate CompleteDateTo = null;
    public JobStatus JobStatus = null;
    public Fidelity Fidelity = null;
    public Priority Priority = null;
    public Integer TurnaroundTimeHoursFrom = null;
    public Integer TurnaroundTimeHoursTo = null;
    public String username = null;
}
