#!/usr/bin/env R

source("http://bioconductor.org/biocLite.R")

list.of.packages <- c("sva", "bladderbatch")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) biocLite(new.packages)

library("bladderbatch")
library("sva")

options(stringsAsFactors=FALSE)
data(bladderdata)

pheno = pData(bladderEset)
# add fake age variable for numeric
pheno$age = c(1:7, rep(1:10, 5))
write.table(data.frame(cel=rownames(pheno), pheno), row.names=F, quote=F, sep=",", file="bladder-pheno.csv")

edata = exprs(bladderEset)
write.table(edata, row.names=T, quote=F, sep=",", file="bladder-expr.csv")
# use dataframe instead of matrix
mod = model.matrix(~as.factor(cancer) + age, data=pheno)
t = Sys.time()
cdata = ComBat(dat=edata, batch=as.factor(pheno$batch), mod=mod)
print(Sys.time() - t)
print(cdata[1:5, 1:5])

write.table(cdata, "r-batch.csv", sep=",", quote=F)
