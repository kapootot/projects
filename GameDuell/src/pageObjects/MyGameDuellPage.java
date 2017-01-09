package pageObjects;

	import org.openqa.selenium.By;
	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.WebElement;


public class MyGameDuellPage {   

	private static WebElement balanceInOverview;
	private static WebElement balanceInAccountBox;
	private static WebElement logOutButton;
	private static WebElement myGameDuell;
	

	public static WebElement balanceInOverview(WebDriver driver){
		
		balanceInOverview = driver.findElement(By.xpath("html/body/div[2]/div/div[3]/div/div[2]/div[2]/p[1]/span"));
		return balanceInOverview;
	}
	
	public static WebElement balanceInAccountBox(WebDriver driver){
		
		balanceInAccountBox = driver.findElement(By.xpath(".//*[@id='accountBoxContainerPractice:accountBoxAmount']/a"));
		return balanceInAccountBox;
	}

	public static WebElement logOutButton(WebDriver driver){
	
		logOutButton = driver.findElement(By.xpath(".//*[@id='logoutLink']"));
		return logOutButton;
	}
	
	public static WebElement myGameDuell(WebDriver driver){
		
		myGameDuell = driver.findElement(By.xpath(".//*[@id='topNaviMygdLink']"));
		return myGameDuell;
	}
	
}
