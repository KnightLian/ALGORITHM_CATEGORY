/*****************************************
 * A template for a computer Nim player
 ****************************************/ 
import java.util.Random;
public class Computer{
    
    private int mode;
    private int choice;
    
    public Computer(int m){
        mode = m;
        choice = -1;
    }
    
    public void move(int marblesLeft){
		
		Random rand = new Random();	
		
		if (mode==1){
			//Computer is stupid and takes random int between 1 and n/2 
			choice = rand.nextInt((marblesLeft/2 - 1) + 1 ) + 1; 	
		}
		else{ 
			//mode == 2
			//Computer is smart and takes random int between 1 and n/2 
			//to make the rest marbles in size 3, 7, 15, 31, or 63	
			if (marblesLeft <=3 ){
				choice = rand.nextInt((marblesLeft/2 - 1) + 1 ) + 1;
			}			
			else {
				for(int i=1; i<=(marblesLeft/2); i++) {
					int whats_left = marblesLeft - i;
					if(whats_left == 3 || 
					   whats_left == 7 || 
					   whats_left == 15 || 
					   whats_left == 31 || 
					   whats_left == 63){
							choice = i;
							break;
					   }					   	
				}				
			}				
		}  
		
    }
    
    public int getChoice(){
        return choice;
    }  
	
}
