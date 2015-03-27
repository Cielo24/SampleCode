import static org.junit.Assert.*;

import java.io.IOException;

import org.junit.Test;

import cielo24.utils.WebException;

public class AccessTest extends ActionsTest {
    
    @Test
    public void testLoginPasswordNoHeaders() throws IOException, WebException {
        // Username, password, no headers
        this.apiToken = this.actions.login(this.config.username, this.config.password, false);
        assertEquals(32, this.apiToken.toString().length());
    }

    @Test
    public void testLoginPasswordHeaders() throws IOException, WebException {
        // Username, password, headers
        this.apiToken = this.actions.login(this.config.username, this.config.password, true);
        assertEquals(32, apiToken.toString().length());
    }

    @Test
    public void testLoginSecureKeyNoHeaders() throws IOException, WebException {
        // Username, secure key, no headers
        this.apiToken = this.actions.login(this.config.username, this.secureKey, false);
        assertEquals(32, this.apiToken.toString().length());
    }

    @Test
    public void testLoginSecureKeyHeaders() throws IOException, WebException {
        // Username, secure key, headers
        this.apiToken = this.actions.login(this.config.username, this.secureKey, true);
        assertEquals(32, apiToken.toString().length());
    }

    @Test
    public void testLogout() throws IOException, WebException {
        // Logout
        this.actions.logout(this.apiToken);
        this.apiToken = null;
    }

    @Test
    public void testGenerateApiKey() throws IOException, WebException {
        this.secureKey = this.actions.generateAPIKey(this.apiToken, this.config.username, false);
        assertEquals(32, secureKey.toString().length());
    }

    @Test
    public void testGenerateApiKeyForceNew() throws IOException, WebException {
        this.secureKey = this.actions.generateAPIKey(this.apiToken, this.config.username, true);
        assertEquals(32, this.secureKey.toString().length());
        this.actions.removeAPIKey(this.apiToken, this.secureKey);
    }

    @Test
    public void testRemoveApiKey() throws IOException, WebException {
        this.actions.removeAPIKey(this.apiToken, this.secureKey);
        this.secureKey = null;
    }

    @Test
    public void testUpdatePassword() throws IOException, WebException {
        this.actions.updatePassword(this.apiToken, this.config.newPassword);
        this.actions.updatePassword(this.apiToken, this.config.password);
    }
}