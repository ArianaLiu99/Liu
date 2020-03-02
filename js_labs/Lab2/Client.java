
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.Remote;
import java.rmi.RemoteException;
import java.rmi.*;

public class Client {
	public static void main(String[] args){
		
		try
		{
			// Check to see if a registry was specified
			String registration = "rmi://10.128.202.68/Patient";
			QueryInterface q = (QueryInterface) Naming.lookup (registration);
	        Patient patient = q.getPatient(args[0]);
			
			System.out.println (patient);
		}
		catch (NotBoundException nbe)
		{
			System.out.println ("No patient available  in registry!");
		}
		catch (RemoteException re)
		{
			System.out.println ("RMI Error - " + re);
		}
		catch (Exception e)
		{
			System.out.println ("Error - " + e);
}
}
}
