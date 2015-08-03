module Cielo24Cli

  require 'thor'
  require 'cielo24'

  class Application < Thor

    include Cielo24

    ENV['THOR_COLUMNS'] = '300' # Increases the maximum allowed length of a console line, otherwise descriptions/help gets truncated (...)

    # ALWAYS REQUIRED:
    username_option = [:u, :required => false, :desc => 'cielo24 username', :type => :string, :banner => 'username', :hide => true]
    password_option = [:p, :required => false, :desc => 'cielo24 password', :banner => 'password', :hide => true]
    securekey_option = [:k, :required => false, :desc => 'The API Secure Key', :banner => 'securekey', :hide => true]
    api_token_option = [:N, :required => false, :desc => 'The API token of the current session', :banner => 'token', :hide => true]
    server_url_option =[:s, :required => false, :desc => 'cielo24 server URL [https://api.cielo24.com]', :banner => 'server_url', :hide => true, :default => 'http://api.cielo24.com']
    # JOB CONTROL:
    job_id_option = [:j, :required => true, :desc => 'Job Id', :banner => 'jobid']
    media_url_option = [:m, :required => false, :desc => 'Media URL', :banner => 'mediaurl']
    media_file_option = [:M, :required => false, :desc => 'Local media file', :banner => 'filepath']
    # OTHER OPTIONS:
    header_option = [:H, :required => false, :desc => 'Use headers', :default => false, :type => :boolean]
    fidelity_option = [:f, :required => false, :desc => 'Fidelity ' + Fidelity.all.join(', '), :banner => 'fidelity', :default => Fidelity::PREMIUM]
    priority_option = [:P, :required => false, :desc => 'Priority ' + Priority.all.join(', '), :banner => 'priority', :default => Priority::STANDARD]
    source_language_option = [:l, :required => false, :desc => 'Source language ' + Language.all.join(', '), :banner => 'source', :default => Language::ENGLISH]
    target_language_option = [:t, :required => false, :desc => 'Target language ' + Language.all.join(', '), :banner => 'target', :default => Language::ENGLISH]
    job_name_option = [:n, :required => false, :desc => 'Job name', :banner => 'jobname']
    job_options_option = [:J, :required => false, :desc => 'Job option (list key:value pairs after -J)', :banner => 'key:value', :type => :hash, :default => {}]
    caption_options_option = [:O, :required => false, :desc => 'Caption/transcript options (list key:value pairs after -O)', :banner => 'key:value', :type => :hash, :default => {}]
    turn_around_hours_option = [:T, :required => false, :desc => 'Turn around hours', :banner => 'hours']
    callback_url_option = [:C, :required => false, :desc => 'Callback URL', :banner => 'callback']
    caption_format_option = [:c, :required => false, :desc => 'Caption format ' + CaptionFormat.all.join(', '), :banner => 'format', :default => CaptionFormat::SRT]
    elementlist_version_option = [:e, :required => false, :desc => 'ElementList Version', :banner => 'version']
    force_new_option = [:F, :required => false, :desc => 'Force new key', :default => false]
    new_password_option = [:d, :required => true, :desc => 'New password', :banner => 'newpass']
    verbose_option = [:v, :require => false, :desc => 'Verbose mode', :hide => true, :default => false, :type => :boolean]

    class_option *server_url_option # Server URL can be specified for any action
    class_option *verbose_option # Verbose mode can be specified for any action

    desc 'login', 'Performs a login action'
    option :u, :required => true, :desc => 'cielo24 username', :type => :string, :banner => 'username'
    option :p, :required => false, :desc => 'cielo24 password', :banner => 'password'
    option :k, :required => false, :desc => 'The API Secure Key', :banner => 'securekey'
    option *header_option
    def login
      puts 'Performing a login action...'
      actions = initialize_actions
      token = actions.login(options[:u], options[:p], options[:k], options[:h])
      puts 'API token: ' + token
    end

    desc 'logout', 'Performs a logout action'
    option :N, :required => true, :desc => 'The API token of the current session', :banner => 'token'
    def logout
      puts 'Performing a logout action...'
      actions = initialize_actions
      actions.logout(options[:N])
      puts 'Logged out successfully'
    end

    desc 'create', 'Creates a job'
    option *fidelity_option
    option *priority_option
    option *source_language_option
    option *target_language_option
    option *media_url_option
    option *media_file_option
    option *job_name_option
    option *job_options_option
    option *turn_around_hours_option
    option *callback_url_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def create

      if options[:m].nil? and options[:M].nil?
        puts 'Media URL or local file path must be supplied'
        exit(1)
      end

      puts 'Creating job...'
      actions = initialize_actions
      token = get_token(actions)
      mash = actions.create_job(token, options[:n], options[:l])
      puts 'Job ID: ' + mash.JobId
      puts 'Task ID: ' + mash.TaskId

      puts 'Adding media...'
      if !options[:m].nil?
        task_id = actions.add_media_to_job_url(token, mash.JobId, options[:m])
      elsif !options[:M].nil?
        file = File.new(File.absolute_path(options[:M]), 'r')
        task_id = actions.add_media_to_job_file(token, mash.JobId, file)
      end
      puts 'Task ID: ' + task_id

      puts 'Performing transcription...'

      # Parse option hash
      jobopts = PerformTranscriptionOptions.new
      jobopts.populate_from_hash(options[:J])

      task_id = actions.perform_transcription(token, mash.JobId, options[:f], options[:P], options[:C], options[:T], options[:t], jobopts)
      puts 'Task ID: ' + task_id
    end

    desc 'delete', 'Delete a job'
    option *job_id_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def delete
      puts 'Deleting job...'
      actions = initialize_actions
      token = get_token(actions)
      task_id = actions.delete_job(token, options[:j])
      puts 'Task ID: ' + task_id
    end

    desc 'authorize', 'Authorize a job'
    option *job_id_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def authorize
      puts 'Authorizing job...'
      actions = initialize_actions
      token = get_token(actions)
      actions.authorize_job(token, options[:j])
      puts 'Authorized successfully'
    end

    desc 'add_media_to_job', 'Add media to job'
    option *job_id_option
    option *media_url_option
    option *media_file_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def add_media_to_job
      puts 'Adding media to job...'
      actions = initialize_actions
      token = get_token(actions)
      if !options[:m].nil?
        task_id = actions.add_media_to_job_url(token, options[:j], options[:m])
      elsif !options[:M].nil?
        file = File.new(File.absolute_path(options[:M]), 'r')
        task_id = actions.add_media_to_job_file(token, options[:j], file)
      else
        raise ArgumentError.new('Media URL or local file path must be supplied')
      end
      puts 'Task ID: ' + task_id
    end

    desc 'add_embedded_media_to_job', 'Add embedded media to job'
    option *job_id_option
    option :m, :required => true, :desc => 'Media URL', :banner => 'mediaurl'
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def add_embedded_media_to_job
      puts 'Adding embedded media to job...'
      actions = initialize_actions
      token = get_token(actions)
      task_id = actions.add_media_to_job_embedded(token, options[:j], options[:m])
      puts 'Task ID: ' + task_id
    end

    desc 'list', 'Lists current jobs'
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def list
      puts 'Retrieving list...'
      actions = initialize_actions
      token = get_token(actions)
      mash = actions.get_job_list(token)
      puts JSON.pretty_generate(JSON.parse(mash.to_json(nil)))
    end

    desc 'list_elementlists', 'List ElementLists'
    option *job_id_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def list_elementlists
      puts 'Listing Element Lists...'
      actions = initialize_actions
      token = get_token(actions)
      array = actions.get_list_of_element_lists(token, options[:j])
      puts JSON.pretty_generate(array)
    end

    desc 'get_caption', 'Get Caption'
    option *job_id_option
    option *caption_format_option
    option *elementlist_version_option
    option *caption_options_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def get_caption
      puts 'Getting caption...'
      actions = initialize_actions
      token = get_token(actions)

      # Parse options
      caption_opts = CaptionOptions.new
      caption_opts.populate_from_hash(options[:O])

      caption = actions.get_caption(token, options[:j], options[:c], caption_opts)
      puts caption
    end

    desc 'get_transcript', 'Get Transcript'
    option *job_id_option
    option *elementlist_version_option
    option *caption_options_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def get_transcript
      puts 'Getting transcript...'
      actions = initialize_actions
      token = get_token(actions)

      # Parse options
      transcription_opts = TranscriptOptions.new
      transcription_opts.populate_from_hash(options[:O])

      transcript = actions.get_transcript(token, options[:j], transcription_opts)
      puts transcript
    end

    desc 'get_elementlist', 'Get ElementList for JobId'
    option *job_id_option
    option *elementlist_version_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def get_elementlist
      puts 'Getting ElementList...'
      actions = initialize_actions
      token = get_token(actions)
      mash = actions.get_element_list(token, options[:j], options[:e])
      puts JSON.pretty_generate(JSON.parse(mash.to_json(nil)))
    end

    desc 'get_media', 'Get Media'
    option *job_id_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def get_media
      puts 'Getting media...'
      actions = initialize_actions
      token = get_token(actions)
      url = actions.get_media(token, options[:j])
      puts url
    end

    desc 'generate_api_key', 'Generate API Secure Key'
    option *force_new_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def generate_api_key
      puts 'Generating API key...'
      actions = initialize_actions
      token = get_token(actions)
      key = actions.generate_api_key(token, options[:u], options[:F])
      puts 'API Secure Key: ' + key
    end

    desc 'remove_api_key', 'Remove API Secure Key'
    option :api_key, :aliases => 'k', :required => true, :desc => 'The API Key to remove'
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def remove_api_key
      puts 'Removing API key...'
      actions = initialize_actions
      token = get_token(actions)
      actions.remove_api_key(token, options[:k])
      puts 'The key was successfully removed.'
    end

    desc 'update_password', 'Update Password'
    option *new_password_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def update_password
      puts 'Updating password...'
      actions = initialize_actions
      token = get_token(actions)
      actions.update_password(token, options[:d])
      puts 'Password was updated successfully.'
    end

    desc 'job_info', 'Get Job Info'
    option *job_id_option
    # always required (hidden)
    option *username_option
    option *password_option
    option *securekey_option
    option *api_token_option
    def job_info
      puts 'Getting Job Info...'
      actions = initialize_actions
      token = get_token(actions)
      mash = actions.get_job_info(token, options[:j])
      puts JSON.pretty_generate(JSON.parse(mash.to_json(nil)))
    end

    # Method override, so that an 'always required' message can be printed out before everything else
    def help(arg=nil, arg2=nil)
      super(arg, arg2)
      puts "\nAlways required options:"
      puts "  -u=username          \# cielo24 username"
      puts "  [-s=serverurl]       \# cielo24 server URL"
      puts "                       \# Default: https://api.cielo24.com"
      puts "\n  ++Either one of the following:"
      puts "  --------------------------------------------"
      puts "  -p=password          \# cielo24 password"
      puts "  -k=securekey         \# The API Secure Key"
      puts "  -N=token             \# The API token of the current session"
      puts "  --------------------------------------------"
    end

    no_commands{
      def private_login(actions, username, password, securekey)
        raise ArgumentError.new('Username was not supplied.') if username.nil?
        return actions.login(username, password, securekey, true)
      end

      def initialize_actions
        actions = Actions.new
        actions.base_url = options[:s] unless options[:s].nil?
        setup_logger()
        return actions
      end

      def get_token(actions)
        return (options[:N].nil?) ? private_login(actions, options[:u], options[:p], options[:k]) : options[:N]
      end

      def setup_logger
        if options[:v]
          # Custom logger formatter
          WebUtils::LOGGER.formatter = proc { |severity, datetime, progname, msg|
            msg + "\n"
          }
        else
          # Disable logger
          WebUtils::LOGGER.level = Logger::ERROR
        end
      end
    }
  end
end