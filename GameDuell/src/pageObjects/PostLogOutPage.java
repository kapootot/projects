package pageObjects;

	import org.openqa.selenium.By;
	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.WebElement;

public class PostLogOutPage {

	private static WebElement userTextBox;	
	private static WebElement passwordTextBox;	
	private static WebElement logInButton;	
			
	public static WebElement userTextBox(WebDriver driver){
		
		userTextBox = driver.findElement(By.xpath(".//*[@id='loggedOutAccountbox']/form/input[2]"));
		return userTextBox;
	}
	
	public static WebElement passwordTextBox(WebDriver driver){
		
		passwordTextBox = driver.findElement(By.xpath(".//*[@id='loggedOutAccountbox']/form/input[3]"));
		return passwordTextBox;
	}
	
	public static WebElement logInButton(WebDriver driver){
		
		logInButton = driver.findElement(By.xpath(".//*[@id='loginLink']"));
		return logInButton;
	}
}
	
	
