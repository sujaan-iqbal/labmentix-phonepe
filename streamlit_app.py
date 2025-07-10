import streamlit as st
import sqlite3
import pandas as pd
import os

# --- Connect to DB ---
DB_PATH = "phonepe.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# --- Streamlit UI ---
st.set_page_config(page_title="PhonePe Insights Dashboard", layout="wide")
st.title("📊 PhonePe Data Insights")
st.markdown("Explore transaction, user, and insurance data across states and time periods.")

# --- Sidebar Selection ---
query_files = {
    "Transaction Dynamics": "q1_transaction_dynamics.sql",
    "Device Dominance": "q2_device_dominance.sql",
    "Insurance Penetration": "q3_insurance_penetration.sql",
    "User Engagement": "q4_user_engagement.sql",
    "Top Transaction Regions": "q5_top_transaction_regions.sql"
}

selected_query = st.sidebar.selectbox("Choose Analysis", list(query_files.keys()))

# --- Run SQL Query ---
query_path = os.path.join("sql", "insights", query_files[selected_query])
try:
    with open(query_path, "r") as f:
        sql_query = f.read()
    df = pd.read_sql_query(sql_query, conn)

    st.subheader(f"Results: {selected_query}")
    st.dataframe(df)

    # --- Optional Visualizations ---
    st.markdown("---")
    if 'state' in df.columns and 'amount' in df.columns:
        st.bar_chart(df.set_index("state")["amount"])
    elif 'brand' in df.columns and 'app_opens' in df.columns:
        st.bar_chart(df.set_index("brand")["app_opens"])
    elif 'state' in df.columns and 'count' in df.columns:
        st.line_chart(df.set_index("state")["count"])

except Exception as e:
    st.error(f"Error: {str(e)}")
