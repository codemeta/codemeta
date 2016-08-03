require 'rubygems'
require 'json/ld'
require 'easy_diff'
require 'minitest/autorun'

# This test checks that an invalid value in the input document
# should be excluded from the result of the JSON-LD expand / compact 
# operations, for example "_not_in_schema" should not be included in
# the result. This test uses the same mechanism as the
# 'test_example_codemeta_full.rb' test, so if the current 'fail'
# test passes, it helps to validate the 'full' test.

describe 'example-codemeta-invalid.json' do
  before do
    input = JSON.parse(File.read('example-codemeta-invalid.json'))
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
    refute @removed.empty?, 'Invalid JSON name in input document should be discarded during JSON-LD expand / conpact operations'
  end
end

