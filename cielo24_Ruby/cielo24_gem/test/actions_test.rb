require 'test/unit'
require '../lib/cielo24/actions'
require '../lib/cielo24/web_utils'
require '../lib/cielo24/options'
include Cielo24

class AccessTest < Test::Unit::TestCase
  @@sample_video_url = "http://techslides.com/demos/sample-videos/small.mp4"
  @@sample_video_file_path = "C:/path/to/file.mp4"
  @@actions = Cielo24::Actions.new("http://sandbox-dev.cielo24.com")
  @@username = "api_test"
  @@password = "api_test"
  @@new_password = "api_test_new"
  @@api_token = nil
  @@job_id = nil

  # Called before every test method runs. Can be used
  # to set up fixture information.
  def setup
    if @@api_token.nil?
      @@api_token = @@actions.login(@@username, @@password, nil, true)
    end
    if @@job_id.nil?
      @@job_id = @@actions.create_job(@@api_token).JobId
    end
  end

  def test_options
    co = CaptionOptions.new(caption_words_min:25)
    co.build_url = true
    co.dfxp_header = "header"
    assert_equal("build_url=true&caption_words_min=25&dfxp_header=header", co.to_query)
  end

  def test_login_and_logout
    # Username, password, no headers
    assert_nothing_raised{@@api_token = @@actions.login(@@username, @@password)}
    assert_equal(32, @@api_token.length)
    # Username, password, headers
    assert_nothing_raised{@@api_token = @@actions.login(@@username, @@password, nil, true)}
    assert_equal(32, @@api_token.length)
    @secure_key = @@actions.generate_api_key(@@api_token, @@username, false)
    # Username, secure key, no headers
    assert_nothing_raised{@@api_token = @@actions.login(@@username, nil, @secure_key)}
    assert_equal(32, @@api_token.length)
    # Username, secure key, headers
    assert_nothing_raised{@@api_token = @@actions.login(@@username, nil, @secure_key, true)}
    assert_equal(32, @@api_token.length)
    # Logout
    assert_nothing_raised{@@actions.logout(@@api_token)}
    #assert_raise(WebError) {@@actions.logout("123")}
    @@api_token = nil
  end

  def test_generate_and_remove_api_key
    assert_nothing_raised{@secure_key = @@actions.generate_api_key(@@api_token, @@username, false)}
    assert_equal(32, @secure_key.length)
    assert_nothing_raised{@secure_key = @@actions.generate_api_key(@@api_token, @@username, true)}
    assert_equal(32, @secure_key.length)
    assert_nothing_raised{@@actions.remove_api_key(@@api_token, @secure_key)}
  end

  def test_update_password
    assert_nothing_raised{@@actions.update_password(@@api_token, @@new_password)}
    assert_nothing_raised{@@actions.update_password(@@api_token, @@password)}
    assert_raise(WebError) {@@actions.update_password("not_an_api_token", @@password)}
  end

  def test_create_job
    assert_nothing_raised{@mash = @@actions.create_job(@@api_token, "testname", "en")}
    assert_equal(32, @mash.JobId.length)
    assert_equal(32, @mash.TaskId.length)
  end

  def test_authorize_job
    assert_nothing_raised{@@actions.authorize_job(@@api_token, @@job_id)}
    @@job_id = nil
  end

  def test_delete_job
    assert_nothing_raised{@task_id = @@actions.delete_job(@@api_token, @@job_id)}
    assert_equal(32, @task_id.length)
    @@job_id = nil
  end

  def test_gets
    assert_nothing_raised{@mash = @@actions.get_job_info(@@api_token, @@job_id)}
    assert_nothing_raised{@@actions.get_job_list(@@api_token)}
    assert_nothing_raised{@@actions.get_element_list(@@api_token, @@job_id)}
    assert_nothing_raised{@@actions.get_list_of_element_lists(@@api_token, @@job_id)}
    assert_nothing_raised{@@actions.get_media(@@api_token, @@job_id)}
  end

  def test_get_text
    assert_nothing_raised{@@actions.get_caption(@@api_token, @@job_id, "SRT")}
    assert_nothing_raised{@@actions.get_transcript(@@api_token, @@job_id)}
    co = CaptionOptions.new
    co.build_url = true
    assert_nothing_raised{@text = @@actions.get_caption(@@api_token, @@job_id, "SRT", co)}
    assert_match("http", @text) # URL must be returned
  end

  def test_perform_transcription
    assert_nothing_raised{@task_id = @@actions.add_media_to_job_url(@@api_token, @@job_id, @@sample_video_url)}
    assert_equal(32, @task_id.length)
    assert_nothing_raised{@task_id = @@actions.perform_transcription(@@api_token, @@job_id, "PREMIUM", "STANDARD")}
    assert_equal(32, @task_id.length)
  end

  def test_add_data
    assert_nothing_raised{@task_id = @@actions.add_media_to_job_url(@@api_token, @@job_id, @@sample_video_url)}
    assert_equal(32, @task_id.length)
    @@job_id = @@actions.create_job(@@api_token).JobId
    assert_nothing_raised{@task_id = @@actions.add_media_to_job_embedded(@@api_token, @@job_id, @@sample_video_url)}
    assert_equal(32, @task_id.length)
    @@job_id = @@actions.create_job(@@api_token).JobId
    file = File.open(@@sample_video_file_path, "r")
    assert_nothing_raised{@task_id = @@actions.add_media_to_job_file(@@api_token, @@job_id, file)}
    assert_equal(32, @task_id.length)
  end

  # Called after every test method runs. Can be used to tear down fixture information.
  def teardown
    # Do nothing
  end
end