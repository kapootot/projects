package pageObjects;

	import org.openqa.selenium.By;
	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.WebElement;

public class HomePage {
	
	private static WebElement newHereTestForfree;
	
	
	public static WebElement newButton(WebDriver driver){
		
		newHereTestForfree = driver.findElement(By.xpath(".//*[@id='newHereLink']"));
		return newHereTestForfree;

	}
			
	
	
}
