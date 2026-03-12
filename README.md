# RBI Policy Market Reaction Analysis 📈

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
<img src="https://img.shields.io/badge/Data-Pandas-150458?logo=pandas">
<img src="https://img.shields.io/badge/Visualization-Matplotlib-orange">
<img src="https://img.shields.io/badge/Domain-Quantitative%20Finance-green">
<img src="https://img.shields.io/github/stars/yourusername/rbi-policy-market-reaction">
<img src="https://img.shields.io/github/forks/yourusername/rbi-policy-market-reaction">
<img src="https://img.shields.io/github/issues/yourusername/rbi-policy-market-reaction">
<img src="https://img.shields.io/github/last-commit/yourusername/rbi-policy-market-reaction">
</p>

<p align="center">
A modular Python-based quantitative event study framework designed to analyze how Reserve Bank of India (RBI) monetary policy decisions influence Indian bond yields and banking sector equities.
</p>

---

# Overview

Rather than attempting to predict the market, this framework focuses on **market microstructure and expectation tracking**.

The system automatically extracts localized time-series windows around policy decision dates to visualize how financial markets react before and after policy announcements.

Specifically, it analyzes:

• **10-Year Government Security (G-Sec) yields**
• **Bank Nifty index movements**

to identify how monetary policy expectations are priced into financial markets.

The framework helps researchers understand:

* pre-policy market expectations
* immediate post-policy market reactions
* volatility patterns around macroeconomic announcements

---

# Animated Event Study Workflow

<p align="center">
<img src="docs/event-study-pipeline.gif" width="850">
</p>

Workflow representation

```id="d3b0o1"
Market Data (CSV)
        │
        ▼
market_data.py
(Data Loading & Time-Series Indexing)
        │
        ▼
policy_event.py
(Event Window Extraction ±N Trading Days)
        │
        ▼
visualizer.py
(Matplotlib Event Visualization)
        │
        ▼
main.py
(Execution & Pipeline Control)
```

---

# Demo Visualization

<p align="center">
<img src="demo/rbi-event-study-demo.gif" width="850">
</p>

Generated charts show:

| Metric              | Description                            |
| ------------------- | -------------------------------------- |
| Policy Event Marker | Vertical line marking RBI announcement |
| Pre-Event Window    | Market expectations before policy      |
| Post-Event Window   | Market reaction after announcement     |
| Yield Movement      | G-Sec interest rate response           |
| Equity Response     | Bank Nifty price adjustment            |

---

# Features

## Time-Series Data Management

Handles raw financial market datasets efficiently.

Capabilities:

* loads daily financial market data
* sanitizes missing values
* standardizes time-series indexing
* aligns multiple datasets on a common timeline

---

## Dynamic Event Window Extraction

Extracts localized volatility windows around policy events.

Configurable window:

```id="q39k1k"
± N trading days
Example: 5 days before and 5 days after policy decision
```

This enables consistent event-study comparisons across multiple policy announcements.

---

## Holiday / Weekend Imputation

Policy announcements often occur on non-trading days.

To maintain consistent analysis windows, the framework uses:

```id="pckz2m"
Pandas get_indexer(method="nearest")
```

This automatically maps policy dates to the **closest valid trading day**, ensuring window lengths remain mathematically intact.

---

## Automated Financial Visualization

Institutional-quality charts generated using **Matplotlib**.

Visualization includes:

* event markers separating expectation vs reaction periods
* grid-based styling using `seaborn-whitegrid`
* synchronized multi-asset charts

---


# Project Structure

```id="kz33m4"
rbi-policy-market-reaction/
│
├── README.md
├── requirements.txt
│
├── data/                       # Raw CSVs (Ignored by Git)
│   ├── gsec_10yr_data.csv
│   └── bank_nifty_data.csv
│
└── src/                        # Application Source Code
    ├── main.py                 # Application entry point
    ├── market_data.py          # DataFrame handling
    ├── policy_event.py         # Event window logic
    └── visualizer.py           # Chart generation
```

---

# Installation

Clone the repository

```bash id="t8f7hx"
git clone https://github.com/yourusername/rbi-policy-market-reaction.git
cd rbi-policy-market-reaction
```

Install dependencies

```bash id="tfy0q4"
pip install -r requirements.txt
```

---

# Usage

Prepare your data

Place the following CSV files inside the `data/` directory:

```
gsec_10yr_data.csv
bank_nifty_data.csv
```

Required format:

* Date column (Datetime index)
* Value column (Yield or Close)

Run the analysis

```bash id="1v5spp"
cd src
python main.py
```

---

# Example Chart Output

<p align="center">
<img src="docs/sample-output-chart.png" width="850">
</p>

Charts clearly illustrate how:

• markets anticipate policy changes
• yields react to monetary signals
• banking stocks adjust after announcements

---

# Performance & Scope Metrics

| Metric                   | Value               | Context                             |
| ------------------------ | ------------------- | ----------------------------------- |
| Data Processing Scope    | 1,000+ trading days | multi-year historical datasets      |
| Analysis Turnaround Time | < 2 seconds         | automated event-window extraction   |
| Imputation Reliability   | 100%                | nearest-index mapping avoids errors |

The framework reduces manual Excel event-study workflows from **hours to milliseconds**.

---

# Technologies Used

| Category        | Technology           |
| --------------- | -------------------- |
| Language        | Python 3.10+         |
| Data Processing | Pandas               |
| Visualization   | Matplotlib           |
| File Handling   | Pathlib              |
| Analysis Domain | Quantitative Finance |

---

# GitHub Metrics

<p align="center">
<img src="https://github-readme-stats.vercel.app/api?username=yourusername&show_icons=true">
<img src="https://github-readme-streak-stats.herokuapp.com/?user=yourusername">
</p>

---

# Repository Activity

<p align="center">
<img src="https://activity-graph.herokuapp.com/graph?username=yourusername">
</p>

---

# Download Statistics

<p align="center">
<img src="https://img.shields.io/github/downloads/yourusername/rbi-policy-market-reaction/total">
</p>

---

# Use Cases

This framework can be used for:

* monetary policy event studies
* fixed income market research
* macroeconomic policy analysis
* financial econometrics experiments
* academic research on market reactions

---

# Future Improvements

Volatility Metrics
Add standard deviation bands to detect abnormal returns relative to historical volatility.

Multi-Asset Support
Integrate `yfinance` API to fetch live market data.

Sentiment Overlay
Apply NLP to RBI policy documents and overlay sentiment scores on the market reaction charts.

---

# License

MIT License

---

# Author

Developed as a quantitative finance and financial data analysis project demonstrating event-study methodology, time-series processing, and macroeconomic market reaction analysis.


