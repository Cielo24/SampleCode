require 'test/unit'
require '../lib/cielo24/actions'
require_relative 'configuration'
include Cielo24

class ActionsTest < Test::Unit::TestCase

  @@config = Configuration.new
  @@actions = Cielo24::Actions.new(@@config.server_url)
  @@api_token = nil
  @@secure_key = nil

  # Called before every test method runs. Can be used
  # to set up fixture information.
  def setup
    if @@api_token.nil?
      @@api_token = @@actions.login(@@config.username, @@config.password, nil, true)
    end
    if @@secure_key.nil?
      @@secure_key = @@actions.generate_api_key(@@api_token, @@config.username, false)
    end
  end
end