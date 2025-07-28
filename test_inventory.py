import pandas as pd
from agents.inventory_advisor_agent import InventoryAdvisorAgent

# Load mock data
forecast_df = pd.read_csv('data/sample_forecast.csv')
historical_df = pd.read_csv('data/historical_sales.csv')

# Create agent
agent = InventoryAdvisorAgent(
    forecast_df=forecast_df,
    historical_df=historical_df,
    sku_id='SKU001',
    lead_time_days=7,
    ordering_cost=100,
    holding_cost_per_unit_per_year=2.0,
    z_score=1.65
)

result = agent.generate_report()
print(result)
