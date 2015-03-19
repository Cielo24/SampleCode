package cielo24.utils.gson;

import java.lang.reflect.Type;

import cielo24.utils.MicroDate;
import com.google.gson.JsonElement;
import com.google.gson.JsonPrimitive;
import com.google.gson.JsonSerializationContext;
import com.google.gson.JsonSerializer;

public class MicroDateSerializer implements JsonSerializer<MicroDate> {

    @Override
    public JsonElement serialize(MicroDate date, Type type, JsonSerializationContext context) {
        return new JsonPrimitive(date.toString());
    }
}