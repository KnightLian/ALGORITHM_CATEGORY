import java.util.Arrays;
public class Zipcode{
	
	private String to_num;
	private String to_bar;
	private String report;
	private int report_num;

	//10025
	public Zipcode(int pcode){
		String report="|";
		String to_str = Integer.toString(pcode);
		String[] str_array =  to_str.split("");
		int sum = 0;
		for (int i=0; i<str_array.length; i++){
			bar_convert(str_array[i]);
			report = report + to_bar; 
			int n = Integer.parseInt(str_array[i]); 
			sum += n;
		}
		int o = 1+sum/10;
		int oo = o*10 - sum;	
		bar_convert(Integer.toString(oo));
		report = report + to_bar; 
		report = report + "|";		
		this.report = report;		
	}
	//|:::||||:::||:::::|:|:|:|:::|:||
	public Zipcode(String barcode){	
		String report="";
		String[] str_array =  barcode.split("");
		String[] temp_array = new String[5];		
		for (int i=1; i<(str_array.length-10); i=i+5){
			System.arraycopy(str_array,i,temp_array,0,5);
			String to_str = String.join("",temp_array);
			num_convert(to_str);
			report = report + to_num; 
		}		
		report_num = Integer.valueOf(report);	
	}	

	public String getBarcode(){
		return report;
	}

	public int getZIPcode(){
		return report_num;
	}

	public void bar_convert(String num_in){	
		switch(num_in) {
			case "1":
				to_bar = ":::||";			
				break;
			case "2":
				to_bar = "::|:|";			
				break;
			case "3":
				to_bar = "::||:";			
				break;
			case "4":
				to_bar = ":|::|";			
				break;
			case "5":
				to_bar = ":|:|:";			
				break;
			case "6":
				to_bar = ":||::";				
				break;
			case "7":
				to_bar = "|:::|";			
				break;			
			case "8":
				to_bar = "|::|:";				
				break;	
			case "9":
				to_bar = "|:|::";				
				break;	
			case "0":
				to_bar = "||:::";				
				break;	
			default: 
				to_bar = "Invalid Code";
				break;
		}	
	}
	
	public void num_convert(String bar_in){
		switch(bar_in) {
			case ":::||":
				to_num = "1";			
				break;
			case "::|:|":
				to_num = "2";			
				break;
			case "::||:":
				to_num = "3";			
				break;
			case ":|::|":
				to_num = "4";			
				break;
			case ":|:|:":
				to_num = "5";			
				break;
			case ":||::":
				to_num = "6";				
				break;
			case "|:::|":
				to_num = "7";			
				break;			
			case "|::|:":
				to_num = "8";				
				break;	
			case "|:|::":
				to_num = "9";				
				break;	
			case "||:::":
				to_num = "0";				
				break;	
			default: 
				to_bar = "Invalid Bar";
				break;				
		}	
	}
	
}	
