###Say you have an array for which the ith element is the price of a given stock on day i.
###Design an algorithm to find the maximum profit. You may complete at most two transactions.

#O(n), O(n)
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
		for i in range(len(price)):
			profit = maxprofitendhere[i]+maxprofitstarthere[i]
			maxprofit = max(maxprofit,profit)
		return maxprofit

# Time:  O(n)
# Space: O(1)
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        hold1, hold2 = float("-inf"), float("-inf")
        release1, release2 = 0, 0
        for i in prices:
            release2 = max(release2, hold2 + i)
            hold2    = max(hold2,    release1 - i)
            release1 = max(release1, hold1 + i)
            hold1    = max(hold1,    -i);
        return release2
    
# Time:  O(k * n)
# Space: O(k)
class Solution2:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return self.maxAtMostKPairsProfit(prices, 2)
        
    def maxAtMostKPairsProfit(self, prices, k):
        max_buy = [float("-inf") for _ in xrange(k + 1)]
        max_sell = [0 for _ in xrange(k + 1)]

        for i in xrange(len(prices)):
            for j in xrange(1, min(k, i/2+1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j-1] - prices[i])
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])

        return max_sell[k]
