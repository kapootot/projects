package functions;

	import org.openqa.selenium.WebDriver;
	import pageObjects.HomePage;

public class NewUserButton {
	
	public static void execute(WebDriver driver){
		
		HomePage.newButton(driver).click();		
	}

}
