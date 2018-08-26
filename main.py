
from Stock_Market_Core import   Core
#from Stock_Market_Core.Core import dividend_yeld

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


_data=StockMarket.record_trade(StockMarket.stock, StockMarket.quantity, StockMarket.strflow,StockMarket.price)
	
print (Core._data)


#Record interval
inter=StockMarket.get_past_interval( StockMarket.stock, 5)
print (inter)


		
#Calculate Volume Weighted Stock Price based on trades in past 5 minutes

volume = StockMarket.volume_weighted_stock_price(StockMarket.stock, int(StockMarket.minutes))

print (volume)


#Calculate the GBCE All Share Index using the geometric mean of the Volume Weighted Stock Price for all stocks
gmean = StockMarket.GBCE(int(StockMarket.minutes))

print (gmean)
