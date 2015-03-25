###Say you have an array for which the ith element is the price of a given stock on day i.
###Design an algorithm to find the maximum profit. You may complete at most two transactions.

def buysellstock(price):
	if len(price) <= 1:
		return 0
	else:
		maxprofitendhere=[0]*len(price)
		maxprofitend = price[0]
		for i in range(1,len(price)):
			maxprofitend = min(price[i],maxprofitend)
			maxprofitendhere[i] = max(price[i]-maxprofitend, \
						  maxprofitendhere[i-1])
		maxprofitstarthere=[0]*len(price)
		maxprofitstart = price[-1]
		for i in range(len(price)-2,-1,-1):
			maxprofitstart = max(price[i],maxprofitstart)
			maxprofitstarthere[i] = max(maxprofitstart-price[i], \
						  maxprofitstarthere[i+1])
		maxprofit = maxprofitendhere[-1]
		for i in range(len(price)-1):
			profit = maxprofitendhere[i]+maxprofitstarthere[i]
			maxprofit = max(maxprofit,profit)
		return maxprofit

