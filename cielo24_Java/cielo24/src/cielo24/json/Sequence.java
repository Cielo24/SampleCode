package cielo24.json;

import java.util.List;
import com.google.gson.annotations.SerializedName;

public class Sequence extends JsonBase {
	
    @SerializedName("tokens")
	public List<Token> tokens;
	@SerializedName("interpolated")
	public boolean interpolated;
	@SerializedName("start_time")
	public int startTime;         // Milliseconds
	@SerializedName("end_time")
	public int endTime;           // Milliseconds
	@SerializedName("confidence_score")
	public float confidenceScore;
}