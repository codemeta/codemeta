require 'rubygems'
require 'json/ld'
require 'easy_diff'
require 'minitest/autorun'

# This test checks a document that contains all the current CodeMeta terms
# that are represented in CodeMeta schema (codemeta.jsonld). If any of
# the JSON names that appear in the test document are not in the schema
# then they will be silently discarded when the JSON-LD API operations
# are performed on the document. In this test the 'expansion' and
# 'compaction' operations are performed. The resulting JSON text
# should be the same as the original test document. 

describe 'example-codemeta-full.json' do
  before do
    input = JSON.parse(File.read('example-codemeta-full.json'))
    # Transform the test document with the json-ld expand operation.
    # Any JSON terms that are not in the @context will be discarded
    # silently, as they are not 'linked' to any schema.
    @expanded = JSON::LD::API.expand(input)
    # Read in the context document that will be required to compact
    # the expanded document. 
    context = JSON.parse(File.read('codemeta.jsonld'))['@context']
    # Transform the expanded JSON object with json-ld compact operation.
    @compacted =  JSON::LD::API.compact(@expanded, context) 
    # Remove the '@context' object from the document - the compact
    # operation puts this in the result with all values listed, so remove
    # it for comparison to the original which may have just had a URL
    # to specify the context.
    @compacted.delete('@context')
    # Compare the input JSON object to the compacted one.
    # Now that we are done transforming the input, the @context can be removed
    # to aid in the diff process.
    input.delete('@context')
    @removed, @added = input.easy_diff @compacted
  end

  it 'json-ld expand and compact does not lose data' do
    assert_empty @removed, 'JSON terms are in input document that were not transformed by JSON-LD expand / conpact operations'
  end
end

