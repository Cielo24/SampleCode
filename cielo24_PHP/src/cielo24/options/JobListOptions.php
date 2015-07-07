<?php

require_once("BaseOptions.php");

class JobListOptions extends BaseOptions
{
    public $CreateDateFrom;
    public $CreateDateTo;
    public $StartDateFrom;
    public $StartDateTo;
    public $DueDateFrom;
    public $DueDateTo;
    public $CompleteDateFrom;
    public $CompleteDateTo;
    public $JobStatus;
    public $Fidelity;
    public $Priority;
    public $TurnaroundTimeHoursFrom;
    public $TurnaroundTimeHoursTo;
    public $JobName;
    public $ExternalID;
    public $JobDifficulty;
    public $Username;

    public function __construct(DateTime $createDateFrom = null,
                                DateTime $createDateTo = null,
                                DateTime $startDateFrom = null,
                                DateTime $startDateTo = null,
                                DateTime $dueDateFrom = null,
                                DateTime $dueDateTo = null,
                                DateTime $completeDateFrom = null,
                                DateTime $completeDateTo = null,
                                $jobStatus = null,
                                $fidelity = null,
                                $priority = null,
                                $turnaroundTimeHoursFrom = null,
                                $turnaroundTimeHoursTo = null,
                                $jobName = null,
                                $externalId = null,
                                $jobDifficulty = null,
                                $subAccount = null)
    {
        $this->CreateDateFrom = $createDateFrom;
        $this->CreateDateTo = $createDateTo;
        $this->StartDateFrom = $startDateFrom;
        $this->StartDateTo = $startDateTo;
        $this->DueDateFrom = $dueDateFrom;
        $this->DueDateTo = $dueDateTo;
        $this->CompleteDateFrom = $completeDateFrom;
        $this->CompleteDateTo = $completeDateTo;
        $this->JobStatus = $jobStatus;
        $this->Fidelity = $fidelity;
        $this->Priority = $priority;
        $this->TurnaroundTimeHoursFrom = $turnaroundTimeHoursFrom;
        $this->TurnaroundTimeHoursTo = $turnaroundTimeHoursTo;
        $this->JobName = $jobName;
        $this->ExternalID = $externalId;
        $this->JobDifficulty = $jobDifficulty;
        $this->Username = $subAccount;
    }
}
