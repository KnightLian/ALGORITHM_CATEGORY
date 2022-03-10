/*****************************************
 * A template for a Nim game
 ****************************************/ 
import java.util.Random;
public class Game{
    
    private int marbles;
    private Human humanPlayer;
    private Computer computerPlayer;
    private int turn;
    private int difflevel;
    private int takes;
    
    public Game(int difficulty){
		Random rand = new Random();	

		difflevel = difficulty;
		if (difflevel == 1)
			System.out.println("1: Computer plays stupid!");
		else 
			System.out.println("2: Computer plays smart!");	

		int inirand = rand.nextInt((100 - 10) + 1) + 10;
		marbles = inirand;
		System.out.println("Initial marbles: " + marbles);
		
		turn = rand.nextInt((1 - 0) + 1) + 0;
		if (turn ==0)			
			System.out.println("Computer plays first!");				
		else
			System.out.println("Human plays first!");
		System.out.println("###########################");		
    }
    
    public void play(){
		Random rand = new Random();	
		computerPlayer = new Computer(difflevel);
		humanPlayer = new Human();
		
		while (marbles > 0){
			System.out.println("Current marbles: " + marbles);
			
			if (turn == 0){
				computerPlayer.move(marbles);
				takes = computerPlayer.getChoice();
				System.out.println("Computer takes "+takes);
			}
			else{	
				humanPlayer.move();
				takes = humanPlayer.getChoice();						
			}
			marbles = marbles - takes;
			turn_switch();
			System.out.println("---------------------------");	
		}

		if (turn == 0){
			System.out.println("Computer Wins!");
		}
		else{	
			System.out.println("Human Wins!");					
		}	
		
    }
	
    public void turn_switch(){
		if (turn == 1){
			turn = 0;
		}
		else if (turn == 0){
			turn = 1;
		}
		else{
			System.out.println("Error, Please Rerun");				
		}	
	}
		
}
