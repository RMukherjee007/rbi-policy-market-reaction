import pandas as pd


class MarketData:
    """Handles loading and storage of financial time series data."""

    def __init__(self, gsec_file, bank_nifty_file):
        self.gsec = self._load_data(gsec_file, 'yield')
        self.bank_nifty = self._load_data(bank_nifty_file, 'close')

    def _load_data(self, filepath, column_name):
        df = pd.read_csv(filepath, parse_dates=[0], index_col=0)
        df.columns = [column_name]
        df.index.name = 'date'
        return df.sort_index()

    def print_summary(self):
        print(f"G-Sec records: {len(self.gsec)}")
        print(f"Bank Nifty records: {len(self.bank_nifty)}")
