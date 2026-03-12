import pandas as pd
from pathlib import Path

class MarketData:
    """Handles loading, sanitization, and storage of financial time series data."""

    def __init__(self, gsec_file: Path, bank_nifty_file: Path):
        self.gsec = self._load_data(gsec_file, 'yield')
        self.bank_nifty = self._load_data(bank_nifty_file, 'close')

    def _load_data(self, filepath: Path, column_name: str) -> pd.DataFrame:
        if not filepath.exists():
            raise FileNotFoundError(f"Missing required data file: {filepath}")
        
        # Parse dates robustly and force DatetimeIndex
        df = pd.read_csv(filepath, parse_dates=[0], index_col=0)
        df.index = pd.to_datetime(df.index)
        
        # Standardize column naming and drop empty rows
        df.columns = [column_name]
        df.index.name = 'date'
        
        # Sort chronologically to ensure rolling windows extract correctly
        return df.dropna().sort_index()

    def print_summary(self):
        print(f"G-Sec records loaded: {len(self.gsec)}")
        print(f"Bank Nifty records loaded: {len(self.bank_nifty)}")
