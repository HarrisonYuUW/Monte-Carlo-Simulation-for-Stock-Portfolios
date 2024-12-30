# Monte-Carlo-Simulation-for-Stock-Portfolios
A Monte Carlo simulation-based tool to forecast and visualize potential future values of a stock portfolio, based on historical data of given stocks and random sampling of returns.

This forecaster uses Monte Carlo simulation to predict the future value of a stock portfolio based on historical data retrieved from Yahoo Finance. It models potential portfolio outcomes over a specified time frame by incorporating historical mean returns, asset covariance, random sampling, and also includes inflation adjustment (for the future only). To put it simply Monte Carlo simulations use random sampling to model uncertain systems and estimate possible outcomes. Instead of predicting a singular outcome, it generates many (often 1000+) potential outcomes by repeatedly simulating the system with different random variables. This model incorporates this method by using historical financial data and their percent changes to estimate what may happen in the future. A graph is then produced of every possible outcome and an average (mean) is displayed. This graph can be interpreted in any way you might like. This version has a customizable cutoff so you can narrow down your data range to calculate the mean.

**Example:**
![Xnip2024-12-30_18-07-12](https://github.com/user-attachments/assets/54d374a1-f81d-4f40-8457-73ee2660f036)

Stocks invested: ['NVDA', 'AAPL', 'TSLA', 'GOOG', 'RY.TO', 'TD.TO', 'CM.TO', 'BNS.TO', 'BMO.TO'] ($10,000 initial investment)

Inflation rate: 0.03

Historical data: Up to 4 years prior to 12/30/2024

Number of simulations: 500

Forecasted: 1 year (365 days)

Weightings: [0.2205134  0.05153788 0.21790635 0.13933028 0.04126821 0.12320218 0.12336882 0.05958874 0.02328414] respectively
