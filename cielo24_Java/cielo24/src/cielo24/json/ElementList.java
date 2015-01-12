package cielo24.json;

import java.util.List;
import com.google.gson.annotations.SerializedName;

public class ElementList extends JsonBase {
    
	@SerializedName("version")
	public int version;
	@SerializedName("start_time")
	public int startTime;         // Milliseconds
	@SerializedName("end_time")
	public int endTime;           // Milliseconds
	@SerializedName("language")
	public String language;
	@SerializedName("segments")
	public List<Segment> segments;
	@SerializedName("speakers")
	public List<Speaker> speakers;
}