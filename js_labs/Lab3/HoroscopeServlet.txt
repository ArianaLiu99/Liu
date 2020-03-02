import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.util.ArrayList;

public class HoroscopeServlet extends HttpServlet{
	public void doGet(HttpServletRequest request,HttpServletResponse response)
			throws IOException, ServletException{
		String name=request.getParameter("name");
		String sex=request.getParameter("sex");
		String sign=request.getParameter("sign");
		String horo=horoScope(sign,sex);
	response.setContentType("text/html");
	PrintWriter out = response.getWriter();
	
	if(name==null)
out.println("Please identify yourself (by indicating your name), so that your horoscope can be given!");
	else{
		out.println("<html><body>Hello "+name);
		out.println(horo);
	}	
	out.println("</body></html>");
	out.close();		
	}
	
	public String horoScope(String sign,String sex){
		String horoscope;
		ArrayList<String> list=new ArrayList<String>();
		list.add("Aries");
		list.add("Taurus");
		list.add("Gemini");
		list.add("Cancer");
		list.add("Leo");
		list.add("Virgo");
		if(list.contains(sign)){
			if(sex.equals("male"))
				horoscope="You will have a long life.";
			else
				horoscope="You will find a tall handsome stranger.";
		}
		else{
			if(sex.equals("male"))
				horoscope="You will have a rich life.";
			else
				horoscope="You will have six children.";
		}
		return horoscope;
	}

}
