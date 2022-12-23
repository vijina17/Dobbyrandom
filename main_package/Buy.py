import random

class Buy:
      
# """A class for buying stocks."""

      def __init__(self, high_price, low_price, balance):
            """Initialize the buy object with the given high price, low price, and balance."""
            self.high_price = high_price
            self.low_price = low_price
            self.balance = balance
            self.volume = 0
            self.price = 0
            self.expense = 0

      def can_afford_expense(self, balance, expense):
            """Return True if the balance is greater than or equal to the expense, False otherwise."""
            return balance - expense >= 0
            
      def has_sufficient_volume(self, current_volume, input_volume):
            """Return True if the current volume is greater than or equal to the input volume, False otherwise."""
            return current_volume - input_volume >= 0

      def execute(self, high_price, low_price, balance, input_volume, random_price):
            """Execute a buy transaction with the given high price, low price, balance, input volume, and random price."""
            info = []
            input_volume = float(input_volume)
                  
            can_afford = self.can_afford_expense(balance, input_volume * random_price)
            buy_price = float(random_price)
            buy_volume = float(input_volume)
            total_price = buy_price * buy_volume
                  
            info.append(total_price)
            info.append(buy_price)
            info.append(buy_volume)
            return info
            
      def buy_stock(self, vol):
            """Buy a stock with the given volume."""
            high_price_ = self.high_price
            low_price_ = self.low_price
            balance_ = self.balance
            vol_ = vol
            random_price = float(random.randint(int(low_price_), int(high_price_)))
                        
            print("|The random price of stock: {}\t|".format(random_price))
            print("|Volume of stock is {}\t\t\t|".format(vol))
            input_volume = float(input("How many volume do you want to buy?\n"))
            
            can_afford_expense = self.can_afford_expense(balance_, input_volume * random_price)
            has_sufficient_volume = self.has_sufficient_volume(vol_, input_volume)
            print("|You bought {} volume of stock  \t|".format(input_volume))
            print("|Input vol: {}, expense: {} \t|".format(input_volume, input_volume * random_price))
            if can_afford_expense and has_sufficient_volume:
                  execute_result = self.execute(high_price_, low_price_, balance_, input_volume, random_price)
                  return execute_result
            else:
                  print("|\t-------- Warning --------\t|")  
                  while not can_afford_expense:
                        print("|The vol you input is {}, and the expense is {}".format(input_volume, input_volume * random_price))
                        print("|Sorry, the balance is not enough")
                        print("|Please buy a smaller volume")
                        input_volume = int(input("How many volume do you want to buy?\n"))
                        input_volume = float(input_volume)
                        can_afford_expense = self.can_afford_expense(balance_, input_volume * random_price)
                  if can_afford_expense:
                        print("|You bought {} volume of stock\t\t|".format(input_volume))
                        execute_result = self.execute(high_price_, low_price_, balance_, input_volume, random_price)
                        return execute_result
                  while not has_sufficient_volume:
                        print("|The vol you input is {}, and the expense is {}".format(input_volume, input_volume * random_price))
                        print("|Sorry, the input volume is larger than the available volume of the stock")
                        print("|Please buy a smaller volume")
                        input_volume = int(input("How many volume do you want to buy?\n"))
                        input_volume = float(input_volume)
                        has_sufficient_volume = self.has_sufficient_volume(vol_, input_volume)
                        if has_sufficient_volume:
                              print("|You bought {} volume of stock\t\t|".format(input_volume))
                              execute_result = self.execute(high_price_, low_price_, balance_, input_volume, random_price)
                              return execute_result
