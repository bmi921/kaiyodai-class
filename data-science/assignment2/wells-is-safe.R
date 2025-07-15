setwd("/Users/inyt113/Desktop/dev/kaiodai-class/data-science/assignment4")

wells <- read.csv("wells.csv")
head(wells)

# 1.距離のみ
wells1 <- glm(switch ~ dist,family = binomial(link = "logit"),data = wells)
summary(wells1)
exp(coef(wells1))

# 2.距離とヒ素
wells2 <- glm(switch ~ dist + arsenic,family = binomial(link = "logit"),data = wells)
summary(wells2)
exp(coef(wells2))

# 3.全てで解析、教育効果について検証
wells3 <- glm(switch ~ dist + arsenic + assoc + educ,family = binomial(link = "logit"),data = wells)
summary(wells3)
exp(coef(wells3))

median_dist <- median(wells$dist)
median_arsenic <- median(wells$arsenic)

educ_values <- c(0, 4, 8, 12, 16)
newdata <- data.frame(
  educ = educ_values,
  dist = rep(median_dist, length(educ_values)),
  assoc = 1,
  arsenic = rep(median_arsenic, length(educ_values))
)
prob <- predict(wells3, newdata = newdata, type = "response")　# responseは確率として返す
results <- data.frame(
  educ = educ_values,
  prob= prob
)
results

# 交互作用項を追加
wells4 <- glm(switch ~ dist + arsenic + assoc + educ + arsenic * educ,family = binomial(link = "logit"),data = wells)
summary(wells4)
exp(coef(wells4))