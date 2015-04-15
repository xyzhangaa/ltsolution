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
