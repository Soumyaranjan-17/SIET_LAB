CREATE TABLE Employee_59 (
    Eid INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dept_id INT
);

INSERT INTO Employee_59 (Eid, name, dept_id) VALUES (1, 'John', 101);
INSERT INTO Employee_59 (Eid, name, dept_id) VALUES (2, 'Alice', 102);
INSERT INTO Employee_59 (Eid, name, dept_id) VALUES (3, 'Bob', 101);
INSERT INTO Employee_59 (Eid, name, dept_id) VALUES (4, 'Charlie', 104);


SELECT * FROM Employee_59;
Describe Employee_59;

CREATE TABLE Department_59 (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
);

INSERT INTO Department_59 (dept_id, dept_name) VALUES (101, 'HR');
INSERT INTO Department_59 (dept_id, dept_name) VALUES (102, 'Engineering');
INSERT INTO Department_59 (dept_id, dept_name) VALUES (103, 'Finance');
INSERT INTO Department_59 (dept_id, dept_name) VALUES (104, 'Operations');

SELECT * FROM Department_59;
Describe Department_59;



// Inner Join //

SELECT E.name, D.dept_name
FROM Employee_59 E
INNER JOIN Department_59 D
ON E.dept_id = D.dept_id;

 // LEFT OUTER JOIN //

SELECT E.name, D.dept_name
FROM Employee_59 E
LEFT OUTER JOIN Department_59 D
ON E.dept_id = D.dept_id;


 // RIGHT OUTER JOIN //

SELECT E.name, D.dept_name
FROM Employee_59 E
RIGHT OUTER JOIN Department_59 D
ON E.dept_id = D.dept_id;


 // FULL OUTER JOIN //

SELECT E.name, D.dept_name
FROM Employee_59 E
FULL OUTER JOIN Department_59 D
ON E.dept_id = D.dept_id;


 // CROSS JOIN //

SELECT E.name, D.dept_name
FROM Employee_59 E
CROSS JOIN Department_59 D;

 // NATURAL JOIN //

SELECT E.name, D.dept_name
FROM Employee_59 E
NATURAL JOIN Department_59 D;

// SELF JOIN //

ALTER TABLE Employee_59
ADD managerId NUMBER(10);

UPDATE Employee_59
SET managerId = 3
WHERE eid = 1 ;

UPDATE Employee_59
SET managerId = 3
WHERE eid = 2;

UPDATE Employee_59
SET managerId = 1
WHERE eid = 4;

SELECT e1.name as employee_1, e2.name as employee_2
FROM Employee_59 e1
JOIN Employee_59 e2
ON e1.eid = e2.managerId
