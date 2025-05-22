load("C:/Users/inyt1/Desktop/assignment1/pima.RData")

factor <- cut(
  pima$bmi,
  breaks = c(-Inf, 25, 40, Inf),
  labels = c("low", "normal", "high"),
  right = TRUE
)

aggregate(diabetes ~ factor,data=pima, FUN=mean)

model <- lm(diabetes ~ factor, data = pima)

anova(model)


