import unittest
import pymysql

class TestSQLQueries(unittest.TestCase):
    def test_select_all_employees(self):
        conn = pymysql.connect(host='localhost', user='root', password='password', db='test')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees;")
        result = cursor.fetchall()
        expected = [(1, 'John', 'Doe', 50000), (2, 'Jane', 'Doe', 60000), (3, 'Bob', 'Smith', 55000)]
        self.assertEqual(result, expected)
        conn.close()

if __name__ == '__main__':
    unittest.main()
