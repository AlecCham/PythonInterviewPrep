import unittest
import sqlite3

class TestEmployeeDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')  # Using in-memory database for tests
        self.conn.execute('BEGIN')
        self.cursor = self.conn.cursor()
        self.setup_database(self.cursor)

    def tearDown(self):
        self.conn.rollback()
        self.conn.close()

    @staticmethod
    def setup_database(cursor):
        cursor.execute('''
            CREATE TABLE employees (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                salary INTEGER,
                department_id INTEGER
            );
        ''')
        cursor.execute('''
            INSERT INTO employees (first_name, last_name, salary, department_id)
            VALUES ('John', 'Doe', 50000, 1),
                   ('Jane', 'Doe', 60000, 1),
                   ('Bob', 'Smith', 55000, 2);
        ''')
        cursor.execute('''
            CREATE TABLE departments (
                id INTEGER PRIMARY KEY,
                name TEXT
            );
        ''')
        cursor.execute('''
            INSERT INTO departments (name)
            VALUES ('Engineering'),
                   ('Human Resources'),;
        ''')
        # Create Projects Table
        cursor.execute('''
            CREATE TABLE projects (
                id INTEGER PRIMARY KEY,
                name TEXT,
                budget INTEGER
            );
        ''')

        # Insert Projects
        cursor.execute('''
            INSERT INTO projects (name, budget) 
            VALUES ('Project Alpha', 100000),
                   ('Project Beta', 150000);
        ''')

        # Create Employee_Projects Table
        cursor.execute('''
            CREATE TABLE employee_projects (
                employee_id INTEGER,
                project_id INTEGER,
                hours_allocated INTEGER,
                FOREIGN KEY (employee_id) REFERENCES employees(id),
                FOREIGN KEY (project_id) REFERENCES projects(id)
            );
        ''')

        # Insert Employee_Projects Relations
        cursor.execute('''
            INSERT INTO employee_projects (employee_id, project_id, hours_allocated) 
            VALUES (1, 1, 30),
                   (2, 1, 20),
                   (3, 2, 40);
        ''')



    def test_select_all_employees(self):
        self.cursor.execute("SELECT * FROM employees ORDER BY id;")
        result = self.cursor.fetchall()
        expected = [(1, 'John', 'Doe', 50000, 1), (2, 'Jane', 'Doe', 60000, 1), (3, 'Bob', 'Smith', 55000, 2)]
        self.assertEqual(result, expected)


    def test_employee_salaries(self):
        self.cursor.execute("SELECT first_name, salary FROM employees ORDER BY salary DESC;")
        result = self.cursor.fetchall()
        expected = [('Jane', 60000), ('Bob', 55000), ('John', 50000)]
        self.assertEqual(result, expected)



    def test_join_employees_departments(self):
        self.cursor.execute('''
            SELECT employees.first_name, departments.name
            FROM employees
            JOIN departments ON employees.department_id = departments.id
            ORDER BY employees.id;
        ''')
        result = self.cursor.fetchall()
        expected = [('John', 'Engineering'), ('Jane', 'Engineering'), ('Bob', 'Human Resources')]
        self.assertEqual(result, expected)


    def test_update_employee_salary(self):
        self.cursor.execute("UPDATE employees SET salary = salary + 5000 WHERE first_name = 'John';")
        self.cursor.execute("SELECT salary FROM employees WHERE first_name = 'John';")
        result = self.cursor.fetchone()[0]
        expected = 55000
        self.assertEqual(result, expected)

    def test_delete_employee(self):
        self.cursor.execute("DELETE FROM employees WHERE first_name = 'Bob';")
        self.cursor.execute("SELECT * FROM employees WHERE first_name = 'Bob';")
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 0)

    def test_employees_in_project_alpha(self):
        self.cursor.execute('''
            SELECT employees.first_name, employees.last_name
            FROM employees
            JOIN employee_projects ON employees.id = employee_projects.employee_id
            JOIN projects ON employee_projects.project_id = projects.id
            WHERE projects.name = 'Project Alpha';
        ''')
        result = self.cursor.fetchall()
        expected = [('John', 'Doe'), ('Jane', 'Doe')]
        self.assertEqual(result, expected)

    def test_total_hours_project_alpha(self):
        self.cursor.execute('''
            SELECT SUM(hours_allocated) as total_hours
            FROM employee_projects
            JOIN projects ON employee_projects.project_id = projects.id
            WHERE projects.name = 'Project Alpha';
        ''')
        result = self.cursor.fetchone()[0]
        expected = 50  # Total hours allocated to Project Alpha
        self.assertEqual(result, expected)

    def test_update_project_budget(self):
        new_budget = 200000
        self.cursor.execute("UPDATE projects SET budget = ? WHERE name = 'Project Beta';", (new_budget,))
        self.cursor.execute("SELECT budget FROM projects WHERE name = 'Project Beta';")
        result = self.cursor.fetchone()[0]
        self.assertEqual(result, new_budget)


if __name__ == '__main__':
    unittest.main()
