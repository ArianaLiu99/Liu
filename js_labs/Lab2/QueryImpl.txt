
import java.rmi.RemoteException;
import java.util.*;
import java.rmi.server.UnicastRemoteObject;

public class QueryImpl extends UnicastRemoteObject implements QueryInterface{
	protected QueryImpl() throws RemoteException {
		super();
	}
    ArrayList<Patient> patientlist=new ArrayList<Patient>();
    public void addPatient(Patient p){
	patientlist.add(p);
    }
	 public Patient getPatient(String ID) throws RemoteException{		
		Patient patient=null;
		for(int i=0;i<patientlist.size();i++){
			if (patientlist.get(i).getID().equals(ID))
		 patient=patientlist.get(i);
		}
		
		return patient;		
			
	}
	
		
}
