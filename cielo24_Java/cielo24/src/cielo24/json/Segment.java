package cielo24.json;

import java.util.List;
import com.google.gson.annotations.SerializedName;

public class Segment extends JsonBase {
	
    @SerializedName("sequences")
	public List<Sequence> sequences;
	@SerializedName("speaker_change")
	public boolean speakerChange;
	@SerializedName("speaker_id")
	public boolean speakerId;
	@SerializedName("interpolated")
	public boolean interpolated;
	@SerializedName("start_time")
	public int startTime;
	@SerializedName("end_time")
	public int endTime;
}