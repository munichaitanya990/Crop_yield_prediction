import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
data = pd.read_csv("backend/data/sample_crop_data.csv")

# ----- Yield Prediction Model -----
X_yield = data[["N", "P", "K", "pH"]]
y_yield = data["Yield"]

yield_model = RandomForestRegressor()
yield_model.fit(X_yield, y_yield)
joblib.dump(yield_model, "backend/yield_model.joblib")

# ----- Price Prediction Model -----
X_price = data[["N", "P", "K", "pH"]]
y_price = data["Price"]

price_model = RandomForestRegressor()
price_model.fit(X_price, y_price)
joblib.dump(price_model, "backend/price_model.joblib")

print("✅ Models trained and saved successfully!")
