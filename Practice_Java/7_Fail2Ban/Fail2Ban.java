  /* $ java Fail2Ban logs_processed.txt output.txt
 * The list of IP addresses that have failed 3 or more times should appear in the output.txt file.
*/
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashSet; 

public class Fail2Ban {
    public static final void main (String[] args) throws
    FileNotFoundException {
        File f = new File(args[0]);
        PrintWriter out = new PrintWriter(args[1]);        
        Scanner s = new Scanner(f);    
        ArrayList<String> Invalid_IP = new ArrayList<>();
        while(s.hasNextLine()){
            String line = s.nextLine();
            String[] tokens = line.split(" ");            
            for (String i:tokens){                               
                if (i.equals("Invalid")){ 
                    Invalid_IP.add(tokens[tokens.length-1]);   
                    break;
                }
            } 
        }
         
        HashSet<String> unique_IP = new HashSet<>(Invalid_IP);
                
        for (String j:unique_IP){
            int count = 0;            
            for (String k:Invalid_IP){
                if(j.equals(k)){
                    count++;
                }
            }
            if (count>=3) {
                out.println(j); 
            }                                   
        }
              
        s.close();  
        out.close();                               
    }
}
