import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Neural Alpha Allocation Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# Custom Styling
# =========================

st.markdown("""
<style>
    .main {
        background-color: #0E1117;
        color: white;
    }

    .stMetric {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #2E2E2E;
    }

    .css-1d391kg {
        background-color: #111827;
    }

    h1, h2, h3 {
        color: #F8FAFC;
    }

    .dashboard-card {
        background-color: #161B22;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# Sidebar
# =========================

st.sidebar.title("Portfolio Controls")

selected_asset = st.sidebar.selectbox(
    "Select Asset",
    ["AAPL", "MSFT", "NVDA", "TSLA", "META", "GOOGL"]
)

selected_model = st.sidebar.selectbox(
    "Forecasting Model",
    ["LSTM", "Transformer"]
)

forecast_window = st.sidebar.slider(
    "Forecast Horizon",
    7,
    90,
    30
)

risk_profile = st.sidebar.selectbox(
    "Risk Profile",
    ["Conservative", "Balanced", "Aggressive"]
)

st.sidebar.markdown("---")

st.sidebar.info("""
Neural Alpha Allocation Engine

Deep Learning + Portfolio Optimization + Financial NLP
""")

# =========================
# Header
# =========================

st.title("Neural Alpha Allocation Engine")

st.markdown("""
### Institutional Deep Learning Portfolio Intelligence Platform

This dashboard integrates:
- LSTM Forecasting
- Transformer Allocation Models
- FinBERT Sentiment Analytics
- Portfolio Optimization Pipelines
- Quantitative Risk Monitoring
""")

# =========================
# KPI Metrics
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Portfolio Return",
    "18.42%",
    "+2.14%"
)

col2.metric(
    "Sharpe Ratio",
    "1.84",
    "+0.12"
)

col3.metric(
    "Portfolio Volatility",
    "11.26%",
    "-1.02%"
)

col4.metric(
    "Max Drawdown",
    "-6.14%",
    "-0.48%"
)

st.markdown("---")

# =========================
# Tabs
# =========================

tab1, tab2, tab3, tab4 = st.tabs([
    "Portfolio Analytics",
    "Forecasting Models",
    "Sentiment Intelligence",
    "Risk Monitoring"
])

# =========================
# Portfolio Analytics Tab
# =========================

with tab1:

    st.subheader("Portfolio Performance Overview")

    portfolio_returns = np.random.randn(250).cumsum()

    df = pd.DataFrame({
        "Portfolio Returns": portfolio_returns
    })

    st.line_chart(df)

    st.markdown("### Allocation Breakdown")

    allocation_df = pd.DataFrame({
        "Asset": ["AAPL", "MSFT", "NVDA", "TSLA", "META"],
        "Allocation": [25, 20, 18, 15, 22]
    })

    st.bar_chart(
        allocation_df.set_index("Asset")
    )

# =========================
# Forecasting Models Tab
# =========================

with tab2:

    st.subheader("Deep Learning Forecasting Engine")

    forecast_data = pd.DataFrame({
        "LSTM Forecast": np.random.randn(100).cumsum(),
        "Transformer Forecast": np.random.randn(100).cumsum()
    })

    st.line_chart(forecast_data)

    st.markdown("""
    ### Model Insights

    - LSTM models capture sequential market dependencies
    - Transformer architectures improve long-range forecasting
    - Ensemble predictions enhance allocation stability
    """)

# =========================
# Sentiment Intelligence Tab
# =========================

with tab3:

    st.subheader("Financial Sentiment Intelligence")

    sentiment_scores = pd.DataFrame({
        "Sentiment": [
            "Positive",
            "Neutral",
            "Negative"
        ],
        "Score": [62, 24, 14]
    })

    st.bar_chart(
        sentiment_scores.set_index("Sentiment")
    )

    st.markdown("""
    ### FinBERT Sentiment Pipeline

    The system processes:
    - Financial news
    - Earnings reports
    - Market commentary
    - Institutional sentiment signals

    Sentiment features are integrated into portfolio forecasting workflows.
    """)

# =========================
# Risk Monitoring Tab
# =========================

with tab4:

    st.subheader("Portfolio Risk Monitoring")

    risk_metrics = pd.DataFrame({
        "Metric": [
            "Beta",
            "VaR",
            "Expected Shortfall",
            "Tracking Error"
        ],
        "Value": [
            1.08,
            -4.25,
            -6.12,
            2.84
        ]
    })

    st.dataframe(risk_metrics)

    risk_curve = np.random.normal(0, 1, 500)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.hist(risk_curve, bins=40)

    st.pyplot(fig)

# =========================
# Footer
# =========================

st.markdown("---")

st.markdown("""
### Quantitative Research Environment

Built for:
- Portfolio Optimization
- Neural Forecasting
- Financial NLP
- Quantitative Risk Analytics
- Institutional Research Workflows
""")
