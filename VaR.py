
import numpy as np
import pandas as pd
import yfinance as yf
from tabulate import tabulate

import matplotlib.pyplot as plt
import seaborn
import matplotlib.mlab as mlab

# Calculate the daily returns and plot
df = ？  ## Get from lstm
df = df[['Close']]
df['returns'] = df.Close.pct_change()
df = df.dropna()
plt.hist(df.returns, bins=40)
plt.xlabel('Returns')
plt.ylable('Frequency')
plt.grid(True)
plt.show()

# Sort the returns
df.sort_values('returns', inplace = True, ascending =  True)

# Calculate the VaR for 90%, 95%, and 99% confidence levels using quantile function
VaR_90 = df['returns'].quantile(0.1)
VaR_95 = df['returns'].quantile(0.05)
VaR_99 = df['returns'].quantile(0.09)
print (tabulate([['90%', VaR_90], ['95%', VaR_95], ['99%', VaR_99]], headers = ['Confidence Level', 'Value at Risk']))
