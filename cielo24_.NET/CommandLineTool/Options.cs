using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using CommandLine;
using CommandLine.Text;
using System.ComponentModel;
using System.IO;
using Cielo24.JSON;
using Cielo24;

namespace CommandLineTool
{
    public class Options
    {
        protected string indent = "   ";
        protected string gap = "     ";
        public static readonly string[] Verbs = { "login", "logout", "create", "delete", "authorize", "add_media_to_job", "add_embedded_media_to_job", "list", "list_elementlists", "get_caption", "get_transcript", "get_elementlist", "get_media", "generate_api_key", "remove_api_key", "update_password", "job_info" };

        [Option('h', "help", HelpText = "cielo24 username", Required = false, DefaultValue = null)]
        public string Help { get; set; }

        [Option('u', "username", HelpText = "cielo24 username", Required = false, DefaultValue = null)]
        public string Username { get; set; }

        [Option('p', "password", HelpText = "cielo24 password", Required = false, DefaultValue = null)]
        public string Password { get; set; }

        [Option('s', "server", HelpText = "cielo24 server URL [https://api.cielo24.com]", Required = false, DefaultValue = "https://api.cielo24.com")]
        public string ServerUrl { get; set; }

        [Option('k', "key", HelpText = "API Secure Key", Required = false, DefaultValue = null)]
        public string _ApiSecureKey { get { return this.ApiSecureKey.ToString("N"); } set { this.ApiSecureKey = Converters.StringToGuid(value, "API Secure Key"); } }
        public Guid ApiSecureKey { get; set; }

        [Option('N', "token", HelpText = "The API token of the current session", Required = false, DefaultValue = null)]
        public string _ApiToken { get { return this.ApiToken.ToString("N"); } set { this.ApiToken = Converters.StringToGuid(value, "Api Token"); } }
        public Guid ApiToken { get; set; }

        [Option('f', "fidelity", HelpText = "Fidelity [MECHANICAL, PREMIUM, PROFESSIONAL] (PREMIUM by default)", Required = false, DefaultValue = Fidelity.PREMIUM)]
        public Fidelity Fidelity { get; set; }

        [Option('P', "priority", HelpText = "Priority [ECONOMY, STANDARD, HIGH] (STANDARD by default)", Required = false, DefaultValue = Priority.STANDARD)]
        public Priority Priority { get; set; }

        [Option('m', "url", HelpText = "Media URL", Required = false, DefaultValue = null)]
        public string _MediaUrl { get { return this.MediaUrl.ToString(); } set { this.MediaUrl = Converters.StringToUri(value, "Media URL"); } }
        public Uri MediaUrl { get; set; }

        [Option('M', "file", HelpText = "Local media file", Required = false, DefaultValue = null)]
        public string _MediaFile { get { return this.MediaFile.ToString(); } set { this.MediaFile = Converters.StringToFileStream(value, "Media File"); } }
        public FileStream MediaFile { get; set; }

        [Option('l', "source", HelpText = "The source language [en, es, de, fr] (en by default)", Required = false, DefaultValue = "en")]
        public Language SourceLanguage { get; set; }

        [Option('t', "target", HelpText = "The target language [en, es, de, fr] (en by default)", Required = false, DefaultValue = "en")]
        public Language TargetLanguage { get; set; }

        [Option('j', "id", HelpText = "Job Id", Required = false, DefaultValue = null)]
        public string _JobId { get { return this.JobId.ToString("N"); } set { this.JobId = Converters.StringToGuid(value, "Job Id"); } }
        public Guid JobId { get; set; }

        [Option('T', "hours", HelpText = "Turnaround hours", Required = false, DefaultValue = null)]
        public int? TurnaroundHours { get; set; }

        [Option('n', "name", HelpText = "Job Name", Required = false, DefaultValue = null)]
        public string JobName { get; set; }

        [Option('c', "format", HelpText = "The caption format [SRT, DFXP, QT] (SRT by default)", Required = false, DefaultValue = CaptionFormat.SRT)]
        public CaptionFormat CaptionFormat { get; set; }

