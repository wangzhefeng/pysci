-- ==============================================================================
-- MySQL
-- ==============================================================================
-- 443 ms
SELECT 
	A.Request_at AS Day,
	ROUND(SUM(A.Status != 'completed') / COUNT(A.Status), 2) AS 'Cancellation Rate' 
FROM Trips A
WHERE 
	A.Client_Id IN (SELECT Users_Id FROM Users WHERE Banned != 'Yes') AND 
	A.Driver_Id IN (SELECT Users_Id FROM Users WHERE Banned != 'Yes') AND 
	A.Request_at >= '2013-10-01' AND 
    A.Request_at <='2013-10-03'
GROUP BY 
	A.Request_at
ORDER BY 
	A.Request_at


-- 365
SELECT 
	A.Request_at AS Day,
	ROUND(SUM(A.Status != 'completed') / COUNT(1), 2) AS 'Cancellation Rate' 
FROM Trips A
WHERE 
	A.Client_Id IN (SELECT Users_Id FROM Users WHERE Banned != 'Yes') AND 
	A.Driver_Id IN (SELECT Users_Id FROM Users WHERE Banned != 'Yes') AND 
	A.Request_at >= '2013-10-01' AND 
    A.Request_at <='2013-10-03'
GROUP BY 
	A.Request_at
ORDER BY 
	A.Request_at


-- ==============================================================================
-- Sql Server
-- ==============================================================================
-- 1139ms
SELECT 
	A.Request_at AS Day,
	ROUND(COUNT(CASE WHEN A.Status != 'completed' THEN A.Status ELSE NULL END) * 1.0 / COUNT(A.Status), 2) AS [Cancellation Rate]
FROM Trips A
INNER JOIN Users B
	ON A.Client_Id = B.Users_Id
	   AND B.Banned = 'No'
	   AND B.Role = 'client'
INNER JOIN Users C
	ON A.Driver_Id = C.Users_Id
	   AND C.Banned = 'No'
	   AND C.Role = 'driver'
WHERE 
	A.Request_at >= '2013-10-01' AND 
	A.Request_at <= '2013-10-03'
GROUP BY 
	A.Request_at
ORDER BY 
	A.Request_at


-- 1441ms
SELECT 
	A.Request_at AS Day,
	ROUND(COUNT(CASE WHEN A.Status != 'completed' THEN A.Status ELSE NULL END) * 1.0 / COUNT(A.Status), 2) AS [Cancellation Rate]
FROM Trips A
WHERE 
	A.Client_Id IN (SELECT Users_Id FROM Users WHERE Banned != 'Yes') AND 
	A.Driver_Id IN (SELECT Users_Id FROM Users WHERE Banned != 'Yes') AND 
	A.Request_at >= '2013-10-01' AND 
    A.Request_at <='2013-10-03'
GROUP BY 
	Request_at
ORDER BY 
	Request_at


-- ==============================================================================
-- Oracle
-- ==============================================================================
SELECT 
	A.Request_at AS Day,
	ROUND(SUM(CASE WHEN A.Status != 'completed' THEN 1 ELSE 0 END) / COUNT(1), 2) AS "Cancellation Rate" 
FROM Trips A
WHERE 
	A.Client_Id IN (SELECT Users_Id FROM Users WHERE Banned != 'Yes') AND 
	A.Driver_Id IN (SELECT Users_Id FROM Users WHERE Banned != 'Yes') AND 
	A.Request_at >= '2013-10-01' AND 
    A.Request_at <='2013-10-03'
GROUP BY 
	A.Request_at
ORDER BY 
	A.Request_at


select 
	t.Request_at as "Day", 
	round(sum(case when t.Status != 'completed' then 1 else 0 end) / count(1), 2) as "Cancellation Rate" 
from Trips t 
join Users u 
	on t.Client_Id = u.Users_Id 
where 
	u.Banned = 'No' and 
	t.Request_at >= '2013-10-01' and
    t.Request_at <= '2013-10-03' 
group by t.Request_at 
order by t.Request_at

