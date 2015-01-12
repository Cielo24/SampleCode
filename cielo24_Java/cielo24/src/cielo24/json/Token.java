package cielo24.json;

import java.util.List;

import static cielo24.Enums.*;

import com.google.gson.annotations.*;

public class Token extends JsonBase {
	
    @SerializedName("interpolated")
	public boolean interpolated;
	@SerializedName("start_time")
	public int startTime;         // Milliseconds
	@SerializedName("end_time")
	public int endTime;           // Milliseconds
	@SerializedName("value")
	public String value;
	@SerializedName("type")
	public TokenType type;
	@SerializedName("display_as")
	public String typeDisplay;
	@SerializedName("tags")
	public List<Tag> tags;
}