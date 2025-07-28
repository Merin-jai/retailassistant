import pandas as pd
from agents.demand_forecast_agent import DemandForecastAgent
from agents.inventory_advisor_agent import InventoryAdvisorAgent

# Load data
df = pd.read_csv('data/m5_forecasting.csv')

# Forecast
demand_agent = DemandForecastAgent(df)
forecast = demand_agent.train_and_forecast('PRODUCT123', 'STORE5')

# Inventory
inventory_agent = InventoryAdvisorAgent(forecast)
reorder_point = inventory_agent.calculate_reorder_point()

print(f"Recommended reorder point: {reorder_point}")