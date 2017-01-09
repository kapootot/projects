package functions;

	import java.util.concurrent.TimeUnit;
	import org.openqa.selenium.By;
	import org.openqa.selenium.WebDriver;
	import pageObjects.RegistrationPage;
	import testPlan.Main;

public class RegisterNewUser {
	
	public static void execute(WebDriver driver) throws InterruptedException{
		
		RegistrationPage.userTextBox(driver).sendKeys(Parameters.userName);
		Main.Log.info("Registered with new user credentials: User: " +  Parameters.loggedUsername + " Password: " + Parameters.loggedPassword);
		RegistrationPage.passwordTextBox(driver).sendKeys(Parameters.password);
		RegistrationPage.emailTextBox(driver).sendKeys(Parameters.email);
		RegistrationPage.passwordTextBox(driver).click();
		driver.manage().timeouts().implicitlyWait(6, TimeUnit.SECONDS);
		RegistrationPage.registrationButton(driver).click();
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		
		String currentPageUrl = driver.getCurrentUrl();
		String SignUpUrl = "http://www.gameduell.com/registration.html";
		
		//Checking if registration failed because system flagged the script as a Robot
		boolean isRegistered = driver.findElements(By.xpath(".//*[@id='validateMailForm']/div[2]/h1")).size() > 0;
		
		if (currentPageUrl.equals(SignUpUrl) && (!isRegistered)){
			
			//If blocked, login with my already exist user, to continue the test with existing user
			RegistrationPage.faileduserTextBox(driver).sendKeys(Parameters.validUser);
			RegistrationPage.faileduserPassBox(driver).sendKeys(Parameters.validPass);
			RegistrationPage.failedLoginButton(driver).click();
			
		}

		
	}

}
