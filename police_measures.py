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
    print("\nEnter values to insert into 'police_measures' table:")
    id_val = input("ID: ")
    measure_type = input("Measure Type: ")
    description = input("Description: ")
    targeted_areas = input("Targeted Areas: ")

    # Insert query
    insert_query = """
    INSERT INTO police_measures (id, measure_type, description, targeted_areas)
    VALUES (%s, %s, %s, %s)
    """
    values = (id_val, measure_type, description, targeted_areas)

    cursor.execute(insert_query, values)
    connection.commit()

    print("\n✅ Data inserted successfully into 'police_measures'!")

    cursor.execute("SELECT * FROM police_measures")  
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print("❌ Error:", err)
