library(readr)
bank_trans_cd <- read_csv("D:/ML/Hackathon/bank_trans.csv")
adm_data_cd <- as.data.frame(bank_trans_cd)

#install.packages("rpart")
library(rpart)
tree <- rpart(FRAUD_FLAG ~ adm_data$TXN_CREDIT_CNT + adm_data$SAL + adm_data$TXN_TYPE, data=adm_data, method="class")
plot(tree)
text(tree, pretty = 0)

#

#install.packages("rattle")
library(rattle)
#install.packages("RColorBrewer")
library(RColorBrewer)
#install.packages("rpart.plot")
library(rpart.plot)

fancyRpartPlot(tree)

printcp(dtree)
ptree<- prune(tree, cp=tree$cptable[which.min(tree$cptable[,"xerror"]), "CP"])
fancyRpartPlot(ptree, uniform=TRUE, main="Pruned Classification Tree")
plotcp(tree)

#install.packages("party")

#install.packages("partykit")
library(partykit)
dtree2 <-ctree(FRAUD_FLAG ~ TXN_CREDIT_CNT + SAL + TXN_TYPE, data=adm_data)
plot(dtree2)

