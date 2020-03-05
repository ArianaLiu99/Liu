public abstract class Monster { 
	protected String name;
	protected double spAttackProbability=0.2;
	public Monster(String name,double probability){
		this.name=name;
		this.spAttackProbability=probability;
	}  
	public Monster(){		}
	public void setName(String name){
		this.name=name;  }
	public String getName(){
		return name;  }
	public void setspAttackProbability(double spAttackProbability){
		this.spAttackProbability=spAttackProbability;}
	public double getspAttackProbability(){
		return spAttackProbability;}
	
	public final int attack(){
		int x = (int)(Math.random()*5+1);
		System.out.println(this.name+", of type"+this.getClass()+" , attacks generically: "+ x +" points damage caused.");
		return x;
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
	public abstract int specialAttack();

}   

