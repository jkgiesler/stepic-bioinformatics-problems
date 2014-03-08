map <- read.table("~/Dropbox/Life/code/Python/Python for git/Bioinformatics/Mismatch Kmer Analysis/Development/output.dat", quote="\"")
var =map[[1]]
jpeg('plot.jpg')
plot(var)
dev.off()