from prophet import Prophet
import pandas as pd

class DemandForecastAgent:
    def __init__(self, data):
        self.data = data

    def train_and_forecast(self, product_id, store_id):
        df = self.data[
            (self.data['product_id'] == product_id) &
            (self.data['store_id'] == store_id)
        ][['date', 'sales']]
        df.rename(columns={'date': 'ds', 'sales': 'y'}, inplace=True)
        
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=30)
        forecast = model.predict(future)
        
        return forecast[['ds', 'yhat']]
