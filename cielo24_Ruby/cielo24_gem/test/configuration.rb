class Configuration
  attr_accessor :server_url
  attr_accessor :username
  attr_accessor :password
  attr_accessor :new_password
  attr_accessor :sample_video_url
  attr_accessor :sample_video_file_path

  def initialize
    @server_url = "http://sandbox-dev.cielo24.com"
    @username = "api_test"
    @password = "api_test"
    @new_password = "api_test_new"
    @sample_video_url = "http://techslides.com/demos/sample-videos/small.mp4"
    @sample_video_file_path = "C:/path/to/file.mp4"
  end
end