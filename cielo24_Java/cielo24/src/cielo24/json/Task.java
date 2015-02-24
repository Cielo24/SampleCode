package cielo24.json;

import cielo24.utils.Guid;
import cielo24.utils.MicroDate;

import static cielo24.Enums.*;

import com.google.gson.annotations.SerializedName;

public class Task extends JsonBase {
	
    @SerializedName("TaskId")
	public Guid taskId;
	@SerializedName("TaskType")
	public TaskType taskType;
	@SerializedName("TaskRequestTime")
	public MicroDate taskRequestTime;
	@SerializedName("TaskCompletionTime")
	public MicroDate taskCompletionTime;
	@SerializedName("TaskInfo")
	public String taskInfo;
	@SerializedName("TaskStatus")
	public TaskStatus taskStatus;
}