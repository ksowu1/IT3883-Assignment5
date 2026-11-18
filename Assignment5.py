# Program Name: Assignment5.py
# Course: IT3883/Section w05
# Student Name: Komi Sowu
# Assignment Number: Assignment 5
# Due Date: 11/20/2026
# Purpose: This program reads temperature data from a text file and stores
#          the data in a SQLite database and then uses SQL commands to
#          calculate and display the average temperatures for Sunday
#          and Thursday.
# Resources Used: Course materials, Python documentation, and class notes.


import sqlite3


# Connect to the database
# The database will be created if it does not already exist
connection = sqlite3.connect("Assignment5.db")

# Create a cursor to execute SQL commands
cursor = connection.cursor()


# Remove the old table if the program was run before
cursor.execute("DROP TABLE IF EXISTS Temperatures")


# Create the temperature table
cursor.execute("""
CREATE TABLE Temperatures (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Day_Of_Week TEXT,
    Temperature_Value REAL
)
""")


# Open and read the input file
with open("DownloadAttachment.txt", "r") as input_file:

    for line in input_file:

        # Separate the day and temperature
        data = line.split()

        day = data[0]
        temperature = float(data[1])

        # Insert the data into the database
        cursor.execute("INSERT INTO Temperatures (Day_Of_Week, Temperature_Value) VALUES (?, ?)",(day, temperature))

# Save the data that was inserted into the database
connection.commit()

# Calculate the average temperature:
# Sunday
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM Temperatures
WHERE Day_Of_Week = 'Sunday'
""")

sunday_average = cursor.fetchone()[0]

# Thursday
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM Temperatures
WHERE Day_Of_Week = 'Thursday'
""")

thursday_average = cursor.fetchone()[0]

# Display Sunday and Thurday average
print(f"Sunday Average Temperature: {sunday_average:.2f}")
print(f"Thursday Average Temperature: {thursday_average:.2f}")

# Close the database connection
connection.close()


