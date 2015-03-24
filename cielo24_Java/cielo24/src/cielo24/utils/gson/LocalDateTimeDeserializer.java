package cielo24.utils.gson;

import java.lang.reflect.Type;
import java.util.logging.Level;
import java.util.logging.Logger;

import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonParseException;

import javax.time.calendar.LocalDateTime;

public class LocalDateTimeDeserializer implements JsonDeserializer<LocalDateTime> {

    @Override
    public LocalDateTime deserialize(JsonElement json, Type type, JsonDeserializationContext context) throws JsonParseException {
        try {
            return LocalDateTime.parse(json.getAsString());
        } catch (Exception e) { // return null if cannot parse
            Logger.getGlobal().log(Level.WARNING, "Could not deserialize Date: " + json.getAsString());
            return null;
        }
    }
}