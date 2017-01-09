package functions;

	import org.openqa.selenium.WebElement;

public class AsssertPracticeMoney {
	
	public static boolean compare(WebElement overview, WebElement account){
				
		String overviewBalance = overview.getText();
		String accountBalance = account.getText();
		
		return overviewBalance.equals(accountBalance);		
	}
}
