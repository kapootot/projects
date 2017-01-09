package functions;

	import org.openqa.selenium.WebDriver;
	import pageObjects.MyGameDuellPage;

public class SignOut {
	
	public static void execute(WebDriver driver){
		
		MyGameDuellPage.logOutButton(driver).click();
	}

}
