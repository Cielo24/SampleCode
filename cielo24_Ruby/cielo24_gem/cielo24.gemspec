# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'cielo24/version'

Gem::Specification.new do |spec|
  spec.name          = "cielo24"
  spec.version       = Cielo24::VERSION
  spec.authors       = ["Evgeny Chistyakov"]
  spec.email         = ["support@cielo24.com"]
  spec.summary       = %q{Cielo24 API gem.}
  spec.description   = %q{This gem allows you to interact with the cielo24 public web API.}
  spec.homepage      = "http://cielo24.com"
  spec.license       = "MIT"

  spec.files         = Dir['lib/cielo24/*.rb'] + Dir['lib/*.rb']
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ["lib"]

  spec.add_development_dependency "bundler", "~> 1.6"
  spec.add_development_dependency "rake", "~> 10.0"

  spec.add_dependency "httpclient"
  spec.add_dependency "hashie"
end