        [Option('e', "el", HelpText = "The element list version [ISO Date format: 2014-05-06T10:49:38.341715]", Required = false, DefaultValue = null)]
        public string _ElementListVersion { get { return this.ElementlistVersion.ToString(); } set { this.ElementlistVersion = Converters.StringToDateTime(value, "Elementlist Version"); } }
        public DateTime? ElementlistVersion { get; set; }

        [Option('C', "callback", HelpText = "Callback URL for the job", Required = false, DefaultValue = null)]
        public string _CallbackUrl { get { return this.CallbackUrl.ToString(); } set { this.CallbackUrl = Converters.StringToUri(value, "Callback URL"); } }
        public Uri CallbackUrl { get; set; }

        [Option('S', "silent", HelpText = "Silent mode", Required = false, DefaultValue = false)]
        public bool Silent { get; set; }

        [OptionArray('J', "jobconfig", HelpText = "Job options dictionary. Usage: -O key1=value1 -O key2=value2. See API documentation for details", Required = false, DefaultValue = null)]
        public string[] JobConfig { get; set; }

        [OptionArray('O', "options", HelpText = "Caption/transcript options query string arguments. Usage: -O key1=value1 -O key2=value2. See API documentation for details", Required = false, DefaultValue = null)]
        public string[] CaptionOptions { get; set; }

        [Option('v', "verbose", HelpText = "Verbose Mode", Required = false, DefaultValue = false)]
        public bool VerboseMode { get; set; }

        [Option('d', "newpassword", HelpText = "New password", Required = false, DefaultValue = null)]
        public string NewPassword { get; set; }

        [Option('F', "forcenew", HelpText = "Always force new API key (disabled by default)", Required = false, DefaultValue = false)]
        public bool ForceNew { get; set; }

        [Option('H', "headers", HelpText = "Login using headers (disabled by default)", Required = false, DefaultValue = false)]
        public bool HeaderLogin { get; set; }

        [HelpVerbOption]
        public void PrintActionHelp(string action)
        {
            PrintDefaultUsage();
            if (!Verbs.Contains(action)) { return; }

            Console.WriteLine("\nREQUIRED FOR \"" + action + "\" ACTION:");
            string[] job_id_param = { "delete", "authorize", "list_elementlists", "get_elementlist", "get_media", "job_info", "add_media_to_job", "add_embedded_media_to_job", "get_transcript", "get_caption" };
            if (job_id_param.Contains(action))
            {
                Console.WriteLine(indent + "-j" + gap + "Job Id");
            }
            switch (action)
            {
                case "add_media_to_job":
                    //"$job_id_param" "$media_url_param" "or" "$media_file_param"
                    Console.WriteLine(indent + "-m" + gap + "Media URL");
                    Console.WriteLine("or");
                    Console.WriteLine(indent + "-M" + gap + "Local Media File");
                    break;
                case "add_embedded_media_to_job":
                    Console.WriteLine(indent + "-m" + gap + "Media URL");
                    break;
                case "list":
                    Console.WriteLine(indent + "none");
                    break;
                case "get_caption":
                case "get_transcript":
                    Console.WriteLine(indent + "-c" + gap + "The caption format [SRT, DFXP, QT] (SRT by default)");
                    Console.WriteLine("\nOPTIONAL:");
                    Console.WriteLine(indent + "-e" + gap + "The element list version [ISO Date format: 2014-05-06T10:49:38.341715]");
                    Console.WriteLine(indent + "-O" + gap + "Caption/transcript options query string arguments. Usage: -O key1=value1 -O key2=value2. See API documentation for details");
                    break;
                case "get_elementlist":
                    Console.WriteLine(indent + "-e" + gap + "ElementList Version");
                    break;
                case "generate_api_key":
                    Console.WriteLine("\nOPTIONAL:");
                    Console.WriteLine(indent + "-F" + gap + "Always force new API key (disabled by default)");
                    break;
                case "remove_api_key":
                    Console.WriteLine(indent + "-k" + gap + "API Secure Key");
                    break;
                case "update_password":
                    Console.WriteLine(indent + "-d" + gap + "New password");
                    break;
                case "logout":
                    Console.WriteLine(indent + "-N" + gap + "API token for the current session");
                    break;
                case "login":
                    Console.WriteLine(indent + "-u" + gap + "cielo24 username");
                    Console.WriteLine(indent + "-p" + gap + "cielo24 password");
                    Console.WriteLine("or");
                    Console.WriteLine(indent + "-k" + gap + "API secure key");
                    Console.WriteLine("or");
                    Console.WriteLine(indent + "-N" + gap + "API token of the current session");
                    Console.WriteLine("\nOPTIONAL:");
                    Console.WriteLine(indent + "-H" + gap + "Use headers");
                    break;
                case "create":
                    Console.WriteLine(indent + "-f" + gap + "Fidelity [MECHANICAL, PREMIUM, PROFESSIONAL]");
                    Console.WriteLine(indent + "-P" + gap + "Priority [ECONOMY, STANDARD, HIGH]");
                    Console.WriteLine(indent + "-M" + gap + "Local Media File");
                    Console.WriteLine("or");
                    Console.WriteLine(indent + "-m" + gap + "Media URL");
                    Console.WriteLine("\nOPTIONAL:");
                    Console.WriteLine(indent + "-n" + gap + "Job Name");
                    Console.WriteLine(indent + "-J" + gap + "Job options dictionary. Usage: -O key1=value1 -O key2=value2. See API documentation for details");
                    Console.WriteLine(indent + "-C" + gap + "Callback URL for the job");
                    Console.WriteLine(indent + "-T" + gap + "Turnaround hours");
                    Console.WriteLine(indent + "-l" + gap + "The source language [en, es, de, fr] (en by default)");
                    Console.WriteLine(indent + "-t" + gap + "The target language [en, es, de, fr] (en by default)");
                    break;
                default:
                    break;
            }
        }

