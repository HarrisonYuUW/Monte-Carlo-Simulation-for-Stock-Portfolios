"""
author: Harrison Yu
date: 12/25/2024
desc: monte carlo simulation
"I can calculate the motion of heavenly bodies, but not the madness of people" - Sir Isaac Newton.
"""

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# Retrieving data from yfinance and performing necessary calculation
def import_data(stocklst, start_date, end_date):
    stock_data = yf.download(stocklst, start=start_date, end=end_date)['Close']
    returns = stock_data.pct_change()  # Calculate percentage change
    mean_returns = returns.mean()  # Mean of returns
    covariance_matrix = returns.cov()  # Covariance matrix
    print(returns)
    return mean_returns, covariance_matrix

# List of stocks we are investing in
# Suffix for each stock can be found at https://help.yahoo.com/kb/SLN2310.html 
stocklst = ['NVDA', 'AAPL', 'TSLA', 'GOOG', 'RY.TO', 'TD.TO', 'CM.TO', 'BNS.TO', 'BMO.TO']

# Defining the historical timeframe desired
end_date = dt.datetime.now()
start_date = end_date - dt.timedelta(days=1460) # Last 4 years

mean_returns, covariance_matrix = import_data(stocklst, start_date, end_date)
print(mean_returns, covariance_matrix)

# Creating random weights from 0 - 1 and ensuring total weight sum = 1
weights = np.random.random(len(mean_returns))
weights /= np.sum(weights)
# weights = [x,y,z...] can be replaced to create your own weightings.
print(f'Weightings: {weights}')

# Monte carlo implementation
n = 500 # Number of simulations
t = 365 # Future timeframe in days
initial_investment = 10000
inflation_rate = 0.03

mean_matrix = np.full(shape=(t, len(weights)), fill_value = mean_returns)
mean_matrix = mean_matrix.T
portfolio_matrix = np.full(shape=(t, n), fill_value=0.0)
for m in range(0, n):
    z = np.random.normal(size=(t, len(weights)))
    l = np.linalg.cholesky(covariance_matrix)
    daily_returns = mean_matrix + np.inner(l, z)
    portfolio_matrix[:,m] = np.cumprod(np.inner(weights, daily_returns.T) + 1) * initial_investment
    portfolio_matrix[:,m] = portfolio_matrix[:, m] / (1 + inflation_rate) ** (np.arange(t) / 365)

#Set values for graph
mean_value = np.mean(portfolio_matrix, axis=1)
final_portfolio_values = portfolio_matrix[-1, :] # Collect all values at end of simulation
min_value = np.min(final_portfolio_values) 
max_value = np.max(final_portfolio_values) 

# Create cutoffs for calculations
lower_percentile = np.percentile(final_portfolio_values, 0)
upper_percentile = np.percentile(final_portfolio_values, 100)
filtered_values = final_portfolio_values[(final_portfolio_values >= lower_percentile) & (final_portfolio_values <= upper_percentile)]
filtered_min_value = np.min(filtered_values)
filtered_max_value = np.max(filtered_values)
filtered_mean_value = np.mean(filtered_values)

#Plot graph
plt.xlim(0, t)
plt.plot(portfolio_matrix, color='blue', alpha=0.05)
plt.plot(mean_value, color='orange', label=f'Mean Portfolio Value: ${filtered_mean_value:,.2f}', linewidth=1, alpha=1)
plt.axhline(y=filtered_max_value, color='grey', linestyle='--', label=f'Max Portfolio Value: ${filtered_max_value:,.2f}', alpha=0.8, linewidth=1)
plt.axhline(y=filtered_min_value, color='grey', linestyle='--', label=f'Min Portfolio Value: ${filtered_min_value:,.2f}', alpha=0.8, linewidth=1)
plt.legend(fontsize=7)
plt.ylabel('Portfolio Value ($)')
plt.xlabel('Number of Days')
plt.title('Monte Carlo Simulation of Stock Portfolio')
plt.show()