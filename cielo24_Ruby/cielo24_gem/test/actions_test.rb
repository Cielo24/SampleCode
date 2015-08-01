require 'test/unit'
require '../lib/cielo24/actions'
require './configuration'


class ActionsTest < Test::Unit::TestCase

  def initialize(test_method_name)
    super(test_method_name)
    @config = Configuration.new
    @actions = Cielo24::Actions.new(@config.server_url)
    @api_token = nil
    @secure_key = nil
  end

  # Called before every test method runs. Can be used to set up fixture information.
  def setup
    # Start with a fresh session each time
    @api_token = @actions.login(@config.username, @config.password, nil, true)
    @secure_key = @actions.generate_api_key(@api_token, @config.username, false)
  end
end