package cielo24.json;

import java.util.List;
import com.google.gson.annotations.SerializedName;

public class Segment extends JsonBase {

    @SerializedName("sequences")
    public List<Sequence> sequences;
    @SerializedName("speaker_change")
    public Boolean speakerChange;
    @SerializedName("speaker_id")
    public Boolean speakerId;
    @SerializedName("interpolated")
    public Boolean interpolated;
    @SerializedName("start_time")
    public Integer startTime;
    @SerializedName("end_time")
    public Integer endTime;
}