# データの読み込み
internet_data <- read.csv("internet.csv")

# データの構造を確認
str(internet_data)

# インターネット利用率が最も高い国
max_int_country <- internet_data[which.max(internet_data$Int), ]
print(paste("インターネット利用率が最も高い国:", max_int_country$Country, "(", max_int_country$Int, "%)"))

# インターネット利用率が最も低い国
min_int_country <- internet_data[which.min(internet_data$Int), ]
print(paste("インターネット利用率が最も低い国:", min_int_country$Country, "(", min_int_country$Int, "%)"))

# インターネット利用率の平均
mean_int <- mean(internet_data$Int)
print(paste("インターネット利用率の平均:", round(mean_int, 2), "%"))

# インターネット利用率の平均値に近い国
closest_int_country <- internet_data[which.min(abs(internet_data$Int - mean_int)), ]
print(paste("インターネット利用率が最も平均値に近い国:", closest_int_country$Country, "(", closest_int_country$Int, "%)"))

# 散布図の作成
plot(internet_data$Gdp, internet_data$Int,
     xlab = "GDP per Capita (in $1000s)", 
     ylab = "Internet Users as % of Population", 
     main = "Relationship between GDP per Capita and Internet Usage", 
     pch = 16, col = "blue")

# 単回帰分析の実行
model <- lm(Int ~ Gdp, data = internet_data)

# モデルのサマリーを表示
summary(model)

# 決定係数を取得
r_squared <- summary(model)$r.squared
print(paste("IntのばらつきがGdpによって説明される割合 (R-squared):", round(r_squared * 100, 2), "%"))

# 予測用の新しいデータフレームを作成
new_gdp_data <- data.frame(Gdp = 20)

# 予測を実行
predicted_int <- predict(model, newdata = new_gdp_data)
print(paste("一人当たりGDPが20,000米ドルの場合、インターネット利用者の割合予測:", round(predicted_int, 2), "%"))

# 残差の計算
residuals <- residuals(model)

# 負の残差が最も大きい国（最も負の値が大きい国）
most_negative_residual_country <- internet_data[which.min(residuals), ]
print(paste("負の残差が最も大きい国:", most_negative_residual_country$Country, "(残差:", round(min(residuals), 2), ")"))

# 正の残差が最も大きい国
most_positive_residual_country <- internet_data[which.max(residuals), ]
print(paste("正の残差が最も大きい国:", most_positive_residual_country$Country, "(残差:", round(max(residuals), 2), ")"))

# 予測値の計算
predicted_values <- predict(model)

# 残差と予測値の散布図
plot(predicted_values, residuals,
     xlab = "Predicted Internet Usage (%)", 
     ylab = "Residuals",
     main = "Residuals vs. Predicted Values",
     pch = 16, col = "red")
abline(h = 0, col = "blue", lty = 2) 