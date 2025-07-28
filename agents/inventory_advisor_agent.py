import pandas as pd

class InventoryAdvisorAgent:
    def __init__(self, forecast_df):
        self.forecast_df = forecast_df

    def calculate_average_daily_demand(self):
        return self.forecast_df['yhat'].mean()

    def calculate_safety_stock(self, service_factor=1.65, std_dev=5, lead_time=7):
        # service_factor 1.65 = 95% service level
        return service_factor * std_dev * (lead_time ** 0.5)

    def calculate_reorder_point(self, lead_time=7):
        avg_daily = self.calculate_average_daily_demand()
        safety_stock = self.calculate_safety_stock(lead_time=lead_time)
        reorder_point = avg_daily * lead_time + safety_stock
        return reorder_point
