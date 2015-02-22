require 'test/unit'
require '../lib/cielo24/actions'
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