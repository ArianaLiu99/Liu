
import java.io.Serializable;

public class Patient implements Serializable{
	public int yearOfBirth;
	public String ID,name;
	public Patient(){}
	public Patient(String ID,String name,int yearOfBirth){
		this.ID=ID;
		this.yearOfBirth=yearOfBirth;
		this.name=name;
	}
	public String getID(){
		return ID;
	}
	public int getyearOfBirth(){
		return yearOfBirth;
	}
	public String getName(){
		return name;
	}
	public String toString(){
		return("ID: "+ID+" Name: "+ name+" Year of birth: "+yearOfBirth);
	}

}
