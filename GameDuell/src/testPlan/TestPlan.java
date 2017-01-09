package testPlan;

	import java.util.concurrent.TimeUnit;
	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.WebElement;
	import org.testng.Assert;
	import org.testng.Reporter;
	import org.testng.annotations.AfterClass;
	import org.testng.annotations.BeforeClass;
	import org.testng.annotations.Test;
	import pageObjects.MyGameDuellPage;
	import pageObjects.PostLogInPage;
	import functions.*;

public class TestPlan {
	
	private static WebDriver firefox;
	private static String dateStart = Parameters.dateNow();
	private static String dateEnd;

		
	@BeforeClass
	public void openBrowser(){
		
		firefox = FireFox.open();
		Main.Log.info("***********Starting GameDuell Acceptance Test***********");
		Main.Log.info("***********Started at: " + dateStart + "**************");
		
	}
	
	@AfterClass
	public void closeBrowser(){
		
		dateEnd = Parameters.dateNow();
		Main.Log.info("***********Test completed at: " + dateEnd + "*******");
		
		firefox.quit();
	}
		
	@Test
	public static void Step_1_OpenBrowser(){
		
		Reporter.log("***********Starting GameDuell Acceptance Test***********\n");
		Reporter.log("***********Started at: " + dateStart + "**************\n");
		
		Main.Log.info("[Executing Step 1] - Open Browser");
		Reporter.log("[Executing Step 1] - Open Browser\n");
		
		firefox.manage().window().maximize();
		GoToHomePage.execute(firefox);
		String currentTitle = firefox.getTitle();
		String expectedTitle = "GameDuell: Online Games - Real People, Real Prizes";
		
		Assert.assertEquals(currentTitle, expectedTitle);
		
		Main.Log.info("[Step 1] completed.");
		Reporter.log("[Step 1] completed.\n");
		firefox.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

	}
	
	@Test
	public static void Step_2_ClickOnNewUser(){
		
		Main.Log.info("[Executing Step 2] - Click on 'New here? Test for free!'");
		Reporter.log("[Executing Step 2] - Click on 'New here? Test for free!'\n");
		
		NewUserButton.execute(firefox);
		
		firefox.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
		String currentTitle = firefox.getTitle();
		String expectedTitle = "GameDuell: play games online";
		
		Assert.assertEquals(currentTitle, expectedTitle);
		
		Main.Log.info("[Step 2] completed.");
		Reporter.log("[Step 2] completed.\n");
		firefox.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

	}
	
	@Test
	public static void step_3_RegisterNewRandomUser() throws InterruptedException{
		
		Main.Log.info("[Executing Step 3] - Register a new random user");		
		Reporter.log("[Executing Step 3] - Register a new random user\n");		
				
		RegisterNewUser.execute(firefox);
		firefox.manage().timeouts().implicitlyWait(8, TimeUnit.SECONDS);
		
		String currentUrl = firefox.getCurrentUrl();
		String expectedUrl = "https://my.gameduell.com/gd/emailManagement/emailValidation.xhtml?justRegistered=true";
		
		Assert.assertEquals(currentUrl, expectedUrl);
		
		Main.Log.info("[Step 3] Completed.");
		Reporter.log("[Step 3] Completed.\n");		
		firefox.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);


	}
	
	@Test
	public static void step_4_AssertPracticeMoney(){
		
		Main.Log.info("[Executing Step 4] - Assert correct practice money");		
		Reporter.log("[Executing Step 4] - Assert correct practice money\n");		

		String assertBalanceResult;
		MyGameDuellPage.myGameDuell(firefox).click();
		firefox.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
		
		WebElement overview = MyGameDuellPage.balanceInOverview(firefox);
		WebElement account = MyGameDuellPage.balanceInAccountBox(firefox);
		boolean asssertPracticeMoney = AsssertPracticeMoney.compare(overview, account);
		
		if (asssertPracticeMoney){
			assertBalanceResult = "Practice Balance is correct";
		}
		
		else {
			assertBalanceResult = "Wrong Balance"; 
		}
		
		Main.Log.info("[Balance] - comparison result: " + assertBalanceResult);
		Main.Log.info("New User Balance: " + overview.getText());
		Reporter.log("[Balance] - comparison result: " + assertBalanceResult +"\n");		
		Reporter.log("New User Balance: " + overview.getText()+"\n");		
		
		Assert.assertTrue(asssertPracticeMoney);
		
		Main.Log.info("[Step 4] completed.");
		Reporter.log("[Step 4] completed.\n");		

		firefox.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
	}
		
	
	@Test
	public static void step_5_LogOut(){
		
		Main.Log.info("[Executing Step 5] - Logout");	
		Reporter.log("[Executing Step 5] - Logout\n");
		
		SignOut.execute(firefox);
		firefox.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
		
		String currentTitle = firefox.getTitle();
		String expectedTitle = "GameDuell: Online Games - Real People, Real Prizes";
		
		Assert.assertEquals(currentTitle, expectedTitle);
		
		Main.Log.info("[Step 5] completed.");
		Reporter.log("[Step 5] completed.\n");

		firefox.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
	}
	
	@Test
	public static void step_6_LogIn(){
		
		Main.Log.info("[Executing Step 6] - Login");		
		Reporter.log("[Executing Step 6] - Login\n");

		SignIn.execute(firefox);
		
		//Checks if "Welcome" message is displayed - Means user logged in successfully
			
		Assert.assertTrue(PostLogInPage.welcomeExists(firefox));
		
		Main.Log.info("[Step 6] completed.");
		Reporter.log("[Step 6] completed.\n");

		firefox.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);

	}
	
	@Test
	public static void step_7_AssertCurrentURL(){
		
		Main.Log.info("[Executing Step 7] - Assert correct URL");		
		Reporter.log("[Executing Step 7] - Assert correct URL\n");

		String comparedUrl = firefox.getCurrentUrl();
		String expectedPath = Parameters.testedPath;
		String assertUrlResult; 
		boolean assertCorrectPath = AssertCorrectPath.compare(comparedUrl, expectedPath);
		
		
		if (assertCorrectPath){
			assertUrlResult = "URL is correct";
		}
		
		else {
			assertUrlResult = "Wrong URL";
		}
		
		Main.Log.info("[Path] - comparison result: " + assertUrlResult);
		Reporter.log("[Path] - comparison result: " + assertUrlResult +"\n");

		Main.Log.info("Current URL: " + comparedUrl);
		Reporter.log("Current URL: " + comparedUrl+"\n");
		
		Assert.assertTrue(assertCorrectPath);
		
		Main.Log.info("[Step 7] completed.");
		Reporter.log("[Step 7] completed.\n");

		firefox.manage().timeouts().implicitlyWait(8, TimeUnit.SECONDS);
		
		dateEnd = Parameters.dateNow();
		
		Reporter.log("***********Test completed at: " + dateEnd + "*******\n");
	}
	
}
