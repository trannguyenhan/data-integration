package datawarehouse.common.stringmatching;

public class EditDistanceStringMatchingImpl implements IStringMatching{
	public double matching(String str1, String str2) {
		return 0;
	}
	
	/**
	 * Method is calculator distance let str1 to str2 with 3 operator delete character, 
	 * insert character or substitute a character with another
	 * @param str1
	 * @param str2
	 * @return
	 */
	public int distance(String str1, String str2) {
		int total = 0;
		int lens2 = str2.length();
		
		for(int i=0; i<lens2; i++) {
			if(str1.charAt(i) != str2.charAt(i)) {
				
			}
		}
		
		return 0;
	}
	
}
