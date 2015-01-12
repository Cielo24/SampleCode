package cielo24.utils;

import java.util.ArrayList;

@SuppressWarnings("serial")
public class Dictionary<K, V> extends ArrayList<KeyValuePair<K, V>> {

	public void add(K k, V v) {
		this.add(new KeyValuePair<K, V>(k, v));
	}

	public static <K, V> Dictionary<K, V> empty() {
		return new Dictionary<K, V>();
	}

	public void merge(Dictionary<K, V> dict) {
		for (KeyValuePair<K, V> pair : dict) {
			this.add(pair.getKey(), pair.getValue());
		}
	}
}