package testPlan;

	import java.io.FileNotFoundException;
	import java.io.UnsupportedEncodingException;
	import java.util.ArrayList;
	import java.util.List;
	import org.apache.log4j.Logger;
	import org.apache.log4j.xml.DOMConfigurator;
	import com.beust.testng.TestNG;
	import functions.CreateXmls;

@SuppressWarnings("deprecation")

public class Main {
	
	public static Logger Log = Logger.getLogger(TestPlan.class.getName());

	//Main method to run the test plan according to 'accept_test.xml'
	
	public static void main(String[] args) throws InterruptedException, FileNotFoundException, UnsupportedEncodingException {
		
		CreateXmls.createTestXml();
		CreateXmls.createLogXml();
		
		DOMConfigurator.configure("log4j.xml");
		TestNG testng = new TestNG();
		List <String> testNgXmls = new ArrayList<String>();
		testNgXmls.add("accept_test.xml");
		testng.setTestSuites(testNgXmls); 
		testng.run();
				
	}

}
