/*
The Drunkard’s (Random) Walk. 
Imagine you live on an infinite grid of streets where locations are represented as integer pairs (avenue,street). 

The drunkard’s current avenue (x loc) and current street (y loc). 
step( ) that moves the drunkard to the next randomly chosen adjacent intersection. 

fastForward(int steps) that takes an integer as a parameter (call it steps) and 
moves the drunkard steps intersections from his current location.

getLocation( ) that returns a String indicating the drunkard’s current location. 

howFar( ) that reports the drunkards distance in blocks from where he started calculated using the Manhattan distance metric.
*/

public class Drunkard{
    private int xloc;
    private int yloc;
    private int xlocorg;
    private int ylocorg;	
  
    public Drunkard(int avenue,int street){
        xloc = avenue;          
        yloc = street; 
		
        xlocorg = avenue;          
        ylocorg = street; 		
    }
    
    public void step(){
		double rand = Math.random();
		double rand2 = Math.random();		
		if (rand<0.5){
			if (rand2<0.5)
				xloc++;
			else
				xloc--;
		}
		else{
			if (rand2<0.5)
				yloc++;
			else
				yloc--;
		}	
    }   
	
	public void fastForward(int steps){
		for (int i=0; i<steps; i++)
			step();
    }
	
	public String getLocation(){
		String xlocStr = Integer.toString(xloc);
		String ylocStr = Integer.toString(yloc);
		return xlocStr+ ", "+ ylocStr ;		
	}

	public int howFar(){
        int Mdist = Math.abs(xloc-xlocorg)+Math.abs(yloc-ylocorg); 
		return Mdist;		
	}
}    


