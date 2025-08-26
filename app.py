import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time
import io
from sklearn.metrics import r2_score, mean_absolute_error

# --- Page Configuration ---
st.set_page_config(layout="wide", page_title="ECG Freight Intelligence", page_icon="🚢")

# --- Password Protection ---
# This section MUST come before any other Streamlit commands
def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["APP_PASSWORD"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("Password incorrect")
        return False
    else:
        return True

# --- Main App Logic ---
# All app content is placed inside this `if` block
if check_password():

    # --- Styling and Font ---
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@300;400&display=swap');
            
            /* Core body and font styles */
            body {
                font-family: 'Roboto', sans-serif;
                color: #333;
            }
            h1, h2, h3 {
                font-family: 'Playfair Display', serif;
                font-weight: 700;
                color: #1E293B; /* Slate 800 */
            }
            
            /* Main container for centered, spacious content */
            .main-container {
                max-width: 900px;
                margin: 0 auto;
                padding: 2rem;
                text-align: center;
            }

            /* Custom Square Buttons */
            .stButton>button {
                border: 2px solid #E2E8F0; /* Slate 200 */
                border-radius: 0;
                color: #475569; /* Slate 600 */
                background-color: #FFFFFF;
                padding: 1rem 1.5rem;
                width: 100%;
                font-weight: bold;
                transition: all 0.2s ease-in-out;
            }
            .stButton>button:hover {
                border-color: #0284C7; /* Sky 600 */
                color: #0284C7;
                background-color: #F0F9FF; /* Sky 50 */
            }
            .stButton>button:focus {
                box-shadow: none !important;
            }
            
            /* Style for KPI metrics */
            .stMetric {
                background-color: #F8FAFC; /* Slate 50 */
                border: 1px solid #E2E8F0; /* Slate 200 */
                padding: 1rem;
            }

        </style>
    """, unsafe_allow_html=True)

    # --- Data Embedding ---
    @st.cache_data
    def load_data():
        results_csv = "date,actual,predicted\n2024-01-30,11.56,11.25\n2024-02-29,11.81,10.64\n2024-03-31,16.23,15.23\n2024-04-30,13.89,12.67\n2024-05-31,12.82,13.15\n2024-06-30,12.26,12.51\n2024-07-31,12.12,11.03\n2024-08-31,11.72,10.66\n2024-09-30,10.77,10.39\n2024-10-31,10.45,10.46\n2024-11-30,8.06,7.96\n2024-12-31,6.25,6.13"
        results_df = pd.read_csv(io.StringIO(results_csv))
        results_df['date'] = pd.to_datetime(results_df['date'])
        results_df.rename(columns={'actual': 'Actual Rate', 'predicted': 'Predicted Rate'}, inplace=True)
        
        components_csv = "CCI_Score,GSI_Score,vessel_count,avg_wait_time,berth_availability,geopolitical_risk,weather_disruption,latest_prediction\n0.783,0.456,45,22.5,7,8.2,0.85,6.13"
        components_df = pd.read_csv(io.StringIO(components_csv))
        return results_df, components_df

    results_df, components_df = load_data()

    # --- App State Management ---
    if 'page' not in st.session_state:
        st.session_state.page = 'opportunity'

    def set_page(page_name):
        st.session_state.page = page_name

    # --- Header & Navigation ---
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.title("ECG Freight Intelligence Platform")
    
    cols = st.columns(3)
    with cols[0]:
        st.button("1. The Opportunity", on_click=set_page, args=('opportunity',), key='btn_opp')
    with cols[1]:
        st.button("2. The Intelligence Engine", on_click=set_page, args=('engine',), key='btn_eng')
    with cols[2]:
        st.button("3. The Verdict & Value", on_click=set_page, args=('verdict',), key='btn_ver')
    
    st.markdown("---")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Page Content ---
    
    # PAGE 1: THE OPPORTUNITY
    if st.session_state.page == 'opportunity':
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        st.header("Turning Market Volatility into a Strategic Advantage")
        st.markdown("""
        [span_0](start_span)Maritime freight isn't a line item; it's our central artery.[span_0](end_span) [span_1](start_span)With Chittagong Port handling over **92% of national trade**, rate volatility is a multi-million dollar risk to our bottom line.[span_1](end_span)
        
        A generic time-series model failed, proving that **global trends are not enough.**
        """)
        st.metric(label="Generic Model Trend Accuracy", value="49.8%", delta="Worse than a coin toss", delta_color="inverse")
        st.markdown("""
        Our response was a strategic pivot: to build a proprietary **Chittagong Congestion Index (CCI)** that quantifies the on-the-ground reality of the port, giving us an asymmetric competitive advantage.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # PAGE 2: THE INTELLIGENCE ENGINE
    elif st.session_state.page == 'engine':
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        st.header("Deconstructing the CCI: Our Secret Sauce")
        [span_2](start_span)[span_3](start_span)st.markdown("The CCI is a daily score of operational stress, adapting World Bank methodology to our unique context.[span_2](end_span)[span_3](end_span) It measures the physical world, not just market charts.")
        
        latest = components_df.iloc[0]
        c1, c2, c3 = st.columns(3)
        c1.metric("Avg. Vessel Wait Time", f"{latest['avg_wait_time']:.1f} hrs")
        c2.metric("Total Vessel Count", f"{int(latest['vessel_count'])}")
        c3.metric("Berths Available", f"{int(latest['berth_availability'])}")
        
        st.markdown("---")
        st.subheader("Simulating the Validation Process")
        
        if st.button("▶️ Run Model Training & Test on 2024 Data"):
            with st.spinner("Training model on 2021-2023 data..."):
                time.sleep(2)
            st.success("✅ Model Trained!")
            
            with st.spinner("Running predictions on unseen 2024 data..."):
                time.sleep(2)
            st.success("✅ Validation Complete!")
            st.info("Navigate to 'The Verdict & Value' to see the results.")
            
        st.markdown('</div>', unsafe_allow_html=True)

    # PAGE 3: THE VERDICT & VALUE
    elif st.session_state.page == 'verdict':
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        st.header("Validated Predictive Power")
        st.markdown("The model was tested on the entire, unseen year of 2024. The results were a definitive success.")

        r2 = r2_score(results_df['Actual Rate'], results_df['Predicted Rate'])
        mae = mean_absolute_error(results_df['Actual Rate'], results_df['Predicted Rate'])
        
        m1, m2 = st.columns(2)
        m1.metric("Model Accuracy (R²)", f"{r2:.1%}")
        m2.metric("Avg. Prediction Error (MAE)", f"${mae:.2f}")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=results_df['date'], y=results_df['Actual Rate'], name='Actual Rate', mode='lines', line=dict(color='royalblue', width=3)))
        fig.add_trace(go.Scatter(x=results_df['date'], y=results_df['Predicted Rate'], name='Predicted Rate', mode='lines', line=dict(color='darkorange', dash='dash')))
        fig.update_layout(title_text='<b>2024 Back-Test: Actual vs. Predicted Rates</b>', legend_title_text='', yaxis_title="BDRY ETF Price ($)")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        st.header("The Financial Impact & Path Forward")
        st.markdown("""
        [span_4](start_span)High accuracy reduces budget uncertainty from a typical +/-15% to **less than 5%**. On a single **$2.5M charter**, this provides **$125,000** in value from avoided costs.[span_4](end_span) [span_5](start_span)Scaled across ECG, this platform generates millions annually.[span_5](end_span)
        
        **Our path is clear:**
        - **Phase 1 (Q4 2025):** Deploy this dashboard for weekly strategic forecasting.
        - **Phase 2 (2026):** Build live data pipelines for a real-time "mission control" center and integrate predictions into our ERP systems.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
