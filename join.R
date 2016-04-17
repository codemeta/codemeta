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

A <- A %>% select(Concept, `Concept Definition`, Zenodo, `Software Ontology`, GitHub, `Use Cases`)
B <- B %>% select(-Zenodo, -`Software Ontology`, -github, -`Software Ontology`, -DataCite, -OntoSoft)
C <- C %>% select(Concept, `Concept Definition`, `Use Cases`, `Software Entities Model (DataCitei/JISC)`) %>% rename("DataCite" = `Software Entities Model (DataCitei/JISC)`)
D <- D %>% select(Concept, `Concept Definition`, OntoSoft)


A %>%  
  full_join(B, by = "Concept") %>% 
  full_join(C, by = "Concept") %>% 
  full_join(D, by = "Concept") -> crosswalk

is.na(crosswalk) <- "-"


## Fill NA
## Remove non-ascii

write_csv(crosswalk, "crosswalk.csv")
