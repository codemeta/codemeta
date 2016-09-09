require 'minitest/autorun'
require 'json/ld'

describe 'example-codemeta-agent.json' do
  before do
    @input = JSON.parse(File.read('examples/example-codemeta-agent.json'))
    @graph = JSON::LD::API.toRdf(@input)
  end
  
  it 'parses to a non-empty graph' do
    refute @graph.empty?
  end
end
