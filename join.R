library("dplyr")
library("readr")

A <- read_csv("group_a_crosswalk.csv")
B <- read_csv("group_b_crosswalk.csv")
C <- read_csv("group_c_crosswalk.csv")
D <- read_csv("crosswalk-OntoSoft.csv")

A <- A %>% select(Concept, `Concept Definition`, Zenodo, `Software Ontology`, GitHub, `Use Cases`)
B <- B %>% select(-Zenodo, -`Software Ontology`, -github, -`Software Ontology`, -DataCite)
C <- C %>% select(Concept, `Concept Definition`, `Use Cases`, DataCite)
D <- D %>% select(Concept, `Concept Definition`, OntoSoft)

A %>%  
  full_join(B, by = "Concept") %>% 
  full_join(C, by = "Concept") %>% 
  full_join(D, by = "Concept") -> crosswalk

write_csv(crosswalk, "join.csv")
