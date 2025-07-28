import pandas as pd
from agents.inventory_advisor_agent import InventoryAdvisorAgent

# Load mock forecast
df = pd.read_csv('data/sample_forecast.csv')

# Create agent
agent = InventoryAdvisorAgent(df)

# Calculate
avg_demand = agent.calculate_average_daily_demand()
safety_stock = agent.calculate_safety_stock()
reorder_point = agent.calculate_reorder_point()

print(f"Average Daily Demand: {avg_demand}")
print(f"Safety Stock: {safety_stock}")
print(f"Reorder Point: {reorder_point}")
