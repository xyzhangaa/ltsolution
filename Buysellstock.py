#O(n), O(1)
### Iteratively
def maxprofitstock(price):
	i=1
	while i<len(price)-1:
		if price[i] < price[i-1]:
			i+=1
		else:
			break
	else:
		return 0	
	buyday=i-1
	sellday=i
	maxbenefit = price[sellday]-price[buyday]
	while sellday < len(price)-1 and buyday < len(price):
		if price[sellday+1] < price[buyday]:
			buyday = sellday+1
			sellday = sellday+1
			maxbenefit = max(maxbenefit, price[sellday]- \
					 price[buyday])
		else:
			sellday = sellday+1
			maxbenefit = max(maxbenefit,price[sellday]- \
					 price[buyday])
	return maxbenefit
	
### Itervatively Two
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        maxprofit = 0
        low = prices[0]
        for i in range(1,len(prices)):
            low = min(low,prices[i])
            maxprofit = max(maxprofit,prices[i]-low)
        return maxprofit
