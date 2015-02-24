package cielo24.json;

import cielo24.utils.Guid;
import cielo24.utils.NanoDate;
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
    public int mediaLengthSeconds;
    @SerializedName("ExternalID")
    public String ExternalID;
    @SerializedName("Priority")
    public Priority priority;
    @SerializedName("Fidelity")
    public Fidelity fidelity;
    @SerializedName("TurnaroundTimeHours")
    public int turnaroundTimeHours;
	@SerializedName("JobStatus")
	public JobStatus jobStatus;
	@SerializedName("SourceLanguage")
	public String sourceLanguage;
	@SerializedName("TargetLanguage")
	public String targetLanguage;
	@SerializedName("CreationDate")
	public NanoDate creationDate;
    @SerializedName("StartDate")
    public NanoDate startDate;
	@SerializedName("DueDate")
	public NanoDate dueDate;
    @SerializedName("CompletedDate")
    public NanoDate CompletedDate;
    @SerializedName("ReturnTargets")
    public Hashtable<String, ArrayList<Hashtable<String, String>>> returnTargets;
    @SerializedName("Options")
    public Hashtable<String, Hashtable<String, String>> options;
}