import streamlit as st
import pandas as pd
from agents.inventory_advisor_agent import InventoryAdvisorAgent

st.set_page_config(page_title="Inventory Advisor Agent")

st.title("📦 Inventory Advisor Agent")
st.write("Calculate **EOQ**, **Safety Stock**, and **Reorder Point** for any SKU.")

sku_id = st.text_input("SKU ID", "SKU001")
lead_time = st.number_input("Lead Time (days)", min_value=1, value=7)
ordering_cost = st.number_input("Ordering Cost per Order ($)", min_value=1, value=100)
holding_cost = st.number_input("Holding Cost per Unit per Year ($)", min_value=0.1, value=2.0)
z_score = st.number_input("Z-Score for Service Level", value=1.65)

if st.button("Calculate Inventory Plan"):
    forecast_df = pd.read_csv('data/sample_forecast.csv')
    historical_df = pd.read_csv('data/historical_sales.csv')

    agent = InventoryAdvisorAgent(
        forecast_df=forecast_df,
        historical_df=historical_df,
        sku_id=sku_id,
        lead_time_days=lead_time,
        ordering_cost=ordering_cost,
        holding_cost_per_unit_per_year=holding_cost,
        z_score=z_score
    )

    result = agent.generate_report()
    st.subheader("📊 Recommended Inventory Plan")
    st.json(result)
