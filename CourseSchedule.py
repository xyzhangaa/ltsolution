###There are a total of n courses you have to take, labeled from 0 to n - 1.

###Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

###Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

class Solution:
  def courseschedule(self,numCourse,prerequisites):
    degree = [0]*numCourse
    childs = [[] for _ in range(numCourse)]
    for pair in prerequisites:
      degree[pair[0]] += 1
      childs[pair[1]].append(pair[0])
    courses = set(range(numCourse))
    flag= True
    while flag and len(courses):
      flag= False
      removeList = []
      for x in course:
        if degree[x] == 0:
          for child in childs[x]:
            degree[child] -= 1
          removeList.append(x)
          flag = True
      for x in removeList:
        courses.remove(x)
      return len(courses) == 0
