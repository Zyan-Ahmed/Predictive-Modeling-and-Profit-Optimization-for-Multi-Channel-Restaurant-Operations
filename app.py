import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Load data
df = pd.read_csv(r"C:\Users\admin\Downloads\SkyCity Auckland Restaurants & Bars.csv")

# Feature Engineering
df['TotalNetProfit'] = (
    df['InStoreNetProfit'] +
    df['UberEatsNetProfit'] +
    df['DoorDashNetProfit'] +
    df['SelfDeliveryNetProfit']
)

df['Commission_Impact'] = df['CommissionRate'] * df['UE_share']
df['DeliveryCost_Impact'] = df['DeliveryCostPerOrder'] * df['SD_share']

# Model Training
features = [
    'InStoreShare', 'UE_share', 'DD_share', 'SD_share',
    'CommissionRate', 'DeliveryCostPerOrder',
    'DeliveryRadiusKM', 'GrowthFactor',
    'Commission_Impact', 'DeliveryCost_Impact'
]

X = df[features]
y = df['TotalNetProfit']

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

# ---------------------------
# UI
# ---------------------------
st.title("🍽️ Restaurant Profit Optimization Dashboard")

st.sidebar.header("Adjust Inputs")

instore = st.sidebar.slider("InStore Share", 0.0, 1.0, 0.4)
ue = st.sidebar.slider("Uber Eats Share", 0.0, 1.0, 0.3)
dd = st.sidebar.slider("DoorDash Share", 0.0, 1.0, 0.2)
sd = st.sidebar.slider("Self Delivery Share", 0.0, 1.0, 0.1)

commission = st.sidebar.slider("Commission Rate", 0.0, 0.5, 0.25)
delivery_cost = st.sidebar.slider("Delivery Cost per Order", 0.5, 6.0, 2.5)
radius = st.sidebar.slider("Delivery Radius (KM)", 1, 20, 8)
growth = st.sidebar.slider("Growth Factor", 0.9, 1.1, 1.02)

# Feature creation
commission_impact = commission * ue
delivery_impact = delivery_cost * sd

input_data = pd.DataFrame([[
    instore, ue, dd, sd,
    commission, delivery_cost,
    radius, growth,
    commission_impact, delivery_impact
]], columns=features)

# Prediction
prediction = model.predict(input_data)[0]

# ---------------------------
# Output
# ---------------------------
st.subheader("📊 Predicted Net Profit")
st.success(f"${prediction:,.2f}")

# ---------------------------
# Sensitivity Analysis
# ---------------------------
st.subheader("📈 Sensitivity Analysis (UE Share)")

ue_range = np.linspace(0, 1, 20)
profits = []

for val in ue_range:
    temp = input_data.copy()
    temp['UE_share'] = val
    temp['Commission_Impact'] = val * commission
    profits.append(model.predict(temp)[0])

st.line_chart(pd.DataFrame({
    "UE Share": ue_range,
    "Profit": profits
}).set_index("UE Share"))

# ---------------------------
# Optimization Insight
# ---------------------------
st.subheader("💡 Recommendation")

if sd > ue:
    st.info("Higher self-delivery improves margins but watch logistics cost.")
elif ue > sd:
    st.warning("High aggregator reliance may reduce margins due to commission.")
else:
    st.success("Balanced channel mix detected.")