import pandas as pd


class PolicyEventAnalyzer:
    """Extracts event windows around RBI policy dates."""

    def __init__(self, market_data, policy_dates, window_days=5, labels=None):
        self.market_data = market_data
        self.policy_dates = policy_dates
        self.window_days = window_days
        self.labels = labels if labels else policy_dates

    def extract_window(self, data, policy_date):
        policy_date = pd.to_datetime(policy_date)

        if policy_date not in data.index:
            idx = data.index.get_indexer([policy_date], method='nearest')[0]
            policy_date = data.index[idx]

        policy_idx = data.index.get_loc(policy_date)
        start_idx = max(0, policy_idx - self.window_days)
        end_idx = min(len(data), policy_idx + self.window_days + 1)

        return data.iloc[start_idx:end_idx].copy(), policy_date

    def run_analysis(self, visualizer):
        for i, policy_date in enumerate(self.policy_dates):
            label = self.labels[i]

            gsec_window, actual_date = self.extract_window(
                self.market_data.gsec, policy_date
            )
            bank_window, _ = self.extract_window(
                self.market_data.bank_nifty, policy_date
            )

            visualizer.plot_gsec(gsec_window, actual_date, label)
            visualizer.plot_bank_nifty(bank_window, actual_date, label)
