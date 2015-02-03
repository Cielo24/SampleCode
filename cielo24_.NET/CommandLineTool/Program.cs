using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Cielo24;
using CommandLine;
using CommandLine.Text;
using Cielo24.JSON;
using System.Net;
using System.Diagnostics;
using Cielo24.Options;

namespace CommandLineTool
{
    class Program
    {
        static Options options = new Options();
        static Parser optionParser = new Parser();
        static Actions actions = new Actions();
        static string invokedVerb = null;

        static void Main(string[] args)
        {
            //string[] argss = { "./prog.exe", "-a", "create", "-u", "testscript", "-p", "testscript2", "-m", "https://www.youtube.com/watch?v=n1JGzxvsRPg" };
            if (args.Length == 1 && Options.Verbs.Contains(args[0]))
            {
                options.PrintActionHelp(args[0]);
            }
            else if (args.Length != 0 && Options.Verbs.Contains(args[0])) // If verb is valid
            {
                invokedVerb = args[0];
                if (optionParser.ParseArguments(args, options)) // If parsing successful
                {
                    if (options.VerboseMode) // Enable verbose mode
                    {
                        Debug.Listeners.Add(new TextWriterTraceListener(System.Console.Out));
                    }

                    if (invokedVerb.Equals("login") || invokedVerb.Equals("logout")) // Login and logout are special cases
                    {
                        CallAction(invokedVerb);
                    }
                    else if (TryLogin())                                             // All other actions
                    {
                        CallAction(invokedVerb);
                    }
                }
                else // Parsing failed: show usage for verb
                {
                    options.PrintActionHelp(invokedVerb);
                }
            }
            else
            {
                options.PrintDefaultUsage();
            }

            return;
        }

