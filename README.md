# 🍽️ Predictive Modeling and Profit Optimization for Multi-Channel Restaurant Operations

## 📌 Project Overview

This project focuses on building a **predictive and prescriptive analytics system** for restaurant businesses operating across multiple sales channels such as:

* In-store dining
* Uber Eats
* DoorDash
* Self-delivery

The goal is to help restaurant operators **simulate scenarios, predict profits, and optimize channel mix decisions** using data-driven insights.

---

## 🎯 Problem Statement

Restaurant operators often struggle with:

* High commission fees from delivery aggregators
* Lack of visibility into profit sensitivity
* Inability to test “what-if” scenarios before making decisions

This project solves these challenges by developing:

* Predictive models for profit estimation
* Scenario simulation engine
* Optimization recommendations

---

## 📊 Dataset Description

The dataset contains operational and financial data for restaurant branches, including:

* Revenue and orders by channel
* Cost structures (COGS, OPEX, delivery cost)
* Commission rates
* Delivery radius and growth factors
* Channel share distribution

---

## ⚙️ Key Features

### 🔹 Exploratory Data Analysis (EDA)

* Profit distribution analysis
* Channel performance comparison
* Correlation heatmaps
* Segment-level insights

### 🔹 Feature Engineering

* Profit per order
* Channel revenue ratios
* Interaction features:

  * CommissionRate × UE_share
  * DeliveryCostOrder × SD_share

### 🔹 Predictive Modeling

Models implemented:

* Linear Regression (baseline)
* Random Forest Regressor

Evaluation metrics:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Square Error)
* R² Score

---

## 📈 Scenario Simulation Engine

Allows testing of strategic decisions such as:

* Increasing/decreasing aggregator share
* Changing commission rates
* Expanding delivery radius
* Adjusting self-delivery investment

---

## 🧠 Optimization Insights

The system provides recommendations for:

* Profit-maximizing channel mix
* Safe commission rate thresholds
* Self-delivery feasibility

---

## 🖥️ Streamlit Dashboard

### Features:

* Interactive sliders for:

  * Channel mix
  * Commission rate
  * Delivery cost
  * Growth factor
* Real-time profit prediction
* Sensitivity analysis charts
* Strategy recommendations

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/restaurant-profit-optimization.git
cd restaurant-profit-optimization
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── data/
│   └── SkyCity Auckland Restaurants & Bars.csv
├── notebooks/
│   └── eda_analysis.ipynb
├── app.py
├── requirements.txt
└── README.md
```

---

## 📌 Key KPIs

* Predicted Net Profit
* Profit Sensitivity Index
* Channel Mix Efficiency
* Break-even Commission Rate
* Optimization Uplift (%)

---

## 📊 Example Use Cases

* Decide optimal channel mix
* Evaluate commission negotiations
* Plan self-delivery expansion
* Forecast profit under growth scenarios

---

## 🔮 Future Improvements

* XGBoost / Gradient Boosting models
* Hyperparameter tuning
* Advanced optimization (linear programming)
* Deployment on cloud platforms

---

## 🤝 Contributors

* Your Name

---

## 📄 License

This project is for educational and analytical purposes.

---

## ⭐ Acknowledgment

This project demonstrates how **data science can transform restaurant operations from reactive reporting to proactive decision-making**.
