# imports
import colorama
from colorama import Fore, Back, Style
import matplotlib.pyplot as plt
import pandas_datareader as web

colorama.init(autoreset=True)


print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
      "\n             Welcome to stock market analyser         ")
print("\n You can enter stock tickers and get the Daily Percentage Change and other statitical data like MEAN, CORRELATION and COVARIANCE for the stocks that you will enter \nfor eg: FB NFLX AMZN \n")


run_program = True

ticker_options = input(
    " \n Enter the stock ticker for which you would like to fetch the data for : ")
print("...loading stock data")

tickers = ticker_options.split(" ")
# Getting Data from Yahoo finance
multpl_stocks = web.get_data_yahoo(tickers,
                                   start="2020-01-01",
                                   end="2020-12-31")
print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
      "\n\n ---- STOCK DATA ---- \n")
print(multpl_stocks)

multpl_stock_monthly_returns = multpl_stocks['Adj Close'].resample(
    'M').ffill().pct_change()

while(run_program == True):
    def optionSelector(argument):

        # All functions that will run by the options
        def plotting_adjusted_close():
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

        def plotting_monthly_returns():
            fig = plt.figure()
            fig.set_size_inches(8.5, 5.5)
            (multpl_stock_monthly_returns + 1).cumprod().plot()
            plt.savefig("monthlyReturns.png")
            plt.show()

        def calculate_mean_of_monthly_returns():
            print(Fore.WHITE + Back.BLUE +
                  Style.BRIGHT + '\n\n ---- Mean ---- \n')
            print(multpl_stock_monthly_returns.mean())

        def calculate_std_dev_of_monthly_returns():
            print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
                  '\n\n ---- Standard Deviation ---- \n')
            print(multpl_stock_monthly_returns.std())

        def calculate_covariance_of_monthly_returns():
            print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
                  '\n\n ---- Covariance ---- \n')
            print(multpl_stock_monthly_returns.cov())

        def calculate_correlation_of_monthly_returns():
            print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
                  '\n\n ---- Correlation ---- \n')
            print(multpl_stock_monthly_returns.corr())

        def default_option():
            print("\n you have not selected a valid option \n")

        options = {
            1: plotting_adjusted_close,
            2: plotting_monthly_returns,
            3: calculate_mean_of_monthly_returns,
            4: calculate_std_dev_of_monthly_returns,
            5: calculate_covariance_of_monthly_returns,
            6: calculate_correlation_of_monthly_returns
        }
        return options.get(argument, default_option)

    # Menu of the program
    print(Fore.WHITE + Back.BLUE + Style.BRIGHT +
          "What would you like to do? You can choose an option from this menu")
    print(" 1 - Plotting the adjusted close of every stock \n 2 - Plotting Monthly Returns \n 3 - Calculate Mean of Monthly Returns \n 4 - Calculate standard deviation of monthly returns \n 5 - Calculate Covariance of Monthly Returns \n 6 - Calculate Correlation of Monthly Returns  \n ")
    option = int(input(
        "  Enter your option over here : "))

    optionSelector(option)()

    terminate_program = input(Fore.WHITE + Back.BLUE + Style.BRIGHT +
                              "Would you like to end the program or would you like to contnue ? \n To terminate enter Y else press enter : ")
    if (terminate_program == "Y" or terminate_program == "y"):
        run_program = False

print(" \n The Images has been stored in the working directory.")
print(Fore.WHITE + Back.BLUE + Style.BRIGHT + "\n  Have a nice day :)")
print("\n")
