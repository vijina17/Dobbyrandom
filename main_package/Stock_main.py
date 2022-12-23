# stock main
# class for Stock
# contain the input for number of rounds to paly with
import numpy as np
import random
class Stock(object):
      # set the parameters as global variables
      def __init__(self):
            size = int(input("How many round do you want to play with?"))
            self.n = int(size)
      
            print("You are going to play {} round, get ready!!!!!!!!\n".format(self.n))
            self.high_price_list = [random.randint(201, 500) for i in range(int(self.n))]
            self.low_price_list = [random.randint(50, 200) for i in range(int(self.n))]
            self.volume_list = [random.randint(1, 200) for i in range(int(self.n))]

      # when we start the program, it will ask user to input the numbers of round user want to play with, use print
      def get_high_price(self):
            return self.high_price_list
      def get_low_price(self):
            return self.low_price_list
      def get_volume(self):
            return self.volume_list
      def get_size(self):
            return int(self.n)
      
      def __str__(self):
            return f"high price list: {self.high_price_list}\nlow price list: {self.low_price_list}\nvolume list: {self.volume_list}"

