-- mssql
CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        select distinct salary
		from (
			select 
				salary, 
				dense_rank() over(order by Salary desc) as Rank
			from Employee
		) p
		where p.Rank = @N
    );
END



CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        select distinct salary
		from (
			select 
				salary, 
				rank() over(order by Salary desc) as Rank
			from Employee
		) p
		where p.Rank = @N
    );
END