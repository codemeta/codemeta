library("dplyr")
library("readr")


## See: https://t.co/DZP2GQ6f83 for a better alternative
## Function to strip ascii characters
find_non_ascii <- function(string){
  grep("I_WAS_NOT_ASCII", 
       iconv(string, "latin1", "ASCII", sub="I_WAS_NOT_ASCII"))
  
}
replace_non_ascii <-function(string){
  i <- find_non_ascii(string)
  non_ascii <- "áéíóúÁÉÍÓÚñÑüÜ’åôö"
  ascii <- "aeiouAEIOUnNuU'aoo"
  translated <- sapply(string[i], function(x) 
    chartr(non_ascii, ascii, x))
  string[i] <- unname(translated)
  string
}


## This is much more comprehensive and offers improved mapping, but is _very slow_
#devtools::install_github('rich-iannone/UnidecodeR')
library("UnidecodeR")


use_ascii <- function(df){
  for(i in 1:length(df)){
    df[[i]] <- replace_non_ascii(df[[i]])
    #df[[i]] <- unidecode(df[[i]], "all")
  }
  df
}



A <- read_csv("group_a_crosswalk.csv", col_types = paste0(rep("c", 16), collapse=""))
B <- read_csv("group_b_crosswalk.csv", col_types = paste0(rep("c", 23), collapse=""))
C <- read_csv("group_c_crosswalk.csv", col_types = paste0(rep("c", 17), collapse=""))
D <- read_csv("crosswalk-OntoSoft.csv", col_types = paste0(rep("c", 15), collapse=""))
E <- read_csv("kyle-neil-join.csv") %>% select(Concept, `Concept Definition`)


A <- A %>% select(Concept, Zenodo, `Software Ontology`, GitHub, `Use Cases`)
B <- B %>% select(-`Concept Definition`, -Zenodo, -`Software Ontology`, -github, -`Software Ontology`, -DataCite, -OntoSoft)
C <- C %>% select(Concept, `Use Cases`, `Software Entities Model (DataCitei/JISC)`) %>% rename(`Software Entities Model (DataCitei/JISC)` = "DataCite")
D <- D %>% select(Concept, OntoSoft)


A %>%  
  full_join(B, by = "Concept") %>% 
  full_join(C, by = "Concept") %>% 
  full_join(D, by = "Concept") %>% 
  full_join(E,by = "Concept") -> crosswalk

fillna <- function(df){
  for(i in 1:length(df)){
    df[[i]][is.na(df[[i]])] <- "-"
  }
  df
}

crosswalk <- fillna(crosswalk)
## Fill NA
## Remove non-ascii

crosswalk <- select(crosswalk, 
`Concept`,
  `Concept Definition`,
  `DataCite`,                                 
  `OntoSoft`,
  `Zenodo`,
  `GitHub`,
 `Figshare`,
 `Software Ontology`,
 `code.jsonld`,                              
 `Software Discovery Index`,                
 `Dublin Core`,                             
 `R Package Description`,                    
 `Debian Package Metadata`,                 
 `Python Distutils (PyPI)`,                  
 `Trove Software Map`,                      
 `Perl Module Description (CPAN::Meta)`,     
 `JavaScript package descption (npm)`,
 `Java (Maven)`,                             
 `Octave`,                                  
 `Ruby Gem`,                                 
 `CodeMeta Field`,                           
 `Use Cases`,                               
 `Use Cases.x`,                              
 `Use Cases.y`)
write_csv(crosswalk, "crosswalk.csv")


