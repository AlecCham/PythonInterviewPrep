import sqlite3
from sqlite3 import Error

class DatabaseManager:
    def __init__(self, db_file):
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

    def create_table(self, create_table_sql):
        try:
            c = self.connection.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def execute_query(self, query, params=None):
        try:
            c = self.connection.cursor()
            if params:
                c.execute(query, params)
            else:
                c.execute(query)
            self.connection.commit()
            return c
        except Error as e:
            print(e)

    def close(self):
        self.connection.close()

class Project:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def create_projects_table(self):
        create_table_sql = """CREATE TABLE IF NOT EXISTS projects (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                begin_date TEXT,
                                end_date TEXT
                            );"""
        self.db_manager.create_table(create_table_sql)

    def add_project(self, name, begin_date, end_date):
        query = "INSERT INTO projects(name, begin_date, end_date) VALUES(?,?,?)"
        params = (name, begin_date, end_date)
        return self.db_manager.execute_query(query, params).lastrowid

    def list_projects(self):
        c = self.db_manager.execute_query("SELECT * FROM projects")
        return c.fetchall()

    def update_project(self, project_id, name, begin_date, end_date):
        query = """ UPDATE projects
                    SET name = ?, begin_date = ?, end_date = ?
                    WHERE id = ?"""
        params = (name, begin_date, end_date, project_id)
        self.db_manager.execute_query(query, params)

    def delete_project(self, project_id):
        query = "DELETE FROM projects WHERE id=?"
        params = (project_id,)
        self.db_manager.execute_query(query, params)

# Usage
db_file = "pythonsqlite.db"
db_manager = DatabaseManager(db_file)
project_manager = Project(db_manager)

# Create Projects Table
project_manager.create_projects_table()

# Add a Project
project_id = project_manager.add_project('Python Project', '2021-01-01', '2022-01-01')

# List Projects
projects = project_manager.list_projects()
print(projects)

# Update a Project
project_manager.update_project(project_id, 'Updated Python Project', '2021-02-01', '2022-02-01')

# Delete a Project
#project_manager.delete_project(project_id)

# Close Connection
db_manager.close()




#Update instead of recreate
# Usage
db_file = "pythonsqlite.db"
db_manager = DatabaseManager(db_file)
project_manager = Project(db_manager)

# Create Projects Table
project_manager.create_projects_table()

# Add a Project
project_id = project_manager.add_project('Python Project', '2021-01-01', '2022-01-01')

# List Projects
projects = project_manager.list_projects()
print(projects)

# Update a Project
project_manager.update_project(project_id, 'Updated Python Project', '2021-02-01', '2022-02-01')

# Delete a Project
#project_manager.delete_project(project_id)

# Close Connection
db_manager.close()

