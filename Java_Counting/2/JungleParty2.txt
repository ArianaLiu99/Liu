import java.awt.*;
import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
/**
 * Title      : JungleParty2.java
 * Description: This class contains the code of the game JungleParty.
 * Copyright  : 
 * date 2017-5-26
 * @author  Liu Bingqing  Student Number:151011070(QM) 2015213107(BUPT) class:2015215109
 * @version 1.0
 */
public class JungleParty2 implements ListSelectionListener{
	
	JFrame frame=new JFrame("Welcome to the Jungle Party!");//Create a frame
	String[] s = {"1","2","3","4","5","6","7","8","9","10"};//Create the numbers in the JList
	JList<String> list = new JList<String>(s);//Create a JList and add the numbers in it
	
	JPanel panel= new JPanel();//Create a panel to put in the images
	JPanel panel1=new JPanel();//Create a panel to put in panel2
	JPanel panel2=new JPanel();//Create a panel to put in the sentence and JScrollerPane
	JLabel label1=new JLabel("How many animals have come to the party?");//Create a label to put in the sentence
	public int imageNum=10;//Ensure that the original number of pictures is ten
	
	/** This method is the main method of the class
     *  to set up an object and call the go() function
     *  @param args  The input of the command lines.
     */	
	public static void main(String args[]){
		JungleParty2 gui =new JungleParty2();
		gui.go();//Call the go() method
	}
	
	/** This method to create the game interface, with adding the images,button, panels and labels
	 * The method contains the size, color and layout of the frame
     */
	public void go(){		
		JScrollPane scroller = new JScrollPane(list);//Create a scroller and add the JList into it
	    scroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
		scroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
	    list.setVisibleRowCount(2);
	    list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
				
		panel.setLayout(new GridLayout(2,5));//Set layout of panel
		panel.setBackground(Color.WHITE);		
		panel1.add(panel2);
		panel2.add(label1);		
		panel2.add(scroller);
		
		for(int i=1;i<=imageNum;i++){						
			ImageIcon img = new ImageIcon("jungle/animal" + i + ".png");			
			JLabel imageLabel = new JLabel(img);//Create a label to put in the pictures
			panel.add(imageLabel);			
		}
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(new BorderLayout());//Set layout of the frame
		frame.getContentPane().add(BorderLayout.NORTH,panel);
		frame.getContentPane().add(BorderLayout.SOUTH,panel1);
		frame.setSize(800, 440);
		frame.setVisible(true);
				
		list.addListSelectionListener(this);//Add selection listener to the scroller
	}
	
	/** This method checks the answer of the player. The answer should be chosen from the roller
     *  If the answer is correct, the number of the picture will appear randomly
     *  If the answer is not correct, the number of the picture will not change 
     *  and the player need to answer again
     *  @param lse  The selection from the roller.
     */
	public void valueChanged(ListSelectionEvent lse){
		String answer = list.getSelectedValue().toString();//Get the selected answer from the JList
		int ans = Integer.parseInt(answer);
		if(ans==0);
		else{
			if(ans==imageNum){
			panel.removeAll();
			panel.repaint();
			panel.setBackground(Color.WHITE);
			panel2.removeAll();
			list=new JList<String>(s);//Create a JList and add the numbers in it
			label1=new JLabel("Correct! How many animals are in the party now?");//Create a label to put in the new question	
			imageNum = (int)(Math.random()*10+1);//Generate a random number
			for(int i=1;i<=imageNum;i++){						
				ImageIcon img = new ImageIcon("jungle/animal" + i + ".png");			
				JLabel imageLabel = new JLabel(img);//Create a label to put in the pictures
				panel.add(imageLabel);			
			}
			frame.getContentPane().add(panel);
			panel.setLayout(new GridLayout(0,5));//Set layout of panel				
			panel1.add(panel2);
			panel2.add(label1);
			JScrollPane scroller = new JScrollPane(list);//Create a scroller and add the JList into it
		    scroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
			scroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
		    list.setVisibleRowCount(2);
		    list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
			panel2.add(scroller);
			frame.getContentPane().setLayout(new BorderLayout());//Set layout of the frame
			frame.getContentPane().add(BorderLayout.NORTH,panel);
			frame.getContentPane().add(BorderLayout.SOUTH,panel1);
			frame.setVisible(true);
			list.addListSelectionListener(this);//Add selection listener to the scroller
		}
		    
		else if ((ans!=imageNum)){
			panel2.removeAll();panel2.repaint();
			label1=new JLabel("Wrong! Try again!");	//Create a label to put in the new sentence								
			panel2.add(label1);		
			JScrollPane scroller = new JScrollPane(list);//Create a scroller and add the JList into it
		    scroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
			scroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
		    list.setVisibleRowCount(2);
		    list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
			panel2.add(scroller);
			panel1.add(panel2);
			frame.getContentPane().add(BorderLayout.SOUTH,panel1);
			frame.setVisible(true);
		
		}	
		}	
	}
}