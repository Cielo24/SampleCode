package test;

import org.junit.Before;

import cielo24.Actions;
import cielo24.utils.Guid;

public class ActionsTest {

	Actions actions = new Actions("http://sandbox-dev.cielo24.com");
	String username = "api_test";
	String password = "api_test";
	String newPassword = "api_test_new";
	Guid apiToken = null;
	Guid secureKey = null;

	@Before
	public void setUp() throws Exception {
		if (this.apiToken == null){
			this.apiToken = actions.login(username, password, true);
		}
		if (this.secureKey == null){
		    this.secureKey = actions.generateAPIKey(this.apiToken, this.username, true);
		}
	}
}