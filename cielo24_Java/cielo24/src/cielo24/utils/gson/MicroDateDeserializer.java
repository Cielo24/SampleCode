package cielo24.utils.gson;

import java.lang.reflect.Type;
import java.text.ParseException;
import java.util.logging.Level;
import java.util.logging.Logger;

import cielo24.utils.MicroDate;

import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonParseException;

public class MicroDateDeserializer implements JsonDeserializer<MicroDate> {

    @Override
    public MicroDate deserialize(JsonElement json, Type type, JsonDeserializationContext context) throws JsonParseException {
        if (json.getAsString().equals("")) {
            return null;
        } else {
            try {
                return MicroDate.parse(json.getAsString());
            } catch (ParseException e) {
                Logger.getGlobal().log(Level.WARNING, "Could not deserialize Date: " + json.getAsString());
                return null;
            }
        }
    }
}