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
        protected Actions actions = new Actions();
        protected Config config = new Config();
        protected Guid apiToken = Guid.Empty;
        protected Guid secureKey = Guid.Empty;

        [TestInitialize]
        public virtual void InitializeActions()
        {
            this.actions.ServerUrl = this.config.serverUrl;
            if (this.apiToken.Equals(Guid.Empty))
            {
                this.apiToken = this.actions.Login(this.config.username, this.config.password, true);
            }
            if (this.secureKey.Equals(Guid.Empty))
            {
                this.secureKey = this.actions.GenerateAPIKey(this.apiToken, this.config.username, true);
            }
        }
    }
}