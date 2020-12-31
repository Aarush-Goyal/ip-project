# imports
import colorama
from colorama import Fore, Back, Style
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web

colorama.init(autoreset=True)

# menu - welcome
print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
      "\n             Welcome to stock market analyser         ")
print("\n You can enter stock tickers and get the Daily Percentage Change and other statitical data like MEAN, CORRELATION and COVARIANCE for the stocks that you will enter \nfor eg: FB NFLX AMZN \n")
# menu -tickers
options = input("Enter the tickers : ")

print("...loading stock data")

tickers = options.split(" ")
# Getting Data from Yahoo finance
multpl_stocks = web.get_data_yahoo(tickers,
                                   start="2020-01-01",
                                   end="2020-12-31")

print(Fore.WHITE + Back.BLUE + Style.BRIGHT + "\n\n ---- STOCK DATA ---- \n")
print(multpl_stocks)

# Plotting the Adjusted Close for every stock

for ticker in tickers:
    fig = plt.figure()
    fig.set_size_inches(8.5, 5.5)
    ax = fig.add_subplot()
    ax.plot(multpl_stocks['Adj Close'][ticker])
    ax.set_title(ticker)
    plt.tight_layout()
    figure_image_name = ticker + ".png"
    plt.savefig(figure_image_name)
    plt.show()

multpl_stock_daily_returns = multpl_stocks['Adj Close'].pct_change()
multpl_stock_monthly_returns = multpl_stocks['Adj Close'].resample(
    'M').ffill().pct_change()

# Plotting the Monthly Returns

fig = plt.figure()
fig.set_size_inches(8.5, 5.5)
(multpl_stock_monthly_returns + 1).cumprod().plot()
plt.savefig("monthlyReturns.png")
plt.show()

print(Fore.WHITE + Back.BLUE + Style.BRIGHT + '\n\n ---- Mean ---- \n')
print(multpl_stock_monthly_returns.mean())
print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
      '\n\n ---- Standard Deviation ---- \n')
print(multpl_stock_monthly_returns.std())
print(Fore.WHITE + Back.BLUE + Style.BRIGHT + '\n\n ---- Correlation ---- \n')
print(multpl_stock_monthly_returns.corr())
print(Fore.WHITE + Back.BLUE + Style.BRIGHT + '\n\n ---- Covariance ---- \n')
print(multpl_stock_monthly_returns.cov())

print(" \nThe Images has been stored in the working directory.")
print(Fore.WHITE + Back.BLUE + Style.BRIGHT + "\nHave a nice day :)")
print("\n")
