package datawarehouse.common.stringmatching;

public class EditDistanceStringMatchingImpl implements IStringMatching{
	
	public double matching(String str1, String str2) {
		int distance = this.distance(str1, str2);
		int lens1 = str1.length();
		int lens2 = str2.length();
		
		return 1 - (double) distance / Math.max(lens1, lens2);
	}
	
	/**
	 * Method is calculator distance let str1 to str2 with 3 operator delete character, 
	 * insert character or substitute a character with another
	 * @param str1
	 * @param str2
	 * @return
	 */
	public int distance(String str1, String str2) {
		int lens2 = str2.length();
		
		int total = 0;
		
		for(int i=0; i<lens2; i++) {
			char ch1 = str1.charAt(i);
			char ch2 = str2.charAt(i);
			
			if(ch1 != ch2) {
				total++;
				if(ch1 == ' ' && ch2 != ' ') {
					str1 = "0" + str1;
				} else if(ch1 != ' ' && ch2 == ' ') {
					str1 = str1.substring(1);
				}
			}
		}
		
		int lens1 = str1.length();
		total += lens1 - lens2;
		
		return total;
	}
	
}
