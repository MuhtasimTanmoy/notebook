# SQL Snippets

- [Group by vs Partition By](https://www.sqlshack.com/sql-partition-by-clause-overview/)

```sql
# Select expression and group by expression must be same

SELECT Customercity,
       AVG(Orderamount) AS AvgOrderAmount, 
       MIN(OrderAmount) AS MinOrderAmount, 
       SUM(Orderamount) TotalOrderAmount
FROM [dbo].[Orders]
GROUP BY Customercity;


# Partition by returns all rows, not just grouped rows, can add any field

SELECT Customercity, 
       CustomerName, 
       ROW_NUMBER() OVER(PARTITION BY Customercity
       ORDER BY OrderAmount DESC) AS "Row Number", 
       OrderAmount, 
       AVG(Orderamount) OVER(PARTITION BY Customercity) AS AvgOrderAmount, 
       MIN(OrderAmount) OVER(PARTITION BY Customercity) AS MinOrderAmount, 
       SUM(Orderamount) OVER(PARTITION BY Customercity) TotalOrderAmount
FROM [dbo].[Orders];


-- Cumulative sum of orderamount

SELECT Customercity, 
       CustomerName, 
       OrderAmount, 
       ROW_NUMBER() OVER(PARTITION BY Customercity
       ORDER BY OrderAmount DESC) AS "Row Number", 
       CONVERT(VARCHAR(20), SUM(orderamount) OVER(PARTITION BY Customercity
       ORDER BY OrderAmount DESC ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING), 1) AS CumulativeTotal,

```

