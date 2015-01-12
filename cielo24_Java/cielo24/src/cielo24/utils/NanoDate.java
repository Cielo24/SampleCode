package cielo24.utils;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class NanoDate {

	private static final DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS"); // 2014-07-24T14:57:38.138269
	private static String regex = "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{6}$";
	private String nanoSec = "000";
	private Date date = null;

	private NanoDate(Date d, String ns) {
		this.date = d;
		this.nanoSec = ns;
	}

	public static NanoDate parse(String str) throws ParseException {
		Matcher matcher = Pattern.compile(regex).matcher(str);
		if(matcher.matches()){
			String ns = str.substring(str.length() - 3, str.length());
			String d = str.substring(0, str.length() - 3);
			return new NanoDate(dateFormat.parse(d), ns);
		}
		else{
			throw new IllegalArgumentException();
		}
	}

	public String toString() {
		return dateFormat.format(date) + this.nanoSec;
	}
}