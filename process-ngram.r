
headers <- c("freq", "pre", "post", "pre-pos", "post-pos")


ngrams <- read.csv("./coca-ngrams/w2c.txt", sep="\t", header=FALSE, col.names=headers)

head(ngrams, 1)