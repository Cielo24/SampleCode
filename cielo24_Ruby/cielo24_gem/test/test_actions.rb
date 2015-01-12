require 'test/unit'
require '../lib/cielo24/actions'
require '../lib/cielo24/web_utils'
require '../lib/cielo24/options'
require 'uri'
include Cielo24

class ActionsTest < Test::Unit::TestCase
  @@actions = Cielo24::Actions.new("http://sandbox-dev.cielo24.com")
  @@username = "api_test"
  @@password = "api_test"
  @@new_password = "api_test_new"
  @@api_token = nil
  @@secure_key = nil

  # Called before every test method runs. Can be used
  # to set up fixture information.
  def setup
    if @@api_token.nil?
      @@api_token = @@actions.login(@@username, @@password, nil, true)
    end
    if @@secure_key.nil?
      @@secure_key = @@actions.generate_api_key(@@api_token, @@username, false)
    end
  end
end

class AccessTest < ActionsTest

  # Username, password, no headers
  def test_login_password_no_headers()
    @@api_token = @@actions.login(@@username, @@password)
    assert_equal(32, @@api_token.length)
  end

  # Username, password, headers
  def test_login_password_headers()
    @@api_token = @@actions.login(@@username, @@password, nil, true)
    assert_equal(32, @@api_token.length)
  end

  # Username, secure key, no headers
  def test_login_securekey_no_headers()
    @@api_token = @@actions.login(@@username, nil, @@secure_key)
    assert_equal(32, @@api_token.length)
  end

  # Username, secure key, headers
  def test_login_securekey_headers()
    @@api_token = @@actions.login(@@username, nil, @@secure_key, true)
    assert_equal(32, @@api_token.length)
  end

  # Logout
  def test_logout()
    @@actions.logout(@@api_token)
    @@api_token = nil
  end

  # Generate API key with force_new option
  def test_generate_api_key_force_new()
    @@secure_key = @@actions.generate_api_key(@@api_token, @@username, false)
    assert_equal(32, @@secure_key.length)
  end

  # Generate API key with force_new option
  def test_generate_api_key_not_force_new()
    @@secure_key = @@actions.generate_api_key(@@api_token, @@username, true)
    assert_equal(32, @@secure_key.length)
  end

  # Remove API key
  def test_remove_api_key()
    @@actions.remove_api_key(@@api_token, @@secure_key)
    @@secure_key = nil
  end

  # Update password
  def test_update_password()
    @@actions.update_password(@@api_token, @@new_password)
    @@actions.update_password(@@api_token, @@password)
  end
end

class JobTest < ActionsTest
  @@sample_video_url = "http://techslides.com/demos/sample-videos/small.mp4"
  @@sample_video_file_path = "C:/path/to/file.mp4"
  @@job_id = nil
  @@task_id = nil

  # Called before every test method runs. Can be used to set up fixture information.
  def setup
    super
    # Always start with a fresh job
    @@job_id = @@actions.create_job(@@api_token).JobId
  end

  # Since all option classes extend BaseOptions class (with all of the functionality) we only need to test one class
  def test_options()
    options = CaptionOptions.new
    options.build_url = true
    options.dfxp_header = "header"
    assert_equal("build_url=true&dfxp_header=header", options.to_query)
  end

  def test_create_job()
    response = @@actions.create_job(@@api_token, "test_name", Language.English)
    assert_equal(32, response['JobId'].length)
    assert_equal(32, response['TaskId'].length)
  end

  def test_authorize_job()
    @@actions.authorize_job(@@api_token, @@job_id)
  end

  def test_delete_job()
    @@task_id = @@actions.delete_job(@@api_token, @@job_id)
    assert_equal(32, @@task_id.length)
  end

  def test_get_job_info()
    response = @@actions.get_job_info(@@api_token, @@job_id)
    assert_not_nil(response.JobId)
  end

  def test_get_job_list()
    response = @@actions.get_job_list(@@api_token)
    assert_not_nil(response.ActiveJobs)
  end

  def test_get_element_list()
    response = @@actions.get_element_list(@@api_token, @@job_id)
    assert_not_nil(response.version)
  end

  def test_get_list_of_element_lists()
    response = @@actions.get_list_of_element_lists(@@api_token, @@job_id)
    assert(response.instance_of?(Array))
  end

  def test_get_media()
    # Add media to job first
    @@actions.add_media_to_job_url(@@api_token, @@job_id, @@sample_video_url)
    # Test get media
    media_url = @@actions.get_media(@@api_token, @@job_id)
    fail if media_url !~ URI::regexp # Fail if response is not a URI
  end

  def test_get_transcript()
    @@actions.get_transcript(@@api_token, @@job_id)
  end

  def test_get_caption()
    @@actions.get_caption(@@api_token, @@job_id, CaptionFormat.SRT)
  end

  def test_get_caption_build_url()
    options = CaptionOptions.new(build_url=true)
    caption_url = @@actions.get_caption(@@api_token, @@job_id, CaptionFormat.SRT, options)
    fail if caption_url !~ URI::regexp
  end

  def test_perform_transcription()
    @@task_id = @@actions.add_media_to_job_url(@@api_token, @@job_id, @@sample_video_url)
    assert_equal(32, @@task_id.length)
    @@task_id = @@actions.perform_transcription(@@api_token, @@job_id, Fidelity.PREMIUM, Priority.STANDARD)
    assert_equal(32, @@task_id.length)
  end

  def test_add_media_to_job_url()
    @@task_id = @@actions.add_media_to_job_url(@@api_token, @@job_id, @@sample_video_url)
    assert_equal(32, @@task_id.length)
  end

  def test_add_media_to_job_embedded()
    @@task_id = @@actions.add_media_to_job_embedded(@@api_token, @@job_id, @@sample_video_url)
    assert_equal(32, @@task_id.length)
  end

  def test_add_media_to_job_file()
    file = open(@@sample_video_file_path, "rb")
    @@task_id = @@actions.add_media_to_job_file(@@api_token, @@job_id, file)
    assert_equal(32, @@task_id.length)
  end
end