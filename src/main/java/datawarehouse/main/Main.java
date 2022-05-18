package datawarehouse.main;

import datawarehouse.common.stringmatching.EditDistanceStringMatchingImpl;
import datawarehouse.common.stringmatching.IStringMatching;

public class Main {
	public static void main(String[] args) {
		IStringMatching stringMatching = new EditDistanceStringMatchingImpl();
		System.out.println(stringMatching.matching("David Smiths", "Davidd Simth"));
	}
}
