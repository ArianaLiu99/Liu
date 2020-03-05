public class Troll extends Monster{
	public Troll(String name){
		this.setName(name);
	}
	public void setName(String name){
		if(name.equals("Saul")||name.equals("Salomon")){
		System.out.println("Error name!The name is set as 'Detritus'.");
		this.name="Detritus";
		}
		else{
			this.name=name;
		}
		
	}
	
	public int attack(){
		return super.attack();
	}
	
	public void move(int direction){
		super.move(direction);
	}
	
}