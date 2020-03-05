
public class ParityBitAdder {
	public static void main(String[] args){
		ParityBitAdder adder = new ParityBitAdder();
		adder.calculateParity(args[0],args[1]);
	}
	
	public void calculateParity(String m, String n){
		int a=0;int b=0;int c=0;int d=0;
		int num = Integer.parseInt(n);
		switch(num){
		case 0:
		{
			for(int i=0;i<m.length();i++){				
				if(m.substring(i, i+1).equals("0"))
					a++;
				else if(m.substring(i,i+1).equals("1"))
					b++;
			}
			if(a%2!=0)
				System.out.println("Adding even parity to กฎ"+m+"กฏ results in the binary pattern กฎ"+"0"+m+"'.");
			else if(b%2!=0)
				System.out.println("Adding even parity to กฎ"+m+"กฏ results in the binary pattern กฎ"+"1"+m+"'.");
				
			break;
		}
		case 1:
		{
			for(int j=0;j<m.length();j++){
				if(m.substring(j,j+1).equals("0"))
					c++;
				else if(m.substring(j,j+1).equals("1"))
					d++;			
			}
			if(c%2==0)
				System.out.println("Adding odd parity to กฎ"+m+"กฏ results in the binary pattern กฎ"+"0"+m+"'.");
			else if(d%2==0)
				System.out.println("Adding odd parity to กฎ"+m+"กฏ results in the binary pattern กฎ"+"1"+m+"'.");
			break;
		}
		}
	}

}
