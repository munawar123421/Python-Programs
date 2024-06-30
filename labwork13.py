import mysql.connector
from mysql.connector import Error
import datetime

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query executed successfully")
        return cursor.lastrowid
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def log_audit(connection, operation, table_name, record_id, description):
    audit_query = """
    INSERT INTO audit_log (operation, table_name, record_id, timestamp, description)
    VALUES (%s, %s, %s, %s, %s)
    """
    timestamp = datetime.datetime.now()
    audit_data = (operation, table_name, record_id, timestamp, description)
    execute_query(connection, audit_query, audit_data)

def insert_student(connection, student_name, student_age, student_grade):
    insert_student_query = """
    INSERT INTO students (name, age, grade)
    VALUES (%s, %s, %s)
    """
    student_data = (student_name, student_age, student_grade)
    student_id = execute_query(connection, insert_student_query, student_data)
    if student_id:
        log_audit(connection, 'INSERT', 'students', student_id, 'Record inserted successfully')

def main():
    connection = create_connection("your_host", "your_username", "your_password", "your_database")

    while True:
        student_name = input("Enter student name: ")
        student_age = int(input("Enter student age: "))
        student_grade = input("Enter student grade: ")

        insert_student(connection, student_name, student_age, student_grade)

        add_another = input("Do you want to add another student record? (yes/no): ").lower()
        if add_another != 'yes':
            break

    if connection:
        connection.close()

if __name__ == "__main__":
    main()
