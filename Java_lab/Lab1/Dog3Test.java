
import java.awt.Color;
import java.util.*;
/**
 * Title      : DogTest2.java
 * Description: This class contains the test class for Dog.
 * Copyright  : Copyright (c) 2006 - 2017
 * @author  Laurissa Tokarchuk
 * @version 1.0
 * @author  Paula Fonseca
 * @version 1.2
 */
public class DogTest3{
	public static void main(String[] args){
		Dog[] d=new Dog[5];
		d[0]=new Dog("A","short",true,Color.BLACK,400);			
		d[1]=new Dog("B","long",true,Color.WHITE,500);
		d[2]=new Dog("C","short",false,Color.BLACK,300);
		d[3]=new Dog("D","long",true,Color.BLACK,200);
		d[4]=new Dog("E","short",false,Color.BLACK,700);		
			
		
	ArrayList<Dog> Dog1=new ArrayList<Dog>();
	for(int j=0;j<5;j++){
		Dog1.add(d[j]);
	}
	System.out.println(Dog1.get(4));
	System.out.println("The size of the Arraylist is " + Dog1.size());
	Dog1.remove(4);
	System.out.println();
	for(int m=0;m<Dog1.size();m++){
		System.out.println(Dog1.get(m));
	}
	}
}