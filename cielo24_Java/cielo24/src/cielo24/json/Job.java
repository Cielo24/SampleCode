package cielo24.json;

import cielo24.utils.Guid;
import cielo24.utils.NanoDate;
import static cielo24.Enums.*;

import com.google.gson.annotations.SerializedName;

public class Job extends JsonBase {
	@SerializedName("JobId")
	public Guid jobId;
	@SerializedName("JobName")
	public String jobName;
	@SerializedName("JobStatus")
	public JobStatus jobStatus;
	@SerializedName("Priority")
	public Priority priority;
	@SerializedName("Fidelity")
	public Fidelity fidelity;
	@SerializedName("JobLanguage")
	public String jobLanguage;
	@SerializedName("TargetLanguage")
	public String targetLanguage;
	@SerializedName("CreationTime")
	public NanoDate creationTime;
	@SerializedName("DueDate")
	public NanoDate dueDate;
	@SerializedName("TurnaroundTimeHours")
	public int turnaroundTimeHours;
	@SerializedName("StartTime")
	public NanoDate startTime;
	@SerializedName("CompletedTime")
	public NanoDate completedTime;
}