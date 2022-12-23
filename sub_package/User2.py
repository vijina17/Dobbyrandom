from main_package.Buy import *

class User:
      """A class representing a user who buys and sells stocks."""

      def __init__(self, stock, balance=10000):
            """Initialize the user with the given stock object and balance."""
            self.stock = stock
            self.balance = balance
            self.stock_owned = 0
            self.profit_loss = 0
            self.stock_price = 0
      
      def print_stock_info(self, high_price, low_price, volume):
            """Print the stock info for the current round."""
            print(f"|The high price of stock is {high_price}\t|")
            print(f"|The low price of stock is {low_price}\t\t|")
            print(f"|The volume of stock is {volume}\t\t|")

      def buy_stock(self, high_price, low_price, balance, vol):
            """Prompt the user to buy a stock with the given high price, low price, balance, and volume."""
            buy_transaction = Buy(high_price, low_price, balance)
            purchase_info = buy_transaction.buy_stock(high_price, low_price, balance, vol)
            self.balance -= purchase_info[0]
            self.stock_owned += purchase_info[2]
            self.stock_price = purchase_info[1]
            print(f"|Your balance is {self.balance}\t\t\t|")
            print(f"|You own {self.stock_owned} volume of stock\t\t|")
            print(f"|Your stock price is {self.stock_price}\t\t\t|")
            return purchase_info
            
      def sell_stock(self, high_price, low_price, balance, vol, stock_owned, stock_price):
            """Prompt the user to sell a stock with the given high price, low price, balance, volume, stock owned, and stock price."""
            sell_transaction = Sell(high_price, low_price, balance, stock_owned, stock_price)
            sell_info = sell_transaction.sell_stock(high_price, low_price, balance, vol, stock_owned, stock_price)
            self.balance += sell_info[0]
            self.stock_owned -= sell_info[2]
            self.profit_loss += sell_info[0] - sell_info[1]
            print(f"|Your balance is {self.balance}\t\t\t|")
            print(f"|You own {self.stock_owned} volume of stock\t\t|")
            print(f"|Your profit/loss is {self.profit_loss}\t\t|")

