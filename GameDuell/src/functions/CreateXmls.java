package functions;

	import java.io.FileNotFoundException;
	import java.io.PrintWriter;
	import java.io.UnsupportedEncodingException;

public class CreateXmls {

	private static String testXml = "<?xml version='1.0' encoding='UTF-8'?> <!DOCTYPE suite SYSTEM 'http://testng.org/testng-1.0.dtd' > <suite name='GameDuell Acceptance Test'> <listeners> <listener class-name='org.uncommons.reportng.HTMLReporter'/> <listener class-name='org.uncommons.reportng.JUnitXMLReporter'/> </listeners> <test name='Acceptance Test Cases'> <classes> <class name='testPlan.TestPlan'/> </classes> </test></suite>";
	private static String logXml = "<?xml version='1.0' encoding='UTF-8'?> <!DOCTYPE log4j:configuration SYSTEM 'log4j.dtd'> <log4j:configuration xmlns:log4j='http://jakarta.apache.org/log4j/' debug='false'> <appender name='fileAppender' class='org.apache.log4j.FileAppender'> <param name='Threshold' value='INFO' /> <param name='File' value='Acceptance_Test_Report.log'/> <layout class='org.apache.log4j.PatternLayout'> <param name='ConversionPattern' value='%d %-5p [%c{1}] %m %n' /> </layout> </appender> <root> <level value='INFO'/> <appender-ref ref='fileAppender'/> </root> </log4j:configuration>";
	
	public static void createTestXml() throws FileNotFoundException, UnsupportedEncodingException{
		
		PrintWriter writer = new PrintWriter("accept_test.xml", "UTF-8");
		writer.print(testXml);
		writer.close();
		
	}
	
	public static void createLogXml() throws FileNotFoundException, UnsupportedEncodingException{
		
		PrintWriter writer = new PrintWriter("log4j.xml", "UTF-8");
		writer.print(logXml);
		writer.close();
		
		
	}
			
}
