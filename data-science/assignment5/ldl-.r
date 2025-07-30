library(ggplot2)
data <- read.csv("heart.csv")
summary(data)
str(data)

# ロジスティック回帰モデルの構築
model <- glm(target ~ chol , data = data, family = binomial(link = "logit"))
summary(model)

# オッズ比の計算 (オプション)
# LDLコレステロールが1単位増加したときの死亡率（心臓病発生率）のオッズ比
exp(coef(model))
exp(confint(model))

# 視覚化 (オプション: LDLコレステロールと死亡率の関係をプロット)
ggplot(data, aes(x = chol, y = target)) +
geom_point(position = position_jitter(height = 0.05), alpha = 0.5) +
   stat_smooth(method = "glm", method.args = list(family = "binomial"), se = FALSE) +
   labs(title = "relation", x = "LDL chol", y = "target") +
   theme_minimal()