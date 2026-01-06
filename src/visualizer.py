import matplotlib.pyplot as plt


class MarketVisualizer:
    """Creates charts with RBI policy date markers."""

    def plot_gsec(self, data, policy_date, title):
        self._plot(
            data=data,
            column='yield',
            policy_date=policy_date,
            title=f'10-Year G-Sec Yield\n{title}',
            ylabel='Yield (%)',
            color='#2E86AB'
        )

    def plot_bank_nifty(self, data, policy_date, title):
        self._plot(
            data=data,
            column='close',
            policy_date=policy_date,
            title=f'Bank Nifty Index\n{title}',
            ylabel='Index Value',
            color='#A23B72'
        )

    def _plot(self, data, column, policy_date, title, ylabel, color):
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data[column], marker='o', color=color)

        if policy_date in data.index:
            plt.axvline(policy_date, color='red', linestyle='--', label='RBI Policy Date')

        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel(ylabel)
        plt.legend()
        plt.grid(alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
