
## call rmarkdown on all .Rmd files
#f <- list.files(recursive = TRUE)
#lapply(f[grepl(".Rmd$", f)], rmarkdown::render)


library("jsonld")
library("jsonlite")
library("magrittr")
library("testthat")

#context <- "codemeta.jsonld"
context <- "https://raw.githubusercontent.com/codemeta/codemeta/master/codemeta.jsonld"



## Round trip expansion and compaction should give us the same thing
validate <- function(example){
  jsonld_expand(example) %>%
  jsonld_compact(context) %>% 
  writeLines("test.json")
  
  ## Same properties in each
  A <- read_json(example) 
  B <- read_json("test.json") 

  unlink("test.json")
  
  ## drop context, we don't care if one is literal and one the URL of context, what matters is content
  A$`@context` <- NULL 
  B$`@context`  <- NULL 
  
  ## sort since order does not matter to JSON
  
  ## Same number of properties as we started with?
  same_number <- identical(
    A %>% unlist() %>% length(),
    B %>% unlist() %>% length())
  
  ## Did any properties fail to compact back?
  compaction_fail <-
  B %>% unlist() %>% names() %>% grepl(pattern = ":") %>% any()
  
  same_number && !compaction_fail
  
}

expect_true(validate("examples/codemeta.json"))
expect_true(validate("examples/schema-org-codemeta.json"))

expect_false(validate("examples/example-codemeta-invalid.json"))

## author isn't a list type, so doesn't compact
expect_false(validate("examples/example-code-jsonld.json"))             


## Verify we have subset the schema.org correctly, e.g we have the same behavior as a context of [codemeta.json, http://schema.org]

             