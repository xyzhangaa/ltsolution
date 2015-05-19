###Given a string containing only digits, restore it by returning all possible valid IP address combinations.
###For example:
###Given "25525511135",
###return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


# O(n^m) = O(3^4), O(m*n)=O(3*4)
def restoreIPaddress(s):
	def dfs(s,sub,ips,ip):
		if sub == 4:
			if s == '':
				ips.append(ip[1:])
			return
		for i in range(1,4):
			if i <= len(s):
				if int(s[:i]) <= 255:
					dfs(s[i:],sub+1,ips,ip+'.'+s[:i])
				if s[0] == '0':
					break
	ips = []
	dfs(s,0,ips,'')
	return ips
