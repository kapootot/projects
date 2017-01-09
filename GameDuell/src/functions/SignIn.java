package functions;

	import org.openqa.selenium.WebDriver;
	import pageObjects.PostLogOutPage;
	import testPlan.Main;

public class SignIn {
	
	public static void execute(WebDriver driver){
		
		PostLogOutPage.userTextBox(driver).sendKeys(Parameters.loggedUsername);
		Main.Log.info("Logged in after logout with user credentials: " + "User: " + Parameters.loggedUsername + " Password: " + Parameters.loggedPassword);
		PostLogOutPage.passwordTextBox(driver).sendKeys(Parameters.loggedPassword);
		PostLogOutPage.logInButton(driver).click();
	}

}
