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
    print("\nEnter values to insert into 'crime_hotspots' table:")
    id = input("ID: ")
    area_name = input("Area Name: ")
    zone = input("Zone: ")
    common_crimes = input("Common crimes: ")
    peak_hours=input("Peak hours:")
    reason_for_hotspot=input("reason_for_hotspot:")

    # Insert query
    insert_query = """
    INSERT INTO crime_hotspots (id, area_name, zone, common_crimes, peak_hours, reason_for_hotspot)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (id, area_name, zone, common_crimes, peak_hours, reason_for_hotspot)

    cursor.execute(insert_query, values)
    connection.commit()

    print("\n✅ Data inserted successfully into 'crime_hotspots'!")

    cursor.execute("SELECT * FROM crime_hotspots")  
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print("❌ Error:", err)
