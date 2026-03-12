import os
from pathlib import Path
from market_data import MarketData
from policy_event import PolicyEventAnalyzer
from visualizer import MarketVisualizer

# Dynamically resolve paths (assumes main.py is inside the src/ folder)
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'

GSEC_FILE = DATA_DIR / 'gsec_10yr_data.csv'
BANK_NIFTY_FILE = DATA_DIR / 'bank_nifty_data.csv'

# Configure your event study parameters
POLICY_DATES = [
    '2024-02-08',
    '2024-04-05',
    '2024-06-07'
]

LABELS = [
    'February 2024 Policy',
    'April 2024 Policy',
    'June 2024 Policy'
]

# ±5 trading days around the event
WINDOW_DAYS = 5 

def main():
    # Directory safety check
    if not DATA_DIR.exists():
        print(f"Creating data directory at: {DATA_DIR}")
        print("Please place 'gsec_10yr_data.csv' and 'bank_nifty_data.csv' inside it and run again.")
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        return

    try:
        print("Initializing Quantitative Event Study...")
        market_data = MarketData(GSEC_FILE, BANK_NIFTY_FILE)
        
        print("\n--- Pipeline Data Summary ---")
        market_data.print_summary()

        analyzer = PolicyEventAnalyzer(
            market_data=market_data,
            policy_dates=POLICY_DATES,
            window_days=WINDOW_DAYS,
            labels=LABELS
        )

        visualizer = MarketVisualizer()
        
        print("\nGenerating Event Window Charts...")
        analyzer.run_analysis(visualizer)
        print("Analysis Complete.")
        
    except FileNotFoundError as e:
        print(f"\n[ERROR] {e}")

if __name__ == "__main__":
    main()
