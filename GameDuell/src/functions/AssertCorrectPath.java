package functions;

	import testPlan.Main;

public class AssertCorrectPath {
			
	public static boolean compare(String comparedUrl, String expectedPath){
		
		//Splitting the domain from Url using RegEx, In case the domain will change in the future
		
		String [] splitUrl = comparedUrl.split("^(([^:/?#]+):)?(//([^/?#]*))");
		String comparedPath = splitUrl[1];
		
		Main.Log.info("Comparing Paths....Done.");
		Main.Log.info("Compared Path: " + comparedPath);
		Main.Log.info("Expected Path: " + expectedPath);
		
		return (comparedPath.equals(expectedPath));
	}	

}
