public class Dragon extends Monster{
	public Dragon(String name,double probability){
		this.name=name;
		this.spAttackProbability=probability;
	}
	public Dragon(String name){
		this.name=name;
	}
	public int specialAttack(){
		double num=Math.random();
		int result=0;
		if(num>=this.getspAttackProbability())
			result=attack();
		else if(num<this.getspAttackProbability())
		{
			int x = (int)(Math.random()*50+1);
			System.out.println(this.name+", of type"+this.getClass()+" , attacks by breathing fire: "+ x +" points damage caused.");
			result=x;
		}
		return result;
	}
	
	
	public void move(int direction){
		super.move(direction);
	}

}
 