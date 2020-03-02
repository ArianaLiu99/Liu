import java.awt.*;
import java.awt.event.ActionListener;
import javax.swing.*;
import java.awt.event.*;
/**
 * Title      : JungleParty1.java
 * Description: This class contains the code of the game JungleParty.
 * Copyright  : 
 * date 2017-5-26
 * @author  Liu Bingqing  Student Number:151011070(QM) 2015213107(BUPT) class:2015215109
 * @version 1.0
 */

public class JungleParty1 implements ActionListener{
	
	JFrame frame=new JFrame("Welcome to the Jungle Party!");//Create a frame
	JButton button=new JButton("Check!");//Create a button with test "Check!"
	JTextField field=new JTextField(2);//Create a TextField for the input of the answer
	JPanel panel= new JPanel();//Create a panel to put in the images
	JPanel panel1=new JPanel();//Create a panel to put in panel2 and panel3
	JPanel panel2=new JPanel();//Create a panel to put in the sentence and JTextField
	JPanel panel3=new JPanel();//Create a panel to put in the button
	JLabel label1=new JLabel("How many animals have come to the party?");//Create a label to put in the sentence
	
	public int imageNum=10;//Ensure that the original number of pictures is ten
	
	/** This method is the main method of the class
     *  to set up an object and call the go() function
     *  @param args  The input of the command lines.
     */
	public static void main(String args[]){
		JungleParty1 gui =new JungleParty1();
		gui.go();//Call the go() method
	}
	
	/** This method to create the game interface, with adding the images,button, panels and labels
	 * The method contains the size, color and layout of the frame
     */
	public void go(){			    			
		panel.setLayout(new GridLayout(2,5));//Set layout of panel
		panel.setBackground(Color.WHITE);		
		panel1.setLayout(new GridLayout(2,1));//Set layout of panel1
		panel1.add(panel2);
		panel1.add(panel3);			
		panel2.add(label1);		
		panel3.add(button);
		panel2.add(field);
		
		for(int i=1;i<=imageNum;i++){						
			ImageIcon img = new ImageIcon("jungle/animal" + i + ".png");			
			JLabel imageLabel = new JLabel(img);//Create a label to put in the pictures
			panel.add(imageLabel);			
		}//Put the ten pictures in the panel
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(new BorderLayout());//Set the layout of the frame
		frame.getContentPane().add(BorderLayout.NORTH,panel);
		frame.getContentPane().add(BorderLayout.SOUTH,panel1);
		frame.setSize(800, 440);
		frame.setVisible(true);
		
		button.addActionListener(this);//Add action listener to the button
	}
	
	/** This method checks the answer of the player. The answer should be an integer between 1 and 10
     *  If the answer is correct, the number of the pictures will appear randomly
     *  If the answer is not correct, the number of the picture will not change 
     *  and the player need to answer again
     *  @param event  The action of the button.
     */
	public void actionPerformed(ActionEvent event){
		if(!field.getText().equals(""))//Ensure that empty answer will not lead to an error
		{
		int answer = Integer.parseInt(field.getText());
		if(answer==imageNum ){
			panel.removeAll();
			panel.repaint();
			panel.setBackground(Color.WHITE);
			panel2.removeAll();
			field=new JTextField(2);//Create a new text field
			label1=new JLabel("Correct! How many animals are in the party now?");
			//Create a label to put in the new question 	
			imageNum = (int)(Math.random()*10+1);//Generate a random number 
			for(int i=1;i<=imageNum;i++){						
				ImageIcon img = new ImageIcon("jungle/animal" + i + ".png");			
				JLabel imageLabel = new JLabel(img);//Create a label to put in the pictures
				panel.add(imageLabel);			
			}
			frame.getContentPane().add(panel);
			panel.setLayout(new GridLayout(0,5));//Set layout of panel
				
			panel1.setLayout(new GridLayout(2,1));//Set layout of panel1
			panel1.add(panel2);
			panel1.add(panel3);			
			panel2.add(label1);					
			panel2.add(field);
			frame.getContentPane().setLayout(new BorderLayout());//Set the layout of the frame
			frame.getContentPane().add(BorderLayout.NORTH,panel);
			frame.getContentPane().add(BorderLayout.SOUTH,panel1);
			frame.setVisible(true);
				
		}
		    
		else if (answer!=imageNum){
			panel2.removeAll();panel2.repaint();
			label1=new JLabel("Wrong! Try again!");//Create a label to put in the new sentence
			field = new JTextField(2);	//Create a new text field		
			panel1.setLayout(new GridLayout(2,1));//Set layout of panel1 
			panel2.add(label1);		
			panel2.add(field);
			panel1.add(panel2);
			panel3.add(button);
			panel1.add(panel3);
			frame.getContentPane().add(BorderLayout.SOUTH,panel1);
			frame.setVisible(true);
		
		}	
		}
	}
}