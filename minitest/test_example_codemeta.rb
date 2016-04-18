require 'json/ld'
require 'minitest/autorun'

describe 'example-codemeta.json' do
  before do
    @input = JSON.parse(File.read('example-codemeta.json'))
    @graph = RDF::Graph.new << JSON::LD::API.toRdf(@input)
  end

  it 'parses to a non-empty graph' do
    refute @graph.empty?
  end

  it 'has an email' do
    emails =  @graph.query(subject:   nil, 
                           predicate: RDF::URI('http://schema.org/email'), 
                           object:    nil)
    refute emails.empty?
  end
end
