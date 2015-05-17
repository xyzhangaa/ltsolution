###There are a total of n courses you have to take, labeled from 0 to n - 1.

###Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

###Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

###There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

class Solution:
  def findOrder(self,numCourses,prerequisites):
    degree = [0]*numCourses
    childs = [[] for _ in range(numCourses)]
    for pair in prerequisites:
      degree[pair[0]] += 1
      childs[pair[1]].append(pair[0])
    courses = set(range(numCourses))
    flag= True
    res = []
    while flag and len(courses):
      flag = False
      removeList = []
      for x in courses:
        if degree[x] == 0:
          for child in childs[x]:
            degree[child] -= 1
          removeList.append(x)
          flag = True
      for x in removeList:
        res.append(x)
        courses.remove(x)
    return [[],res][len(courses) == 0]
