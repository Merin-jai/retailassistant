import pandas as pd
import numpy as np

class InventoryAdvisorAgent:
    def __init__(self, forecast_df, historical_df, sku_id, lead_time_days=7, ordering_cost=100, holding_cost_per_unit_per_year=2.0, z_score=1.65):
        self.forecast_df = forecast_df
        self.historical_df = historical_df
        self.sku_id = sku_id
        self.lead_time_days = lead_time_days
        self.ordering_cost = ordering_cost
        self.holding_cost_per_unit_per_year = holding_cost_per_unit_per_year
        self.z_score = z_score

    def average_daily_demand(self):
        return self.forecast_df['yhat'].mean()

    def std_dev_demand(self):
        sku_sales = self.historical_df[self.historical_df['sku_id'] == self.sku_id]
        return sku_sales['units_sold'].std()

    def annual_demand(self):
        return self.average_daily_demand() * 365

    def calculate_eoq(self):
        D = self.annual_demand()
        S = self.ordering_cost
        H = self.holding_cost_per_unit_per_year
        eoq = np.sqrt((2 * D * S) / H)
        return eoq

    def calculate_safety_stock(self):
        sigma = self.std_dev_demand()
        ss = self.z_score * sigma * np.sqrt(self.lead_time_days)
        return ss

    def calculate_reorder_point(self):
        avg_daily = self.average_daily_demand()
        ss = self.calculate_safety_stock()
        rop = (avg_daily * self.lead_time_days) + ss
        return rop

    def generate_report(self):
        return {
            "SKU_ID": self.sku_id,
            "EOQ": round(self.calculate_eoq(), 2),
            "ReorderPoint": round(self.calculate_reorder_point(), 2),
            "SafetyStock": round(self.calculate_safety_stock(), 2)
        }
