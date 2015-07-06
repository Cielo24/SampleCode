using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UnitTest
{
    // Unittest configurations
    public class Config
    {
        public String serverUrl = "http://sandbox.cielo24.com";
        public String username = "api_test";
        public String password = "api_test";
        public String newPassword = "api_test_new";
        public Uri sampleVideoUri = new Uri("http://techslides.com/demos/sample-videos/small.mp4");
        public string sampleVideoFilePath = "..\\..\\..\\..\\testing\\sample_video.mp4";
    }
}
