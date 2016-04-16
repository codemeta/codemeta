library("dplyr")
library("readr")

A <- read_csv("group_a_crosswalk.csv")
B <- read_csv("group_b_crosswalk.csv")
C <- read_csv("group_c_crosswalk.csv")

C <- C %>% select(Concept, `Concept Definition`, `Use Cases`, DataCite)
B <- B %>% select(-Zenodo, -`Software Ontology`, -github, -`Software Ontology`, -DataCite)
A <- A %>% select(Concept, `Concept Definition`, Zenodo, `Software Ontology`, GitHub, `Use Cases`)

A %>%  full_join(B, by = "Concept") %>% full_join(C, by = "Concept") -> ABC

write_csv(ABC, "join.csv")
