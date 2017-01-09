package pageObjects;

	import org.openqa.selenium.By;
	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.WebElement;

public class PostLogInPage {
	
	private static WebElement welcome;

	public static WebElement welcome(WebDriver driver){
				
		welcome = driver.findElement(By.xpath(".//*[@id='validateMailForm']/div[2]/h1"));
		return welcome;
	}
	
	public static boolean welcomeExists(WebDriver driver){
		
		return driver.findElements(By.xpath(".//*[@id='validateMailForm']/div[2]/h1")).size() != 0;
	}
}
