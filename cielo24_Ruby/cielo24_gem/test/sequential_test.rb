require 'test/unit'
require '../lib/cielo24/actions'
require '../lib/cielo24/web_utils'
require '../lib/cielo24/options'
require_relative 'actions_test'
require 'uri'
include Cielo24

class SequentialTest < ActionsTest

  # Called before every test method runs. Can be used to set up fixture information.
  def setup
    # Do nothing - we want to be able to control when we login/logout etc.
  end
  
  def test_sequence
    # Login, generate API key, logout
    @api_token = @actions.login(@config.username, @config.password)
    @secure_key = @actions.generate_api_key(@api_token, @config.username, true)
    @actions.logout(@api_token)
    @api_token = nil

    # Login using API key
    @api_token = @actions.login(@config.username, nil, @secure_key)

    # Create a job using a media URL
    @job_id = @actions.create_job(@api_token, 'Ruby_test').JobId
    @actions.add_media_to_job_url(@api_token, @job_id, @config.sample_video_url)

    # Assert JobList and JobInfo data
    job_list = @actions.get_job_list(@api_token)
    assert(contains_job(@job_id, job_list), 'JobId not found in JobList')
    job = @actions.get_job_info(@api_token, @job_id)
    assert_equal(@job_id, job.JobId, 'Wrong JobId found in JobInfo')

    # Logout
    @actions.logout(@api_token)
    @api_token = nil

    # Login/logout/change password
    @api_token = @actions.login(@config.username, @config.password)
    @actions.update_password(@api_token, @config.new_password)
    @actions.logout(@api_token)
    @api_token = nil

    # Change password back
    @api_token = @actions.login(@config.username, @config.new_password)
    @actions.update_password(@api_token, @config.password)
    @actions.logout(@api_token)
    @api_token = nil

    # Login using API key
    @api_token = @actions.login(@config.username, nil, @secure_key)

    # Delete job and assert JobList data
    @actions.delete_job(@api_token, @job_id)
    job_list2 = @actions.get_job_list(@api_token)
    assert_equal(false, contains_job(@job_id, job_list2), 'JobId should not be in JobList')

    # Delete current API key and try to re-login (should fail)
    @actions.remove_api_key(@api_token, @secure_key)
    @actions.logout(@api_token)
    @api_token = nil

    begin
      @api_token = @actions.login(@config.username, @secure_key)
      fail('Should not be able to login using invalid API key')
    rescue WebError => e
      assert_equal(ErrorType::ACCOUNT_UNPRIVILEGED, e.type, 'Unexpected error type')
    end
  end


  def contains_job(job_id, job_list)
    job_list.ActiveJobs.each do |j|
      if job_id.eql? j.JobId
        return true
      end
    end
    return false
  end
end