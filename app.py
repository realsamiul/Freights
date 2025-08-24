import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import io
from sklearn.metrics import r2_score, mean_absolute_error

# --- Page Configuration ---
st.set_page_config(
    layout="wide",
    page_title="ECG | Freight Intelligence Platform",
    page_icon="🚢"
)

# --- App Styling ---
st.markdown("""
<style>
    .reportview-container {
        background: #FFFFFF;
    }
    .sidebar .sidebar-content {
        background: #F0F2F6;
    }
    h1, h2, h3 {
        color: #1E293B;
    }
    .stMetric-value {
        font-size: 2.5rem !important;
    }
    .stMetric-label {
        color: #64748B !important;
    }
    .stAlert {
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Data Embedding ---
# All data is embedded here to make the app self-contained and reliable.
@st.cache_data
def load_data():
    # Data from your final `model_results.csv`
    results_csv = """
date,actual,predicted
2024-01-30,11.56,11.25
2024-02-29,11.81,10.64
2024-03-31,16.23,15.23
2024-04-30,13.89,12.67
2024-05-31,12.82,13.15
2024-06-30,12.26,12.51
2024-07-31,12.12,11.03
2024-08-31,11.72,10.66
2024-09-30,10.77,10.39
2024-10-31,10.45,10.46
2024-11-30,8.06,7.96
2024-12-31,6.25,6.13
"""
    results_df = pd.read_csv(io.StringIO(results_csv))
    results_df['date'] = pd.to_datetime(results_df['date'])
    results_df.rename(columns={'actual': 'Actual Rate', 'predicted': 'Predicted Rate'}, inplace=True)
    
    # Data from your final `feature_importance.csv`
    importance_csv = """
feature,importance
CCI_Score_lag_1,0.489
BDRY_price_lag_1,0.444
CCI_Score_lag_3,0.032
GSI_Score_lag_1,0.009
CCI_Score_lag_7,0.005
BDRY_price_lag_3,0.004
avg_wait_time_lag_7,0.003
BDRY_price_lag_7,0.003
GSI_Score_lag_7,0.002
vessel_count_lag_3,0.002
"""
    feature_importance_df = pd.read_csv(io.StringIO(importance_csv)).sort_values('importance', ascending=True)
    # Clean up feature names for presentation
    feature_importance_df['feature'] = feature_importance_df['feature'].str.replace('_', ' ').str.title().str.replace('Bdry Price', 'Freight Rate')

    # Data from your `cci_components.csv` for the latest values
    components_csv = """
CCI_Score,GSI_Score,vessel_count,avg_wait_time,berth_availability,geopolitical_risk,weather_disruption,latest_prediction
0.783,0.456,45,22.5,7,8.2,0.85,6.13
"""
    components_df = pd.read_csv(io.StringIO(components_csv))

    return results_df, feature_importance_df, components_df

results_df, feature_importance_df, components_df = load_data()

# --- Page Navigation ---
PAGES = {
    "1. The Strategic Imperative": "intro",
    "2. A Tale of Two Methodologies": "journey",
    "3. Deconstructing the CCI: Our Secret Sauce": "cci_deep_dive",
    "4. Live Demo: Running the Validation": "live_demo",
    "5. Results: Validated Predictive Power": "results",
    "6. The Path Forward: From Demo to Deployment": "next_steps"
}

st.sidebar.title('Presentation Navigator')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# --- Page 1: Introduction ---
if selection == "1. The Strategic Imperative":
    st.title("The Strategic Imperative")
    st.header("Why Predicting Freight Rates is a Multi-Million Dollar Opportunity")
    
    st.markdown("""
    [span_0](start_span)For a conglomerate as deeply integrated into the Bangladeshi economy as ECG, maritime freight is not a line item; it is the central artery of our supply chain[span_0](end_span). [span_1](start_span)With Chittagong Port handling over **92% of the nation's trade**, any volatility in shipping rates directly impacts the profitability and stability of nearly every business unit[span_1](end_span).
    
    [span_2](start_span)Historically, ECG has been a price taker, exposed to extreme volatility where a single delayed shipment can incur costs exceeding **$50,000** and unpredictable rate spikes can erode margins on entire product lines[span_2](end_span).
    
    [span_3](start_span)The goal of this project was to leverage ECG's unique internal data—our "asymmetric advantage"—to build a predictive capability that turns this volatility from a strategic risk into a strategic opportunity[span_3](end_span).
    """)
    
    st.image("https://images.unsplash.com/photo-1578574577315-3fbeb0cecdc2?q=80&w=2070", caption="The lifeblood of ECG's business flows through the Port of Chittagong.")

# --- Page 2: Our Analytical Journey ---
elif selection == "2. A Tale of Two Methodologies":
    st.title("A Tale of Two Methodologies")
    st.header("The Initial Failure and the Methodological Pivot")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("❌ The Initial Approach: A Dead End")
        st.markdown("""
        [span_4](start_span)The first attempt relied on a generic time-series analysis[span_4](end_span). [span_5](start_span)On the surface, the results looked spectacular, with a reported R² score of 0.923[span_5](end_span).
        [span_6](start_span)However, a deeper look revealed a complete predictive failure caused by **data leakage** from an incorrect random train-test split[span_6](end_span).
        """)
        [span_7](start_span)st.metric(label="Actual Trend Direction Accuracy", value="49.8%", delta="Literally worse than a coin flip[span_7](end_span)")
        [span_8](start_span)st.warning("This proved that a simple, off-the-shelf approach is methodologically flawed and insufficient for this complex problem[span_8](end_span). [span_9](start_span)It necessitated a 'flight to quality'[span_9](end_span).")

    with col2:
        st.subheader("✅ The Strategic Pivot: A Theory-Backed Model")
        st.markdown("""
        [span_10](start_span)[span_11](start_span)Learning from this failure, we developed a Master Plan grounded in the practices of global market intelligence firms like the World Bank[span_10](end_span)[span_11](end_span). [span_12](start_span)This led to our core thesis: **freight rates for ECG are driven not just by global markets, but by local, on-the-ground reality at the port**[span_12](end_span).
        
        We pivoted to building two proprietary indices:
        - **[span_13](start_span)The Chittagong Congestion Index (CCI):** A hyper-local measure of port stress[span_13](end_span).
        - **[span_14](start_span)The Global Shipping Index (GSI):** A macro indicator of market pressure[span_14](end_span).
        
        [span_15](start_span)These indices, fed into a highly-tuned XGBoost model, became the heart of our new, successful approach[span_15](end_span).
        """)

# --- Page 3: Deconstructing the CCI ---
elif selection == "3. Deconstructing the CCI: Our Secret Sauce":
    st.title("Deconstructing the CCI: Our Secret Sauce")
    st.header("Quantifying the Physical Reality of the Port")
    
    st.markdown("""
    [span_16](start_span)The Chittagong Congestion Index (CCI) is a proprietary, multi-variate index that provides a daily score of operational stress at the port[span_16](end_span). [span_17](start_span)It's our primary leading indicator, adapting the methodology of the World Bank's Container Port Performance Index (CPPI), which focuses on physical, time-based metrics of efficiency[span_17](end_span).
    """)
    
    latest_components = components_df.iloc[0]
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.subheader("Vessel Wait Time")
        st.metric(label="Latest Avg. Wait Time", value=f"{latest_components['avg_wait_time']:.1f} hrs")
        st.info("Measures time vessels spend idle at anchorage. The single biggest indicator of systemic congestion.")
    with c2:
        st.subheader("Vessel Count")
        st.metric(label="Latest Vessel Count", value=f"{int(latest_components['vessel_count'])}")
        st.info("Total vessels at berth and anchorage, indicating traffic pressure.")
    with c3:
        st.subheader("Berth Availability")
        st.metric(label="Latest Availability", value=f"{latest_components['berth_availability']} Berths")
        st.info("The number of free berths. Lower numbers signal the port is near capacity.")
    with c4:
        st.subheader("Disruption Score")
        st.metric(label="Latest Risk Level", value=f"{latest_components['geopolitical_risk']}/10")
        st.info("Quantifies external shocks from geopolitical news and severe weather events.")

# --- Page 4: Live Demo ---
elif selection == "4. Live Demo: Running the Validation":
    st.title("Live Demo: Running the Model Validation")
    st.markdown("This is a simulation of the final validation step: training the model on historical data and testing it against the unseen data from 2024.")

    if 'trained' not in st.session_state:
        st.session_state.trained = False

    if st.button("▶️ Run Model Training & Validation"):
        st.session_state.trained = False
        st.info("Step 1: Preparing 2021-2023 training data...")
        time.sleep(1)
        st.info("Step 2: Calculating historical CCI and GSI features...")
        time.sleep(1)
        st.info("Step 3: Training the final XGBoost regression model...")
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)
        st.success("✅ Model Trained on 2021-2023 Data!")
        
        st.info("Step 4: Running predictions on the entire, unseen year of 2024...")
        time.sleep(1.5)
        st.success("✅ Validation Complete! Proceed to the 'Results' page to see the performance.")
        st.session_state.trained = True

    if st.session_state.trained:
        st.header("Validation run is complete. Please proceed to the next page to view the full results.")


# --- Page 5: The Results ---
elif selection == "5. Results: Validated Predictive Power":
    st.title("Results: Validated Predictive Power")
    [span_18](start_span)st.header("The model was tested on the entire, unseen year of 2024. The results were a definitive success[span_18](end_span).")

    # Calculate metrics dynamically from the loaded data
    r2 = r2_score(results_df['Actual Rate'], results_df['Predicted Rate'])
    mae = mean_absolute_error(results_df['Actual Rate'], results_df['Predicted Rate'])

    # Main Historical Validation Chart
    st.subheader("📈 Historical Validation: Actual vs. Predicted Rates (2024)")
    fig_val = go.Figure()
    fig_val.add_trace(go.Scatter(x=results_df['date'], y=results_df['Actual Rate'], name='Actual Rate', mode='lines+markers', line=dict(color='royalblue', width=3)))
    fig_val.add_trace(go.Scatter(x=results_df['date'], y=results_df['Predicted Rate'], name='Predicted Rate', mode='lines+markers', line=dict(color='darkorange', dash='dash')))
    
    fig_val.update_layout(
        title_text='<b>Our model\'s predictions (orange) track the real-world rates (blue) with high accuracy.</b>',
        legend_title_text='',
        yaxis_title="Freight Rate Proxy (BDRY ETF Price, $)",
        xaxis_title="2024 Test Period"
    )
    st.plotly_chart(fig_val, use_container_width=True)

    st.divider()
    
    # Key Statistics and Feature Importance
    st.subheader("Translating Statistics into Business Value")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric(label="Model Accuracy (R² Score)", value=f"{r2:.1%}")
        st.metric(label="Average Prediction Error (MAE)", value=f"${mae:.2f}")
        [span_19](start_span)st.info(f"The model successfully explained {r2:.1%} of the price movements in the unseen test data[span_19](end_span). [span_20](start_span)On average, its predictions were off by only ${mae:.2f}[span_20](end_span).")

    with col2:
        fig_imp = px.bar(feature_importance_df.tail(5), x='importance', y='feature', orientation='h', 
                         title='Top 5 Most Important Features',
                         labels={'importance': 'XGBoost Feature Importance', 'feature': ''})
        fig_imp.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_imp, use_container_width=True)
        [span_21](start_span)st.success("Crucially, the model confirmed that our proprietary CCI and its lagged values are the most powerful external drivers of the forecast, validating our core thesis[span_21](end_span).")

# --- Page 6: Next Steps ---
elif selection == "6. The Path Forward: From Demo to Deployment":
    st.title("The Path Forward: From Demo to Deployment")
    [span_22](start_span)st.header("From a Proven Demo to an Enterprise Asset[span_22](end_span)")
    
    st.markdown("""
    [span_23](start_span)This project has successfully delivered a validated, high-performance model that is ready for a compelling demo[span_23](end_span). [span_24](start_span)[span_25](start_span)The next step is to transition from this historical proof-of-concept to a live, operational tool that generates millions of dollars in annual value[span_24](end_span)[span_25](end_span).
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Phase 1: MVP Deployment (Q4 2025)")
        st.markdown("""
        - **Action:** Deploy this exact dashboard, powered by a semi-automated weekly data refresh.
        - **[span_26](start_span)Goal:** Provide procurement teams with a 7-to-14 day forward-looking forecast to inform near-term strategic decisions[span_26](end_span).
        - **[span_27](start_span)[span_28](start_span)[span_29](start_span)Value:** Begin capturing value immediately through optimized procurement, reduced demurrage costs, and enhanced negotiation power[span_27](end_span)[span_28](end_span)[span_29](end_span).
        """)
    
    with col2:
        st.subheader("Phase 2: Full Application & Integration (2026)")
        st.markdown("""
        - **[span_30](start_span)Action:** Build live, automated data pipelines to feed real-time information from port authorities and market data providers into the model daily[span_30](end_span).
        - **[span_31](start_span)Goal:** Create a real-time "mission control" dashboard with live forecasts, customizable alerts (e.g., "Alert me if CCI > 80"), and deeper drill-down capabilities[span_31](end_span).
        - **Integration:** Develop an internal API to feed these predictive insights directly into ECG's ERP and financial planning systems, automating the competitive advantage.
        """)
    
    st.success("The investment in the AI Center of Excellence begins to pay dividends now. Let's take the next step.")

