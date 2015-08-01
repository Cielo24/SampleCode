require 'test/unit'
require '../lib/cielo24/actions'
require '../lib/cielo24/web_utils'
require '../lib/cielo24/options'
require './actions_test'
require 'uri'
include Cielo24

class JobTest < ActionsTest

  # Called before every test method runs. Can be used to set up fixture information.
  def setup
    super
    # Always start with a fresh job
    @job_id = @actions.create_job(@api_token, 'Ruby_test').JobId
  end

  # Since all option classes extend BaseOptions class (with all of the functionality) we only need to test one class
  def test_options
    options = CaptionOptions.new
    options.populate_from_hash({build_url: true, dfxp_header: 'header'})
    options.force_case = Case::UPPER
    options.caption_by_sentence = true
    # Can only assert length because hash produces different order each time
    assert_equal('build_url=true&caption_by_sentence=true&dfxp_header=header&force_case=upper'.length, options.to_query.length)
  end

  def test_create_job
    response = @actions.create_job(@api_token, 'Ruby_test', Language::ENGLISH)
    assert_equal(32, response['JobId'].length)
    assert_equal(32, response['TaskId'].length)
  end

  def test_authorize_job
    @actions.authorize_job(@api_token, @job_id)
  end

  def test_delete_job
    @task_id = @actions.delete_job(@api_token, @job_id)
    assert_equal(32, @task_id.length)
  end

  def test_get_job_info
    response = @actions.get_job_info(@api_token, @job_id)
    assert_not_nil(response.JobId)
  end

  def test_get_job_list
    response = @actions.get_job_list(@api_token)
    assert_not_nil(response.ActiveJobs)
  end

  def test_get_element_list
    response = @actions.get_element_list(@api_token, @job_id)
    assert_not_nil(response.version)
  end

  def test_get_list_of_element_lists
    response = @actions.get_list_of_element_lists(@api_token, @job_id)
    assert(response.instance_of?(Array))
  end

  def test_get_media
    # Add media to job first
    @actions.add_media_to_job_url(@api_token, @job_id, @config.sample_video_url)
    # Test get media
    media_url = @actions.get_media(@api_token, @job_id)
    fail if media_url !~ URI::regexp # Fail if response is not a URI
  end

  def test_get_transcript
    @actions.get_transcript(@api_token, @job_id)
  end

  def test_get_caption
    @actions.get_caption(@api_token, @job_id, CaptionFormat::SRT)
  end

  def test_get_caption_build_url
    options = CaptionOptions.new
    options.build_url = true
    caption_url = @actions.get_caption(@api_token, @job_id, CaptionFormat::SRT, options)
    fail if caption_url !~ URI::regexp
  end

  def test_perform_transcription
    @task_id = @actions.add_media_to_job_url(@api_token, @job_id, @config.sample_video_url)
    assert_equal(32, @task_id.length)
    callback_url = 'http://fake-callback.com/action?api_token=1234&job_id={job_id}'
    @task_id = @actions.perform_transcription(@api_token, @job_id, Fidelity::PREMIUM, Priority::STANDARD, callback_url)
    assert_equal(32, @task_id.length)
  end

  def test_add_media_to_job_url
    @task_id = @actions.add_media_to_job_url(@api_token, @job_id, @config.sample_video_url)
    assert_equal(32, @task_id.length)
  end

  def test_add_media_to_job_embedded
    @task_id = @actions.add_media_to_job_embedded(@api_token, @job_id, @config.sample_video_url)
    assert_equal(32, @task_id.length)
  end

  def test_add_media_to_job_file
    file = open(@config.sample_video_file_path, 'rb')
    @task_id = @actions.add_media_to_job_file(@api_token, @job_id, file)
    assert_equal(32, @task_id.length)
  end
end