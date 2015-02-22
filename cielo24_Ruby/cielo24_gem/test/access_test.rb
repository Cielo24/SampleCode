require 'test/unit'
require '../lib/cielo24/actions'
require '../lib/cielo24/web_utils'
require './actions_test'
include Cielo24

class AccessTest < ActionsTest

  # Username, password, no headers
  def test_login_password_no_headers
    @@api_token = @@actions.login(@@username, @@password)
    assert_equal(32, @@api_token.length)
  end

  # Username, password, headers
  def test_login_password_headers
    @@api_token = @@actions.login(@@username, @@password, nil, true)
    assert_equal(32, @@api_token.length)
  end

  # Username, secure key, no headers
  def test_login_securekey_no_headers
    @@api_token = @@actions.login(@@username, nil, @@secure_key)
    assert_equal(32, @@api_token.length)
  end

  # Username, secure key, headers
  def test_login_securekey_headers
    @@api_token = @@actions.login(@@username, nil, @@secure_key, true)
    assert_equal(32, @@api_token.length)
  end

  # Logout
  def test_logout
    @@actions.logout(@@api_token)
    @@api_token = nil
  end

  # Generate API key with force_new option
  def test_generate_api_key_force_new
    @@secure_key = @@actions.generate_api_key(@@api_token, @@username, false)
    assert_equal(32, @@secure_key.length)
  end

  # Generate API key with force_new option
  def test_generate_api_key_not_force_new
    @@secure_key = @@actions.generate_api_key(@@api_token, @@username, true)
    assert_equal(32, @@secure_key.length)
  end

  # Remove API key
  def test_remove_api_key
    @@actions.remove_api_key(@@api_token, @@secure_key)
    @@secure_key = nil
  end

  # Update password
  def test_update_password
    @@actions.update_password(@@api_token, @@new_password)
    @@actions.update_password(@@api_token, @@password)
  end
end