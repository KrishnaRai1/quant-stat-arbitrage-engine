# Quantitative Statistical Arbitrage Engine

A professional quantitative trading and statistical arbitrage research framework focused on mean-reversion strategies, spread analysis, portfolio analytics, and risk-adjusted backtesting.

This project implements statistical arbitrage methodologies using z-score based signal generation, rolling spread calculations, portfolio risk management, and interactive visualization tools for financial market research.

---

# Overview

The Quantitative Statistical Arbitrage Engine is designed to simulate and evaluate market-neutral trading strategies using statistical relationships between correlated assets.

The framework includes:

- Statistical arbitrage and pairs trading workflows
- Mean-reversion signal generation
- Rolling z-score analysis
- Portfolio analytics and risk evaluation
- Historical market data processing
- Interactive dashboard visualization
- Research-oriented notebook experimentation

The repository is structured to resemble a modular quantitative research environment commonly used in systematic trading and hedge fund workflows.

---

# Features

## Statistical Arbitrage Strategies
- Mean-reversion trading models
- Spread-based trading signals
- Rolling z-score calculations
- Pair selection workflows
- Cointegration-focused research utilities

## Portfolio Analytics
- Sharpe Ratio analysis
- Annualized return calculations
- Drawdown monitoring
- Volatility analytics
- Risk-adjusted performance metrics

## Risk Management
- Stop-loss management
- Portfolio exposure monitoring
- Capital allocation utilities
- Portfolio turnover analytics
- Risk threshold configuration

## Data Processing
- Historical market data ingestion
- Equity dataset management
- CSV-based research workflows
- Quantitative preprocessing utilities

## Visualization
- Equity curve plotting
- Cumulative return visualization
- Portfolio analytics charts
- Rolling spread visualization
- Dashboard-based monitoring

## Interactive Dashboard
- Streamlit trading dashboard
- Strategy parameter controls
- Portfolio analytics overview
- Interactive visualization panels

---

# Project Structure

```bash
quant-stat-arbitrage-engine/
│
├── analytics/              # Performance and risk analytics modules
├── dashboard/              # Streamlit dashboard application
├── datasets/               # Historical datasets and trading outputs
├── market_data/            # Historical equity market data
├── notebooks/              # Research and experimentation notebooks
├── risk_management/        # Portfolio risk management utilities
├── visualization/          # Visualization and charting tools
├── reports/                # Quantitative research notes
├── configs/                # Configuration and parameter settings
├── requirements.txt        # Python dependencies
└── README.md
```

---

# Technologies Used

## Core Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels
- Streamlit

## Quantitative Finance Concepts
- Statistical Arbitrage
- Pairs Trading
- Mean Reversion
- Z-Score Analysis
- Cointegration Research
- Portfolio Optimization
- Risk Management

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/quant-stat-arbitrage-engine.git

cd quant-stat-arbitrage-engine
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

## Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

## Open Research Notebook

```bash
jupyter notebook
```

Navigate to:

```bash
notebooks/statistical_arbitrage_research.ipynb
```

---

# Example Workflow

1. Load historical equity data
2. Generate spread between correlated assets
3. Calculate rolling z-score
4. Generate trading signals
5. Backtest strategy performance
6. Evaluate portfolio analytics
7. Visualize cumulative returns and equity curves

---

# Research Objectives

This project focuses on:
- Quantitative strategy research
- Statistical market inefficiency analysis
- Market-neutral portfolio construction
- Risk-adjusted return optimization
- Backtesting infrastructure development

---

# Future Improvements

- Live market data integration
- Automated trade execution simulation
- Bayesian parameter optimization
- Multi-asset portfolio support
- Advanced risk factor modeling
- Machine learning signal generation
- Real-time dashboard analytics

---

# Disclaimer

This repository is intended for educational and research purposes only.

It does not constitute financial advice, investment recommendations, or production-ready trading infrastructure.

Trading financial markets involves substantial risk.

---

# Author

Krishna Rai

GitHub:
https://github.com/KrishnaRai1
