# RBI Policy Market Reaction Analysis

A Python-based analysis tool to study how RBI monetary policy decisions influence Indian bond yields and banking sector equities.

## Overview

This project analyzes the movement of:
- Indian 10-year Government Security (G-Sec) yields  
- Bank Nifty index  

around RBI monetary policy announcement dates using a simple event-window approach.

The goal is to understand how market expectations and policy communication translate into asset price movements, rather than to predict markets.

## What this project does

- Tracks 10Y G-Sec yield and Bank Nifty movements around RBI policy dates  
- Visualizes market reactions before and after policy announcements  
- Highlights expectation-driven behavior in financial markets  

## Project Structure

```text
rbi-policy-market-reaction/
├── README.md
├── requirements.txt
└── src/
    ├── main.py
    ├── market_data.py
    ├── policy_event.py
    └── visualizer.py
```

## How it works

- `MarketData` loads and stores financial time series data  
- `PolicyEventAnalyzer` extracts event windows around RBI policy dates  
- `MarketVisualizer` generates charts with policy date markers  
- `main.py` coordinates the full analysis flow  

Each component has a single responsibility to keep the analysis modular and easy to reason about.

## Usage

1. Place your CSV files in the project directory:
   - `gsec_10yr_data.csv`
   - `bank_nifty_data.csv`

2. Update policy dates and configuration in `src/main.py`

3. Run the analysis:
```bash
cd src
python main.py


