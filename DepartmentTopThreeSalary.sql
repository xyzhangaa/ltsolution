The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables, your SQL query should return the following rows.

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Joe      | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+

# Write your MySQL query statement below
SELECT d.NAME AS Department, t.NAME AS Employee, Salary FROM (
  SELECT    DepartmentId,
            NAME,
            Salary, 
            @rank := IF(@prevDeptId != DepartmentId, 1, 
                         IF(@prevSalary = Salary, @rank, @rank + 1) ) AS Rank,
            @prevDeptId := DepartmentId AS prevDeptId,
            @prevSalary := Salary AS prevSalary
  FROM      Employee e, (SELECT @rank := 0, @prevDeptId := NULL, @prevSalary := NULL) r
  ORDER BY  DepartmentId ASC, Salary DESC
) t INNER JOIN Department d ON t.DepartmentId = d.ID
WHERE t.rank <= 3

# Write your MySQL query statement below
SELECT D.Name AS Department, E.Name AS Employee, E.Salary AS Salary 
FROM Employee E, Department D
WHERE (SELECT COUNT(DISTINCT(Salary)) FROM Employee 
       WHERE DepartmentId = E.DepartmentId AND Salary > E.Salary) < 3
AND E.DepartmentId = D.Id 
ORDER by E.DepartmentId, E.Salary DESC;