from market_data import MarketData
from policy_event import PolicyEventAnalyzer
from visualizer import MarketVisualizer


GSEC_FILE = 'gsec_10yr_data.csv'
BANK_NIFTY_FILE = 'bank_nifty_data.csv'

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

WINDOW_DAYS = 5


def main():
    market_data = MarketData(GSEC_FILE, BANK_NIFTY_FILE)
    market_data.print_summary()

    analyzer = PolicyEventAnalyzer(
        market_data=market_data,
        policy_dates=POLICY_DATES,
        window_days=WINDOW_DAYS,
        labels=LABELS
    )

    visualizer = MarketVisualizer()
    analyzer.run_analysis(visualizer)


if __name__ == "__main__":
    main()
