using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UnitTest
{
    [TestClass]
    public class AccessTest : ActionsTest
    {
        [TestInitialize]
        public override void Initialize()
        {
            base.Initialize();
        }

        [TestMethod]
        public void testLoginPasswordNoHeaders()
        {
            // Username, password, no headers
            this.apiToken = this.actions.Login(this.config.username, this.config.password, false);
            Assert.AreEqual(32, this.apiToken.ToString("N").Length);
        }

        [TestMethod]
        public void testLoginPasswordHeaders()
        {
            // Username, password, headers
            this.apiToken = this.actions.Login(this.config.username, this.config.password, true);
            Assert.AreEqual(32, apiToken.ToString("N").Length);
        }

        [TestMethod]
        public void testLoginSecureKeyNoHeaders()
        {
            // Username, secure key, no headers
            this.apiToken = this.actions.Login(this.config.username, this.secureKey, false);
            Assert.AreEqual(32, this.apiToken.ToString("N").Length);
        }

        [TestMethod]
        public void testLoginSecureKeyHeaders()
        {
            // Username, secure key, headers
            this.apiToken = this.actions.Login(this.config.username, this.secureKey, true);
            Assert.AreEqual(32, apiToken.ToString("N").Length);
        }

        [TestMethod]
        public void testLogout()
        {
            // Logout
            this.actions.Logout(this.apiToken);
            this.apiToken = Guid.Empty;
        }

        [TestMethod]
        public void testGenerateApiKey()
        {
            this.secureKey = this.actions.GenerateAPIKey(this.apiToken, this.config.username, false);
            Assert.AreEqual(32, secureKey.ToString("N").Length);
        }

        [TestMethod]
        public void testGenerateApiKeyForceNew()
        {
            this.secureKey = this.actions.GenerateAPIKey(this.apiToken, this.config.username, true);
            Assert.AreEqual(32, this.secureKey.ToString("N").Length);
            this.actions.RemoveAPIKey(this.apiToken, this.secureKey);
        }

        [TestMethod]
        public void testRemoveApiKey()
        {
            this.actions.RemoveAPIKey(this.apiToken, this.secureKey);
            this.secureKey = Guid.Empty;
        }

        [TestMethod]
        public void testUpdatePassword()
        {
            this.actions.UpdatePassword(this.apiToken, this.config.newPassword);
            this.actions.UpdatePassword(this.apiToken, this.config.password);
        }
    }
}
