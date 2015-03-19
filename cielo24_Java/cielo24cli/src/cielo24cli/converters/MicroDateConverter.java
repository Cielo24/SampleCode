package cielo24cli.converters;

import java.text.ParseException;

import cielo24.utils.MicroDate;

import com.beust.jcommander.IStringConverter;

public class MicroDateConverter implements IStringConverter<MicroDate> {
	@Override
	public MicroDate convert(String arg) {
		try {
			return MicroDate.parse(arg);
		} catch (ParseException e) {
			return null;
		}
	}
}