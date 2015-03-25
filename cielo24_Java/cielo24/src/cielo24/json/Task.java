package cielo24.json;

import cielo24.utils.Guid;

import static cielo24.Enums.*;

import com.google.gson.annotations.SerializedName;

import javax.time.calendar.LocalDateTime;

public class Task extends JsonBase {
    
    @SerializedName("TaskId")
    public Guid taskId;
    @SerializedName("TaskType")
    public TaskType taskType;
    @SerializedName("TaskRequestTime")
    public LocalDateTime taskRequestTime;
    @SerializedName("TaskCompletionTime")
    public LocalDateTime taskCompletionTime;
    @SerializedName("TaskInfo")
    public String taskInfo;
    @SerializedName("TaskStatus")
    public TaskStatus taskStatus;
}