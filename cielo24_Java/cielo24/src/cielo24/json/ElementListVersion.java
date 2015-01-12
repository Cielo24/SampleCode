package cielo24.json;

import java.util.Date;
import com.google.gson.annotations.SerializedName;

public class ElementListVersion extends JsonBase {
    
	@SerializedName("version")
	public Date version;
	@SerializedName("iwp_name")
	public String iwp;
}