        public void PrintDefaultUsage()
        {
            Console.WriteLine("\nUsage: ./program.exe [action] [options]");
            Console.WriteLine("Available actions: " + String.Join(", ", Verbs));
            Console.WriteLine("\nExecutes a cielo24 API call");
            Console.WriteLine("\nALWAYS REQUIRED:");
            Console.WriteLine("--------------------------");
            Console.WriteLine(indent + "-u" + gap + "cielo24 username");
            Console.WriteLine(indent + "-p" + gap + "cielo24 password");
            Console.WriteLine("or");
            Console.WriteLine(indent + "-k" + gap + "API secure key");
            Console.WriteLine("or");
            Console.WriteLine(indent + "-N" + gap + "API token of the current session");
            Console.WriteLine("--------------------------");
            Console.WriteLine("\nOPTIONAL:");
            Console.WriteLine(indent + "-s" + gap + "cielo24 server URL [https://api.cielo24.com]");
        }
    }

    public class Converters
    {
        public static Guid StringToGuid(string s, string propertyName)
        {
            if (s == null) {
                return Guid.Empty;
            }
            try {
                return Guid.Parse(s);
            }
            catch (FormatException e)
            {
                throw new FormatException("Invalid value entered for option \'" + propertyName + "\'.\n" + e.Message, e);
            }
        }

        public static Uri StringToUri(string s, string propertyName)
        {
            if (s == null) {
                return null;
            }
            try {
                return new Uri(s); 
            }
            catch (UriFormatException e)
            {
                throw new UriFormatException("Invalid URL: \'" + propertyName + "\'.\n" + e.Message, e);
            }
        }

        public static FileStream StringToFileStream(string s, string propertyName)
        {
            if (s == null) {
                return null;
            }
            try {
                s = Path.GetFullPath(s); // Handles both absolute and relative paths
                return new FileStream(s, FileMode.Open);
            }
            catch (IOException e)
            {
                throw new IOException("Invalid file path: \'" + propertyName + "\'.\n" + e.Message, e);
            }
        }

        public static DateTime? StringToDateTime(string s, string propertyName)
        {
            if (s == null)
            {
                return null;
            }
            try
            {
                return DateTime.Parse(s);
            }
            catch (IOException e)
            {
                throw new IOException("Invalid format: \'" + propertyName + "\'.\n" + e.Message, e);
            }
        }
    }
}
