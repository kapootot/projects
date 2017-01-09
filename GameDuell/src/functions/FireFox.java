package functions;

	import java.util.concurrent.TimeUnit;
	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.firefox.FirefoxDriver;

public class FireFox {
	
	public static WebDriver driver;
	
	public static WebDriver open(){
	
		driver = new FirefoxDriver();
	    driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
	    return driver;
	}
	
	public static void close(){
		
		driver.close();
	}
	
	

}
