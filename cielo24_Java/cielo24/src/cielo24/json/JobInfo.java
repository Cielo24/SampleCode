package cielo24.json;

import cielo24.utils.Guid;
import java.util.ArrayList;
import com.google.gson.annotations.SerializedName;

public class JobInfo extends JsonBase {
	
    @SerializedName("JobId")
	public Guid jobId;
	@SerializedName("JobName")
	public String jobName;
	@SerializedName("Language")
	public String language;
	@SerializedName("Tasks")
	public ArrayList<Task> tasks;
}