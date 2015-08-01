# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'cielo24_cli/version'

Gem::Specification.new do |spec|
  spec.name          = 'cielo24-cli'
  spec.version       = Cielo24CLI::VERSION
  spec.authors       = ['cielo24']
  spec.email         = ['support@cielo24.com']
  spec.summary       = %q{Command line interface to cielo24 gem.}
  spec.description   = %q{Command line interface that allows you to make REST API calls using cielo24 gem.}
  spec.homepage      = 'http://cielo24.com'
  #spec.license       = 'MIT'

  spec.files         = Dir['lib/cielo24_cli/*.rb'] + Dir['lib/*.rb']
  spec.executables   = ['cielo24cli'] #spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ['lib']

  spec.add_development_dependency 'bundler', '~> 1.10.6'
  spec.add_development_dependency 'rake', '~> 10.4.2'

  spec.add_dependency 'cielo24', '~> 0.0.15'
  spec.add_dependency 'thor', '~> 0.19.1'
end
