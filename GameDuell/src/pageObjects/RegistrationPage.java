package pageObjects;

	import org.openqa.selenium.By;
	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.WebElement;

public class RegistrationPage {
	
	private static WebElement userTextBox;
	private static WebElement passwordTextBox;
	private static WebElement emailTextBox;   
	private static WebElement registrationButton;
	private static WebElement faileduserTextBox;
	private static WebElement faileduserPassBox;
	private static WebElement failedLoginButton;
	
	public static WebElement userTextBox(WebDriver driver){
		
		userTextBox = driver.findElement(By.xpath(".//*[@id='tf1']"));
		return userTextBox;
	}
	
	public static WebElement passwordTextBox(WebDriver driver){
		
		passwordTextBox = driver.findElement(By.xpath(".//*[@id='tf2']"));
		return passwordTextBox;
	}
	
	public static WebElement emailTextBox(WebDriver driver){
		
		emailTextBox = driver.findElement(By.xpath(".//*[@id='tf3']"));
		return emailTextBox;
	}
	
	public static WebElement registrationButton(WebDriver driver){
		
		registrationButton = driver.findElement(By.xpath(".//*[@id='registrationButton']"));
		return registrationButton;
	}
	
	public static WebElement faileduserTextBox(WebDriver driver){
		
		faileduserTextBox = driver.findElement(By.xpath("j_username"));
		return faileduserTextBox;
	}
	
	public static WebElement faileduserPassBox(WebDriver driver){
		
		faileduserPassBox = driver.findElement(By.xpath("j_password"));
		return faileduserPassBox;
	}	
	
	public static WebElement failedLoginButton (WebDriver driver){
		
		failedLoginButton = driver.findElement(By.id("loginLink"));
		return failedLoginButton;
	}
	
	
}
