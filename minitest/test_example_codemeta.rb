#!/usr/bin/env ruby
require 'minitest/autorun'

require 'json/ld'

describe 'example-codemeta.json' do
  it 'parses to a non-empty graph' do
    input = JSON.parse(File.read('example-codemeta.json'))
    refute JSON::LD::API.toRdf(input).empty?
  end
end

