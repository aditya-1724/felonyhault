import mysql.connector

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host="localhost",      # or your DB host, e.g., "127.0.0.1"
        user="root",  # replace with your MySQL username
        password="adi24niki",  # replace with your MySQL password
        database="project"   # replace with your DB name
        )
    cursor = connection.cursor()

    # Ask user for values to insert
    print("\nEnter values to insert into 'daily_crime_stats' table:")
    id = input("ID: ")
    crime_type = input("Crime Type: ")
    avg_cases_per_day = input("Average case: ")
    major_areas = input("Major Areas: ")

    # Insert query
    insert_query = """
    INSERT INTO daily_crime_stats (id, crime_type, avg_cases_per_day, major_areas)
    VALUES (%s, %s, %s, %s)
    """
    values = (id, crime_type, avg_cases_per_day, major_areas)

    cursor.execute(insert_query, values)
    connection.commit()

    print("\n✅ Data inserted successfully into 'daily_crime_stats'!")

    cursor.execute("SELECT * FROM daily_crime_stats")  
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print("❌ Error:", err)
