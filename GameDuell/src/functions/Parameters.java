package functions;

	import java.text.DateFormat;
	import java.text.SimpleDateFormat;
	import java.util.Date;
	import org.apache.commons.lang3.RandomStringUtils;

public class Parameters {

	public static String homePageUrl = "http://www.gameduell.com";
	public static String email = validEmailGenerator(8);
	public static String userName = validUserGenerator();
	public static String loggedUsername = userName;
	public static String password = "4r5t6Y72";
	public static String loggedPassword = password;
	public static String testedPath = "/gd/emailManagement/emailValidation.xhtml";
	public static String validUser = "kapoo13";
	public static String validPass = "4r5t6Y7U";
	
	public static String validEmailGenerator(int length){
		
		String allowedChars="abcdefghijklmnopqrstuvwxyz" + "1234567890" + "_";
		String email="";
		String temp=RandomStringUtils.random(length,allowedChars);
		email=temp.substring(0,temp.length())+"@gmail.com";
		return email;
	}
	
	public static String validUserGenerator(){
		
		String allowedChars="abcdefghijklmnopqrstuvwxyz" + "1234567890";
		String user="";
		String temp=RandomStringUtils.random(8,allowedChars);
		user=temp.substring(0,temp.length());
		return user;
	}
	
	public static String dateNow(){
		
		DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
		Date date = new Date();
		return dateFormat.format(date);
	}
}
