package functions;

	import org.openqa.selenium.WebDriver;

public class GoToHomePage {
	
	public static void execute(WebDriver driver){
		
		driver.get(Parameters.homePageUrl);
	}

}
