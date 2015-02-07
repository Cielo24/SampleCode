using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Cielo24;
using Cielo24.JSON;
using System.Collections.Generic;
using System.IO;

namespace UnitTest
{
    [TestClass]
    public class ActionsTest
    {
        protected Actions actions = new Actions("http://sandbox-dev.cielo24.com");
        protected String username = "api_test";
        protected String password = "api_test";
        protected String newPassword = "api_test_new";
        protected Guid apiToken = Guid.Empty;
        protected Guid secureKey = Guid.Empty;

        [TestInitialize]
        public void Initialize()
        {
            if (this.apiToken.Equals(Guid.Empty))
            {
                this.apiToken = this.actions.Login(username, password, true);
            }
            if (this.secureKey.Equals(Guid.Empty))
            {
                this.secureKey = this.actions.GenerateAPIKey(this.apiToken, this.username, true);
            }
        }
    }
}