import java.util.Random;
public class Dragon extends Monster{
	public Dragon(String name){
		super(name);
	}

	public int attack(){
		double num=Math.random();
		if(num<0.3)
		    return this.breathingFire();
		else
			return super.attack();
	}
	
	public void move(int direction){
		super.move(direction);
	}
	
	public int breathingFire(){
		int randomNumber=(int)(Math.random()*50);
		System.out.println(this.name + " of type "+this.getClass()+
				", attacks in breathing fire: " + randomNumber +
				" points damage caused.");
		return randomNumber;
	}
}
