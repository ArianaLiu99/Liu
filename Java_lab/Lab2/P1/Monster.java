import java.util.Random;
public class Monster{
	protected String name;
	public Monster(String name){
		this.name=name;
	}
	public Monster(){	}
	
	public void setName(String name){
		this.name=name;
	}
	public String getName(){
		return name;
	}
	
	public int attack(){
		int randomNumber=(int)(Math.random()*5);
		System.out.println(this.name + " of type "+this.getClass()+
				", attacks generically: " + randomNumber +
				" points damage caused.");
		return randomNumber;
	}
	
	public void move(int direction) {
		switch(direction) {
		case 1:
		System.out.println(this.name + " is moving 1 step NORTH.");
		break;
		case 2:
		System.out.println(this.name + " is moving 1 step EAST.");
		break;
		case 3:
		System.out.println(this.name + " is moving 1 step SOUTH.");
		break;
		default:
		System.out.println(this.name + " is moving 1 step WEST.");
		break;
		}
		}

}

