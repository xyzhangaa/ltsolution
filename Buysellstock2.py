###Say you have an array for which the ith element is the price of a given stock on day i.
###Design an algorithm to find the maximum profit. You may complete as many transactions as 
###you like (ie, buy one and sell one share of the stock multiple times). However, you may 
###not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

#O(n), O(1)
def maxprofitstock(price):
	maxprofit = 0
	if len(price) <= 1:
		return maxprofit
	for i in range(len(price)-1):
		if price[i+1] > price[i]:
			maxprofit = maxprofit + price[i+1]-price[i]
	return maxprofit
