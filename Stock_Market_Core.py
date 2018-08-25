##
# Project 	: Assignment – Super Simple Stock Market
# Pourpose 	: Core of Super Simple Stock Market
# Author	: Walugembe Francis
# Module 	: Super_Simple_Stock_Market
# Last Rev  : 1
# Update Log:
#
#
##
from datetime import datetime, timedelta
import math

__COM__  = 0
__PRE__  = 1
__BUY__  = 0
__SELL__ = 1

class Core:

	#_test_data = None
	#_version = "1.0.0.1"
	#_data = {}


	def __init__(self,stock,quantity,strflow,price,minutes):
		self._version= "1.0.0.1"
		self.stock=stock
		self.price=price
		self.strflow=strflow
		self.flow=None
		self.quantity=quantity
		self.minutes=minutes
		
		self._data= {}
		self._test_data = { 
                    "TEA":{"type":__COM__,"last":0 ,"fixed":None,"par":100},
                    "POP":{"type":__COM__,"last":8 ,"fixed":None,"par":100},
                    "ALE":{"type":__COM__,"last":23,"fixed":None,"par":60},
                    "GIN":{"type":__PRE__,"last":8 ,"fixed":0.02,"par":100},
                    "JOE":{"type":__COM__,"last":13,"fixed":None,"par":250},
            }		    
	
	
	def __del__(self):
		pass
	


	#
	# Return core version 
	#
	def version():
		return Core._version	
	 
	#
	# Return P/E ratio
	#
	def pe_ratio(self, stock, price):
		# force ZeroDivisionException
		if price < 0: 
			price = 0	

		if stock in self._test_data:
			stk = self._test_data[stock]
		else:
			raise Exception("Stock type {} not found".format(stock))	

		if stk["last"] < 0:
			raise Exeception("It does not make sense to calculate P/E ratio for negative earnings per share")
		elif stk["last"] == 0:
			return 0

		return price / stk["last"]


	#
	# Return Dividend Yeld
	#
	def dividend_yeld(self, stock, price):
		# force ZeroDivisionException
		if price < 0: 
			price = 0
		
		if stock in self._test_data:
			stk = self._test_data[stock]
		else:
			raise Exception("Stock type {} not found".format(stock))	

		if stk["type"] == __COM__:
			return stk["last"] / price

		return stk["fixed"] * stk["par"] / price

	#
	# Clear all trade data
	#
	def record_clean_all():
		Core._data = {}		
		

	#
	# Add a trade record
	#
	def record_trade(self,stock:str, quantity:float, strflow:str, price:float):
		
		
		
		if strflow == "BUY":
			self.flow = 0
		elif strflow== "SELL":
			self.flow = 1
		else:
			raise Exception("Invalid value for flow type")		
		
		
		
		
		timestamp = datetime.now()
		ele = {}
		if stock not in StockMarket._data:
			StockMarket._data[stock] = []
		ele[timestamp] =  {"quantity":quantity, "flow":self.flow, "price":price}
		StockMarket._data[stock].append(ele)
		

	#
	# Records past <interval> minutes
	#	
	def get_past_interval(self, stock, interval):
		if not stock in StockMarket._data:
			return []
		minutes = timedelta(minutes=interval)	
		min_time = datetime.now() - minutes
		# stock data
		stk_vals = list({k:v for k,v in StockMarket._data.items() if k == stock}.values())[0]
		# selected keys
		result = [list(tm.keys())[0] for tm in stk_vals if list(tm.keys())[0] > min_time]

		return result	

	def volume_weighted_stock_price(self, stock, interval):
		if StockMarket._data == {}:
			return None
		if not stock in StockMarket._data:
			return None 
		# get selected trades
		sel_trades = self.get_past_interval(stock, interval)
		# stock data
		stk_vals = list({k:v for k,v in StockMarket._data.items() if k == stock}.values())[0]
		# convert to dict
		d_stk_vals = {list(item.keys())[0]:list(item.values())[0] for item in stk_vals}
		# get sub set of _data building a list
		subset = {m:d_stk_vals[m] for m in d_stk_vals if m in sel_trades}
		# calculate wsp 
		volume = sum([(x['price']*x['quantity']) for x in subset.values()]) / sum([(x['quantity']) for x in subset.values()])
		return volume

	def GBCE(self, interval):
		if StockMarket._data == {}:
			return 0 
		stocks = set(StockMarket._data.keys())
		n = len(stocks)
		p = None
		for st in stocks:
			if p == None:
				p = self.volume_weighted_stock_price(st, interval)
			else: 
				p *= self.volume_weighted_stock_price(st, interval)
		if n > 0:
			return math.pow(p, 1/n)
		else:
			return 0


#StockMarket = Core('ALE',100)

StockMarket = Core('ALE',1,"BUY",100,5)

print (StockMarket._test_data)


#Given any price as input, calculate the dividend yield
dy = StockMarket.dividend_yeld(StockMarket.stock, float(StockMarket.price))
print (dy)


#Given any price as input, calculate the P/E Ratio
pe = StockMarket.pe_ratio(StockMarket.stock, float(StockMarket.price))
print (pe)


#Record a trade, with timestamp, quantity, buy or sell indicator and price


StockMarket.record_trade(StockMarket.stock, StockMarket.quantity, StockMarket.strflow,StockMarket.price)
	
print (StockMarket._data)
		
#Calculate Volume Weighted Stock Price based on trades in past 5 minutes

volume = StockMarket.volume_weighted_stock_price(StockMarket.stock, int(StockMarket.minutes))

print (volume)

#Calculate the GBCE All Share Index using the geometric mean of the Volume Weighted Stock Price for all stocks
gmean = StockMarket.GBCE(int(StockMarket.minutes))

print (gmean)

