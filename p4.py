import mysql.connector

# Function to create a MySQL connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ritesh",
        database="database1"
    )

# Function to create the Customer table
def create_customer_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customer (
            CustNo INT PRIMARY KEY,
            CustName VARCHAR(255) NOT NULL,
            Age INT,
            Gender VARCHAR(10),
            Salary FLOAT
        )
    ''')
    connection.commit()

# Function to insert values into the Customer table
def insert_customer_data(connection):
    cursor = connection.cursor()
    customers = [
        (1, 'John Doe', 28, 'Male', 90000.0),
        (2, 'Jane Doe', 25, 'Female', 75000.0),
        (3, 'Bob Smith', 32, 'Male', 85000.0),
        (4, 'Alice Johnson', 29, 'Female', 92000.0),
        (5, 'Charlie Brown', 35, 'Male', 78000.0),
    ]

    cursor.executemany('''
        INSERT INTO Customer (CustNo, CustName, Age, Gender, Salary) 
        VALUES (%s, %s, %s, %s, %s)
    ''', customers)

    connection.commit()

# Function to display customer information with Salary above 80,000
def display_above_80000(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Customer WHERE Salary > 80000')
    above_80000_customers = cursor.fetchall()

    print("\nCustomer Information with Salary above 80,000:")
    for customer in above_80000_customers:
        print(customer)

# Function to count male and female customers
def count_gender(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT Gender, COUNT(*) FROM Customer GROUP BY Gender')
    gender_counts = cursor.fetchall()

    print("\nGender Counts:")
    for gender, count in gender_counts:
        print(f"{gender}: {count}")

if __name__ == "__main__":
    # Change the connection details accordingly
    connection = create_connection()

    # Create Customer table
    create_customer_table(connection)

    # Insert values into the Customer table
    insert_customer_data(connection)

    # Display customer information with Salary above 80,000
    display_above_80000(connection)

    # Count male and female customers
    count_gender(connection)

    # Close the connection
    connection.close()
