
require 'rubygems'
require 'json/ld'
require 'sparql'
require 'rdf/nquads'
require 'minitest/autorun'

describe 'example-codemeta-full.json deserialized to RDF' do
  before (:all) do
    @input = JSON.parse(File.read('example-codemeta-full.json'))
    @graph = RDF::Graph.new << JSON::LD::API.toRdf(@input)
  end

  it 'parses to a non-empty graph' do
    refute @graph.empty?
  end

  it 'has an author orcid' do
    sse = SPARQL.parse("PREFIX so: <http://schema.org/>
                        PREFIX cm: <https://codemeta.github.io/terms/>
                        PREFIX orcid: <http://orcid.org/>
                        SELECT * WHERE { orcid:0000-0002-2192-403X ?p ?o  }")
    resultSet = @graph.query(sse)
    #resultSet.each do |result|
      #puts result.inspect
      #puts "predicate=#{result.p} object=#{result.o}"
    #end
    refute resultSet.empty?
  end

  it 'has agent' do
    sse = SPARQL.parse("PREFIX so: <http://schema.org/>
                      PREFIX cm: <https://codemeta.github.io/terms/>
                      PREFIX orcid: <http://orcid.org/>
                      SELECT * WHERE { ?s <http://schema.org/agent> ?o  }")
    resultSet = @graph.query(sse)
    #resultSet.each do |result|
    #  puts result.inspect
    #end
    refute resultSet.empty?
  end

  it 'has schema.org predicates' do
     queryStr = "PREFIX so: <http://schema.org/>
                 PREFIX cm: <https://codemeta.github.io/terms/>
                 PREFIX orcid: <http://orcid.org/>
                 SELECT * WHERE { ?s <http://schema.org/JSONTerm> ?o  }"
     # Check statements with schema.org based predicate
     predicates = ["affiliation", "codeRepository", "dateCreated", "dateModified", "datePublished",
                  "description", "downloadUrl", "email", "keywords", "license",
                 "programmingLanguage", "publisher", "suggests",
                 "version", "URL", "name"]
     predicates.each do |thisPredicate|
         thisQueryStr = queryStr.gsub("JSONTerm", thisPredicate)
         sse = SPARQL.parse(thisQueryStr)
         resultSet = @graph.query(sse)
         #resultSet.each do |result|
           #puts result.inspect
         #nd
         refute resultSet.empty?
     end
   end

  it 'has codemeta predicates' do
     queryStr = "PREFIX so: <http://schema.org/>
                 PREFIX cm: <https://codemeta.github.io/terms/>
                 PREFIX orcid: <http://orcid.org/>
                 SELECT * WHERE { ?s <https://codemeta.github.io/terms/JSONTerm> ?o  }"
     # Check statements with codemeta namespaced predicate
     predicates = ["buildInstructions", "contIntegration",
       "embargoDate", "function", "funding", "inputs", "interactionMethod",
       "isAutomatedBuild", "isMaintainer", "isRightsHolder", "issueTracker", "mustBeCited", "namespace", "outputs",
       "packageId", "packageSystem", "readme", "relatedLink",
       "relatedPublications", "relationship", "requirement", "Role", "roleCode", "softwareCitation", "softwarePaperCitation",
       "testCoverage", "uploadedBy", "zippedCode"]
     predicates.each do |thisPredicate|
         thisQueryStr = queryStr.gsub("JSONTerm", thisPredicate)
         sse = SPARQL.parse(thisQueryStr)
         resultSet = @graph.query(sse)
         #resultSet.each do |result|
          # puts result.inspect
         #end
         refute resultSet.empty?
     end
  end

  it 'has dcterms' do
     queryStr = "PREFIX so: <http://schema.org/>
                 PREFIX cm: <https://codemeta.github.io/terms/>
                 PREFIX orcid: <http://orcid.org/>
                 SELECT * WHERE { ?s <http://purl.org/dc/terms/JSONTerm> ?o  }"
     # Check statements with codemeta namespaced predicate
     predicates = ["identifier", "title"]
     predicates.each do |thisPredicate|
         thisQueryStr = queryStr.gsub("JSONTerm", thisPredicate)
         sse = SPARQL.parse(thisQueryStr)
         resultSet = @graph.query(sse)
         #resultSet.each do |result|
          # puts result.inspect
         #end
         refute resultSet.empty?
     end
   end
end
