require 'rubygems'
require 'json/ld'
require 'minitest/autorun'
require 'json-schema'

# This test checks a document that contains all the current CodeMeta terms
# that are represented in CodeMeta schema (codemeta.jsonld). If any of
# the JSON names that appear in the test document are not in the schema
# then they will be silently discarded when the JSON-LD API operations
# are performed on the document. In this test the 'expansion' and
# 'compaction' operations are performed. The resulting JSON text
# should be the same as the original test document.

describe 'example-codemeta-schema' do
  before do
    input = JSON.parse(File.read('examples/example-codemeta-full.json'))
    schema = JSON.parse(File.read('codemeta-json-schema.json'))
    @errorMsgs = JSON::Validator.fully_validate(schema, input)
  end

  it 'CodeMeta example file validates with CodeMeta JSON schema' do
    assert_empty @errorMsgs, 'example-codemeta-full.json does not validate against CodeMeta JSON schema'
  end
end

describe 'example-codemeta-agent' do
  before do
    input = JSON.parse(File.read('examples/example-codemeta-agent.json'))
    schema = JSON.parse(File.read('codemeta-json-schema.json'))
    @errorMsgs = JSON::Validator.fully_validate(schema, input)
  end

  it 'CodeMeta exmaple file validates with CodeMeta JSON schema' do
    assert_empty @errorMsgs, 'example-codemeta-agent.json does not validate against CodeMeta JSON schema'
  end
end

describe 'example-codemeta-rdataone' do
  before do
    input = JSON.parse(File.read('examples/example-codemeta-rdataone.json'))
    schema = JSON.parse(File.read('codemeta-json-schema.json'))
    @errorMsgs = JSON::Validator.fully_validate(schema, input)
  end

  it 'CodeMeta exmaple file validates with CodeMeta JSON schema' do
    assert_empty @errorMsgs, 'example-codemeta-rdataone.json does not validate against CodeMeta JSON schema'
  end
end

describe 'example-codemeta-full-invalid' do
  before do
    input = JSON.parse(File.read('examples/example-codemeta-full-invalid.json'))
    schema = JSON.parse(File.read('codemeta-json-schema.json'))
    @errorMsgs = JSON::Validator.fully_validate(schema, input)
  end

  it 'CodeMeta exmaple file validates with CodeMeta JSON schema' do
    assert @errorMsgs, 'example-codemeta-full-invalid.json does not generate a validation error for CodeMeta JSON schema (it should!).'
  end
end
