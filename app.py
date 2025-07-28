# app.py
import streamlit as st
from orchestrator import reorder_point

st.title("AI Supply Chain Optimization Assistant")

st.write(f"Recommended Reorder Point: {reorder_point}")
