###There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

###You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to 
###its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

###Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

#O(n), O(1)
def gasstation(gas,cost):
  if sum(gas) < sum(cost):
    return -1
  else:
    start = 0
    left = 0
    for i in range(len(gas)):
      if gas[i]+left < cost[i]:
        start = i+1
        left = 0
      else:
        left += gas[i]-cost[i]
    return start
