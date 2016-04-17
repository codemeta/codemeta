#!/usr/bin/env ruby

require 'json/ld'

input = JSON.parse(File.read('example-codemeta.json'))
rdf = JSON::LD::API.toRdf(input)

raise if rdf.empty?

