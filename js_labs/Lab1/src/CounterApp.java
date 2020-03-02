package problem_1;

public class CounterApp {

	public static void main(String[] args) {
		Counter a=new Counter();
		Runnable runnable=new SleepyCounter();
		Thread b=new Thread(runnable);
		a.start();
		b.start();

	}

}
