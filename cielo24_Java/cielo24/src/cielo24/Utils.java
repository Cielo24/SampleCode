package cielo24;

import java.io.UnsupportedEncodingException;
import java.lang.reflect.Type;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Hashtable;

import cielo24.utils.MicroDate;
import com.google.common.base.Joiner;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import cielo24.json.ElementListVersion;
import cielo24.utils.Guid;
import cielo24.utils.gson.MicroDateDeserializer;
import cielo24.utils.gson.MicroDateSerializer;
import cielo24.utils.gson.GuidDeserializer;
import cielo24.utils.gson.GuidSerializer;

public class Utils {

	public static final Type hashMapType = new TypeToken<HashMap<String, String>>() {}.getType();
	public static final Type listELType = new TypeToken<ArrayList<ElementListVersion>>() {}.getType();
	//public static final DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSSSS"); // 2014-07-24T14:57:38.138269

	/* Concatenates baseURL, actionPath and key-value pairs from the dictionary, returning a URL */
	public static URL buildURL(String baseURL, String actionPath, Hashtable<String, String> dictionary) throws MalformedURLException {
		String urlString = baseURL + actionPath + "?" + toQuery(dictionary);
		return new URL(urlString);
	}

	/* Creates a query String from key-value pairs in the dictionary */
	public static String toQuery(Hashtable<String, String> dictionary) {
		if (dictionary == null) {
			return "";
		}
		ArrayList<String> pairs = new ArrayList<String>();
		for (String key : dictionary.keySet()) {
			pairs.add(key + "=" + dictionary.get(key));
		}
		return Joiner.on("&").join(pairs);
	}

	/* Deserializes given JSON into an object of type T */
	public static <T> T deserialize(String json, Type type) {
		Gson gson = getCustomGson();
		return gson.fromJson(json, type);
	}

	/* Custom Gson for (de)serializing custom classes */
	public static Gson getCustomGson() {
		return new GsonBuilder()
				.registerTypeAdapter(Guid.class, new GuidDeserializer())
				.registerTypeAdapter(Guid.class, new GuidSerializer())
				.registerTypeAdapter(MicroDate.class, new MicroDateDeserializer())
				.registerTypeAdapter(MicroDate.class, new MicroDateSerializer())
				.setPrettyPrinting().create();
	}

	/* Encodes the supplied Url into an escaped format */
	public static String encodeUrl(URL url) throws UnsupportedEncodingException {
		return URLEncoder.encode(url.toString(), "UTF-8");
	}

	/* Unescapes a String */
	public static String unescapeUrl(String urlString) throws UnsupportedEncodingException {
		return URLDecoder.decode(urlString, "UTF-8");
	}

	/*
	 * Joins list with delimiter, adding quotes around every element (result of
	 * the form ["item 1", "item2", "item 3"])
	 */
	public static String joinQuoteList(ArrayList<?> list, String delimeter) {
		ArrayList<String> stringList = new ArrayList<String>();
		for (int i = 0; i < list.size(); i++) {
			stringList.add("\"" + list.get(i).toString() + "\""); // Add quotation marks
		}
		return "[" + Joiner.on(delimeter).join(stringList) + "]";
	}

	public static String joinCharArray(char[] array, String delimeter) {
		ArrayList<String> stringList = new ArrayList<String>();
		for (char c : array) {
			stringList.add(Character.toString(c)); // Add quotation marks
		}
		return "(" + Joiner.on(delimeter).join(stringList) + ")";
	}
}