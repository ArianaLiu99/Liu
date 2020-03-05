public class Troll extends Monster{
	public Troll(String name,double probability){
		this.setName(name);
		this.spAttackProbability=probability;
	}
	public Troll(String name){
		this.setName(name);
	}
	public void setName(String name){
		if(name.equals("Saul")||name.equals("Salomon")){
			System.out.println("Error name!The name is set to Detritus.");
		this.name="Detritus";
		}
		else{
			this.name=name;}
		}
	
	public int specialAttack(){
		double num=Math.random();
		int result=0;
		if(num>=this.getspAttackProbability())
			result=attack();
		else if(num<this.getspAttackProbability())
		{
			int x = (int)(Math.random()*15+1);
			System.out.println(this.name+", of type"+this.getClass()+" , attacks by hitting with a club: "+ x +" points damage caused.");
			result=x;
		}
		return result;
	}
	public void move(int direction)	{
		super.move(direction);
	}
		
}
   