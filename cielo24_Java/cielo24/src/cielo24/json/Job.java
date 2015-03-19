package cielo24.json;

import cielo24.utils.Guid;
import cielo24.utils.MicroDate;

import static cielo24.Enums.*;

import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;
import java.util.Hashtable;

public class Job extends JsonBase {
	
    @SerializedName("JobId")
	public Guid jobId;
	@SerializedName("JobName")
	public String jobName;
    @SerializedName("MediaLengthSeconds")
    public Float mediaLengthSeconds;
    @SerializedName("ExternalID")
    public String externalID;
    @SerializedName("Priority")
    public Priority priority;
    @SerializedName("Fidelity")
    public Fidelity fidelity;
    @SerializedName("TurnaroundTimeHours")
    public Integer turnaroundTimeHours;
	@SerializedName("JobStatus")
	public JobStatus jobStatus;
	@SerializedName("SourceLanguage")
	public String sourceLanguage;
	@SerializedName("TargetLanguage")
	public String targetLanguage;
	@SerializedName("CreationDate")
	public MicroDate creationDate;
    @SerializedName("StartDate")
    public MicroDate startDate;
	@SerializedName("DueDate")
	public MicroDate dueDate;
    @SerializedName("CompletedDate")
    public MicroDate completedDate;
    @SerializedName("ReturnTargets")
    public Hashtable<String, ArrayList<Hashtable<String, String>>> returnTargets;
    @SerializedName("Options")
    public Hashtable<String, Hashtable<String, String>> options;
}