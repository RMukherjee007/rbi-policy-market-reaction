import matplotlib.pyplot as plt
import pandas as pd

class MarketVisualizer:
    """Generates publication-ready charts with RBI policy date markers."""

    def plot_gsec(self, data: pd.DataFrame, policy_date: pd.Timestamp, title: str):
        self._plot(
            data=data,
            column='yield',
            policy_date=policy_date,
            title=f'10-Year G-Sec Yield Reaction\n({title})',
            ylabel='Yield (%)',
            color='#2E86AB'  # Professional Blue
        )

    def plot_bank_nifty(self, data: pd.DataFrame, policy_date: pd.Timestamp, title: str):
        self._plot(
            data=data,
            column='close',
            policy_date=policy_date,
            title=f'Bank Nifty Index Reaction\n({title})',
            ylabel='Index Value',
            color='#A23B72'  # Professional Burgundy
        )

    def _plot(self, data: pd.DataFrame, column: str, policy_date: pd.Timestamp, title: str, ylabel: str, color: str):
        # Apply a clean, institutional charting style
        plt.style.use('seaborn-v0_8-whitegrid')
        fig, ax = plt.subplots(figsize=(10, 5))
        
        ax.plot(data.index, data[column], marker='o', color=color, linewidth=2, markersize=6)

        # Draw the critical event marker
        if policy_date in data.index:
            ax.axvline(policy_date, color='#D62828', linestyle='--', linewidth=2, label='RBI Policy Date')

        ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
        ax.set_xlabel('Trading Date', fontsize=11)
        ax.set_ylabel(ylabel, fontsize=11)
        
        fig.autofmt_xdate(rotation=45)
        ax.legend(frameon=True, facecolor='white', edgecolor='gray')
        plt.tight_layout()
        plt.show()
