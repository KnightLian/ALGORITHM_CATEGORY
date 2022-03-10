/** 
Create an application in Java that asks a user for 
a number of hours, days, weeks, and years. 
It then computes the equivalent number of minutes
 */

import java.util.Scanner;

public class Minutes {
    	
    public static final void main(String[] args) {

        Scanner s = new Scanner(System.in);
		System.out.println("Input a unit in hours, days, weeks, or years");
		String t = s.nextLine();
		
		double intime;
		double outtime;		
		
		switch(t) {
			case "hours":
				System.out.println("Input hours");				
				intime = s.nextDouble();
				outtime = intime*60;
				System.out.println("equivalent in minutes: " + outtime);
				break;
			case "days":
				System.out.println("Input days");
				intime = s.nextDouble();
				outtime = intime*60*24;
				System.out.println("equivalent in minutes: " + outtime);											
				break;
			case "weeks":
				System.out.println("Input weeks");
				intime = s.nextDouble();
				outtime = intime*60*24*7;
				System.out.println("equivalent in minutes: " + outtime);								
				break;
			case "years":
				System.out.println("Input years");
				intime = s.nextDouble();
				outtime = intime*60*24*365;
				System.out.println("equivalent in minutes: " + outtime);						
				break;				
			default:
				System.out.println("Input wrong unit");
			
		}
		
	}
}
