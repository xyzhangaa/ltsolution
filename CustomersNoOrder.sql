##Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.


#Solution1:
# Write your MySQL query statement below
SELECT Name FROM Customers c WHERE c.Id NOT IN (SELECT CustomerId FROM Orders o);

#Solution2:
SELECT Name FROM Customers c WHERE NOT EXISTS (SELECT CustomerId FROM Orders o WHERE o.CustomerId = c.Id);

#Solution3:
SELECT Name FROM Customers c LEFT JOIN Orders o ON c.Id = o.CustomerId WHERE o.Id IS NULL;
