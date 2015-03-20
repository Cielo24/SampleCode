package cielo24.json;

import cielo24.utils.MicroDate;
import com.google.gson.annotations.SerializedName;

public class ElementListVersion extends JsonBase {
    
    @SerializedName("version")
    public MicroDate version;
    @SerializedName("iwp_name")
    public String iwp;
}