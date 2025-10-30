CREATE TABLE Employees (
  EmployeeID INT PRIMARY KEY,
  EmployeeName VARCHAR(100) NOT NULL,
  ManagerID INT NULL
);

INSERT INTO Employees (EmployeeID, EmployeeName, ManagerID) VALUES
(1, 'Rajesh', NULL),          -- no manager
(2, 'Hardik Shah', 1),        -- reports to Rajesh
(3, 'Ajay Jain', 2),          -- reports to Hardik
(4, 'Asif Shamim', 2);        -- reports to Hardik


EmployeeID | Employee      | ManagerID
-----------+---------------+--------------
1          | Rajesh        | 
2          | Hardik Shah   | 1
3          | Ajay Jain     | 2
4          | Asif Shamim   | 3
