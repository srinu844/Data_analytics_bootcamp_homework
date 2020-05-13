CREATE TABLE departments (
    dept_no varchar(4),  
    dept_name varchar 
);
select * from departments;

CREATE TABLE employees (
    emp_no int,
	emp_title_id varchar,
    birth_date varchar(10),
    first_name varchar,
    last_name varchar,
    sex varchar(1),
    hire_date varchar(10)
);
select * from employees;

CREATE TABLE dept_manager (
    dept_no varchar(4),
    emp_no int
);

select * from dept_manager


CREATE TABLE dept_emp (
    emp_no int,
    dept_no varchar(4)
);

select * from dept_emp;


drop table titles 
CREATE TABLE titles (
    title_id varchar,
    title varchar
);

select * from titles;


CREATE TABLE salaries (
    emp_no int,
    salary int
);

select * from salaries;



---1) List the following details of each employee: employee number, last name, first name, gender, and salary.

SELECT e.emp_no,e.last_name,e.first_name,e.sex,s.salary
FROM employees AS e JOIN salaries AS s ON s.emp_no = e.emp_no;

---2)List employees who were hired in 1986

SELECT first_name || ' ' || last_name AS "Employee", hire_date
FROM employees
WHERE hire_date >= '1986-01-01' AND hire_date <= '1986-12-31';

---3) List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT dm.dept_no, dept_name, dm.emp_no, first_name, last_name
FROM dept_manager dm
LEFT JOIN departments on dm.dept_no = departments.dept_no
LEFT JOIN employees on dm.emp_no = employees.emp_no;

--- 4) List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT e.emp_no, first_name, last_name, dept_name
FROM employees e
LEFT JOIN dept_emp d
ON e.emp_no = d.emp_no
LEFT JOIN departments ON d.dept_no = departments.dept_no;

--- 5) List all employees whose first name is "Hercules" and last names begin with "B."
SELECT * FROM employees
WHERE(first_name LIKE 'Hercules' AND last_name LIKE '%B%');

--- 6) List all employees in the Sales department, including their employee number, last name, first name, and department name.
Select e.emp_no, last_name, first_name, dept_name
FROM employees e
LEFT JOIN dept_emp d ON e.emp_no = d.emp_no
LEFT JOIN departments ON d.dept_no = departments.dept_no 
WHERE departments.dept_name lIKE 'Sales';

--- 7) List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
Select e.emp_no, first_name, last_name, dept_name
FROM employees e
LEFT JOIN dept_emp d ON e.emp_no = d.emp_no
LEFT JOIN departments ON d.dept_no = departments.dept_no 
WHERE departments.dept_name lIKE 'Sales'
OR departments.dept_name LIKE  'Development';

--- 8) In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name,
COUNT(last_name) AS "count_name"
from employees
GROUP BY last_name
ORDER BY count_name DESC;
