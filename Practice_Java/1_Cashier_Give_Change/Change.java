/** 
Implement a program that directs a cashier how to give change. 

The program has two inputs: 
the amount due and the amount received form the customer.

Display the dollars, quarters, dimes, nickels, and pennies 
that the customer should receive in return. 
 */
 
import java.util.Scanner;

public class Change {
    
    public static final void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Input the amount of due");
		double due = s.nextDouble();
        System.out.println("Input the amount of received");
		double rec = s.nextDouble();

		double change = rec - due;
		
		if (change < 0){
			System.out.println("Please pay the total due");
		}
		else {
			
			if ((int)change == 0){
				int inqua = (int) (change/0.25);
				double left1 = change%0.25;
				int indim = (int) (left1/0.10);
				double left2 = left1%0.10;
				int innick = (int) (left2/0.05);
				double left3 = left2%0.05;
				int inpenn = (int) Math.round(left3*100);				
				System.out.println("Change in " + inqua + 
				" quarters, " + indim + " dims, " + innick +
				" nickels, " + inpenn + " pennies.");								
			}
			else{
				int indol = (int) change;
				double left0 = change%1;								
				int inqua = (int) (left0/0.25);
				double left1 = left0%0.25;
				int indim = (int) (left1/0.10);
				double left2 = left1%0.10;
				int innick = (int) (left2/0.05);
				double left3 = left2%0.05;
				int inpenn = (int) Math.round(left3*100);				
				System.out.println(				
				"Change in " 
				 + indol + " dollars, "+ 
				+ inqua + " quarters, " 
				+ indim + " dims, " + innick +
				" nickels, " + inpenn + " pennies.");	
			}
				
			
        }
    }
}
