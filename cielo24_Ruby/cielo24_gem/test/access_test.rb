require 'test/unit'
require '../lib/cielo24/actions'
require '../lib/cielo24/web_utils'
require './actions_test'
include Cielo24


class AccessTest < ActionsTest

  # Username, password, no headers
  def test_login_password_no_headers
    @api_token = @actions.login(@config.username, @config.password)
    assert_equal(32, @api_token.length)
  end

  # Username, password, headers
  def test_login_password_headers
    @api_token = @actions.login(@config.username, @config.password, nil, true)
    assert_equal(32, @api_token.length)
  end

  # Username, secure key, no headers
  def test_login_securekey_no_headers
    @api_token = @actions.login(@config.username, nil, @secure_key)
    assert_equal(32, @api_token.length)
  end

  # Username, secure key, headers
  def test_login_securekey_headers
    @api_token = @actions.login(@config.username, nil, @secure_key, true)
    assert_equal(32, @api_token.length)
  end

  # Logout
  def test_logout
    @actions.logout(@api_token)
    begin
      @actions.get_job_list(@api_token)
      fail('Should not be able to use the API with invalid API token')
    rescue WebError => e
      assert_equal(ErrorType::BAD_API_TOKEN, e.type, 'Unexpected error type')
    end
  end

  # Generate API key with force_new option
  def test_generate_api_key_force_new
    @secure_key = @actions.generate_api_key(@api_token, @config.username, false)
    assert_equal(32, @secure_key.length)
  end

  # Generate API key with force_new option
  def test_generate_api_key_not_force_new
    @secure_key = @actions.generate_api_key(@api_token, @config.username, true)
    assert_equal(32, @secure_key.length)
  end

  # Remove API key
  def test_remove_api_key
    @actions.remove_api_key(@api_token, @secure_key)
    begin
      @api_token = @actions.login(@config.username, @secure_key)
      fail('Should not be able to login using invalid API key')
    rescue WebError => e
      assert_equal(ErrorType::ACCOUNT_UNPRIVILEGED, e.type, 'Unexpected error type')
    end
  end

  # Update password
  def test_update_password
    @actions.update_password(@api_token, @config.new_password)
    @actions.update_password(@api_token, @config.password)
  end
end