package cielo24.json;

import cielo24.utils.Guid;
import cielo24.utils.NanoDate;
import static cielo24.Enums.*;

import com.google.gson.annotations.SerializedName;

public class Task extends JsonBase {
	
    @SerializedName("TaskId")
	public Guid taskId;
	@SerializedName("TaskType")
	public TaskType taskType;
	@SerializedName("TaskRequestTime")
	public NanoDate taskRequestTime;
	@SerializedName("TaskCompletionTime")
	public NanoDate taskCompletionTime;
	@SerializedName("TaskInfo")
	public String taskInfo;
	@SerializedName("TaskStatus")
	public TaskStatus taskStatus;
}