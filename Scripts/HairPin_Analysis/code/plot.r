library(tidyverse)
library(ggthemes)

args = commandArgs(trailingOnly=TRUE)

input <- as.character(args[1])
output <- paste0(as.character(input), ".pdf")


df = read_csv(input,
              col_names = c("tag", "sps", "pos", "pos2", "nt")) %>% 
    mutate(sps=factor(sps, levels=c("gac", setdiff(unique(sps), "gac"))),
           nt=factor(nt, levels=c("a", "c", "g", "t","-"))) 

library(ggplot2)
df %>% filter(tag %in% c("nt", "nt-change")) %>%
    ggplot() +
    
    geom_segment(data=filter(df, tag %in% c("5p-pos", "3p-pos")), 
                 aes(pos, sps, xend=pos2, yend=sps), size=5, alpha=0.5) +
    geom_tile(aes(pos, sps, fill=nt), alpha=0.8) +
#     geom_text(aes(pos, sps,label=nt)) +
    geom_vline(data=filter(df, sps=="gac", tag %in% c("5p-pos", "3p-pos")) %>% 
                   gather(pos, value, -tag, -sps, -nt),
               aes(xintercept = value)) + 
    scale_fill_manual(values=c("#e34a33", "#2b8cbe", "#ffeda0", "#31a354","grey")) +
    theme_clean() 
ggsave(output, width=12)
