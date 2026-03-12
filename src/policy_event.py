import pandas as pd
from typing import List, Tuple

class PolicyEventAnalyzer:
    """Extracts exact trading-day event windows around RBI policy dates."""

    def __init__(self, market_data, policy_dates: List[str], window_days: int = 5, labels: List[str] = None):
        self.market_data = market_data
        self.policy_dates = [pd.to_datetime(date) for date in policy_dates]
        self.window_days = window_days
        self.labels = labels if labels else policy_dates

    def extract_window(self, data: pd.DataFrame, policy_date: pd.Timestamp) -> Tuple[pd.DataFrame, pd.Timestamp]:
        # Nearest-Neighbor Imputation: Finds the closest trading day if policy falls on a weekend/holiday
        if policy_date not in data.index:
            idx = data.index.get_indexer([policy_date], method='nearest')[0]
            actual_date = data.index[idx]
        else:
            actual_date = policy_date

        policy_idx = data.index.get_loc(actual_date)
        
        # Integer-based slicing guarantees we get exactly N trading days, 
        # ignoring calendar gaps like weekends.
        start_idx = max(0, policy_idx - self.window_days)
        end_idx = min(len(data), policy_idx + self.window_days + 1)

        return data.iloc[start_idx:end_idx].copy(), actual_date

    def run_analysis(self, visualizer):
        for i, policy_date in enumerate(self.policy_dates):
            label = self.labels[i]

            gsec_window, actual_gsec_date = self.extract_window(self.market_data.gsec, policy_date)
            bank_window, actual_bank_date = self.extract_window(self.market_data.bank_nifty, policy_date)

            visualizer.plot_gsec(gsec_window, actual_gsec_date, label)
            visualizer.plot_bank_nifty(bank_window, actual_bank_date, label)
