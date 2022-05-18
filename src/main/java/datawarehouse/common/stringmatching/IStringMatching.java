package datawarehouse.common.stringmatching;

public interface IStringMatching {
	
	/**
	 * Return score mathing of 2 string str1 and str2
	 * @param str1
	 * @param str2
	 * @return
	 */
	public double matching(String str1, String str2);
}