        public static void CallAction(string actionName)
        {
            actions.ServerUrl = options.ServerUrl;

            switch (actionName)
            {
                // ACCESS CONTROL //
                case "login":
                    Console.WriteLine("Logging in...");
                    if (options.ApiSecureKey.Equals(Guid.Empty))
                    { // Use password and username
                        TryAction(delegate() { return actions.Login(options.Username, options.Password, options.HeaderLogin); });
                    }
                    else
                    { // Use secure key
                        TryAction(delegate() { return actions.Login(options.Username, options.ApiSecureKey, options.HeaderLogin); });
                    }
                    break;
                case "logout":
                    Console.WriteLine("Logging out...");
                    TryAction(delegate() { actions.Logout(options.ApiToken); return "Logged out successfully"; });
                    break;
                case "generate_api_key":
                    Console.WriteLine("Generating API key...");
                    TryAction(delegate() { return actions.GenerateAPIKey(options.ApiToken, options.Username, options.ForceNew); });
                    break;
                case "remove_api_key":
                    Console.WriteLine("Removing API key...");
                    TryAction(delegate() { actions.RemoveAPIKey(options.ApiToken, options.ApiSecureKey); return "API Key removed successfully"; });
                    break;
                case "update_password":
                    Console.WriteLine("Updating password...");
                    TryAction(delegate() { actions.UpdatePassword(options.ApiToken, options.NewPassword); return "Password updated successfully"; });
                    break;
                // JOB CONTROL //
                case "create":
                    TryAction(delegate()
                    {
                        Console.WriteLine("Creating job...");
                        Guid jobId = actions.CreateJob(options.ApiToken, options.JobName, options.SourceLanguage).JobId;
                        Console.WriteLine("JobId: " + jobId.ToString());
                        Console.WriteLine("Adding media...");
                        if (options.MediaFile == null)
                        {
                            Console.WriteLine("TaskId: " + actions.AddMediaToJob(options.ApiToken, jobId, options.MediaUrl).ToString("N"));
                        }
                        else
                        {
                            Console.WriteLine("TaskId: " + actions.AddMediaToJob(options.ApiToken, jobId, options.MediaFile).ToString("N"));
                        }
                        Console.WriteLine("Performing transcrition...");
                        PerformTranscriptionOptions pto = new PerformTranscriptionOptions();
                        pto.PopulateFromArray(options.JobConfig);
                        return actions.PerformTranscription(options.ApiToken, jobId, options.Fidelity, options.Priority, options.CallbackUrl, options.TurnaroundHours, options.TargetLanguage, pto);
                    });
                    break;
                case "authorize":
                    Console.WriteLine("Authorizing job...");
                    TryAction(delegate() { actions.AuthorizeJob(options.ApiToken, options.JobId); return "Job Authorized Succesfully"; });
                    break;
                case "delete":
                    Console.WriteLine("Deleting job...");
                    TryAction(delegate() { return actions.DeleteJob(options.ApiToken, options.JobId); });
                    break;
                case "job_info":
                    Console.WriteLine("Getting job info...");
                    TryAction(delegate() { return actions.GetJobInfo(options.ApiToken, options.JobId); });
                    break;
                case "list":
                    Console.WriteLine("Listing jobs...");
                    TryAction(delegate() { return actions.GetJobList(options.ApiToken); });
                    break;
                case "add_media_to_job":
                    Console.WriteLine("Ading media to job...");
                    if (options.MediaUrl != null)
                    { // Media Url
                        TryAction(delegate() { return actions.AddMediaToJob(options.ApiToken, options.JobId, options.MediaUrl); });
                    }
                    else
                    { // Media File
                        TryAction(delegate() { return actions.AddMediaToJob(options.ApiToken, options.JobId, options.MediaFile); });
                    }
                    break;
                case "add_embedded_media_to_job":
                    Console.WriteLine("Adding embedded media to job...");
                    TryAction(delegate() { return actions.AddEmbeddedMediaToJob(options.ApiToken, options.JobId, options.MediaUrl); });
                    break;
                case "get_media":
                    Console.WriteLine("Getting media...");
                    TryAction(delegate() { return actions.GetMedia(options.ApiToken, options.JobId); });
                    break;
                case "get_transcript":
                    Console.WriteLine("Getting transcript...");
                    TranscriptOptions to = new TranscriptOptions();
                    to.PopulateFromArray(options.CaptionOptions);
                    TryAction(delegate() { return actions.GetTranscript(options.ApiToken, options.JobId, to); });
                    break;
                case "get_caption":
                    Console.WriteLine("Getting caption...");
                    CaptionOptions co = new CaptionOptions();
                    co.PopulateFromArray(options.CaptionOptions);
                    TryAction(delegate() { return actions.GetCaption(options.ApiToken, options.JobId, options.CaptionFormat, co); });
                    break;
                case "get_elementlist":
                    Console.WriteLine("Getting element list...");
                    TryAction(delegate() { return actions.GetElementList(options.ApiToken, options.JobId, options.ElementlistVersion); });
                    break;
                case "list_elementlists":
                    Console.WriteLine("Listing element lists...");
                    TryAction(delegate() {
                        return string.Join("\n", actions.GetListOfElementLists(options.ApiToken, options.JobId));
                    });
                    break;
                default:
                    options.PrintDefaultUsage();
                    break;
            }
        }

        private static void TryAction(Func<object> action)
        {
            try
            {
                string output = action.Invoke().ToString();
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("\n" + output);
                Console.ResetColor();
            }
            catch (Exception e)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("\n" + e.Message);
                Console.ResetColor();

                options.PrintActionHelp(invokedVerb);
            }
        }

        private static bool TryLogin()
        {
            actions.ServerUrl = options.ServerUrl;
            if (options.ApiToken.Equals(Guid.Empty)) // Need to obtain api token
            {
                try
                {
                    if (options.Password != null)
                    {
                        options.ApiToken = actions.Login(options.Username, options.Password, true);
                    }
                    else
                    {
                        options.ApiToken = actions.Login(options.Username, options.ApiSecureKey, true);
                    }
                }
                catch (Exception e)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("\n" + e.Message);
                    Console.ResetColor();
                    options.PrintActionHelp(invokedVerb);
                    return false;
                }
            }
            return true;
        }
    }
}