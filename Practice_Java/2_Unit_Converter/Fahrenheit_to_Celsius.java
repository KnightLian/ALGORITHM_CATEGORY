/*
Convert from degrees Fahrenheit to degrees Celsius. 
The program should prompt for a temperature in Fahrenheit 
and output a temperature in Celsius. 
 */

import java.util.Scanner;
public class F2C {
    public static final void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Input temperature in Fahrenheit");
        int f = s.nextInt();	
	double c = ( f - 32 ) * (double)5/9 ;
	System.out.println("Output temperature in Celsius: " + (int)c);  
    }     
}
