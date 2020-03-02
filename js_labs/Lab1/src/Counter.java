package problem_1;

public class Counter extends Thread{
	public void run(){
		for(int i=10;i<=500;i++){
		System.out.println(i);
		}
	}
}
