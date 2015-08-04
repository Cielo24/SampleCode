using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Cielo24;
using Cielo24.JSON;
using NLog;
using NLog.Config;
using NLog.Targets;
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
        // Storing memoryTarget here, so that unittests can access it
        protected MemoryTarget memoryTarget;

        private void EnableCustomLogger()
        {
            // Make WebUtils log to Console as well as to Memory
            LoggingConfiguration logConf = new LoggingConfiguration();
            this.memoryTarget = new MemoryTarget();
            ConsoleTarget consoleTarget = new ConsoleTarget();

            logConf.AddTarget("MemoryTarget", memoryTarget);
            logConf.AddTarget("ConsoleTarget", consoleTarget);
            logConf.LoggingRules.Add(new LoggingRule("*", LogLevel.Info, memoryTarget));
            logConf.LoggingRules.Add(new LoggingRule("*", LogLevel.Info, consoleTarget));

            LogManager.Configuration = logConf;
            WebUtils.logger = LogManager.GetLogger("TestLogger");
        }

        [TestInitialize]
        public virtual void Initialize()
        {
            this.EnableCustomLogger();
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