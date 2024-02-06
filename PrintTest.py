import mysql.connector
import os
import time

host = "localhost"
user = "root"
password = "MDBPass9517"
database = "carservice"

garageID = []
garageName = []
address = []
town = []
postcode = []
phoneNo = []

try:

    connection = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )

    if connection.is_connected():
        print("connected to the database")
        # to run the query we need cursor
        cursor = connection.cursor()

        # read the records from table
        query = "select * from garage"

        cursor.execute(query)

        data = cursor.fetchall()

        # add the result of query in the lists
        rowCount = 0
        for row in data:
            rowCount = rowCount + 1
            garageID.append(row[0])
            garageName.append(row[1])
            address.append(row[2])
            town.append(row[3])
            postcode.append(row[4])
            phoneNo.append(row[5])

        # print the lists
    decision = ""
    counter = 0
    while decision != "Cancel":
        print(garageID[counter])
        print(garageName[counter])
        print(address[counter])
        print(town[counter])
        print(postcode[counter])
        print(phoneNo[counter])
        print("")
        print("Page - " + str(counter + 1))
        print("")
        print("Next // Cancel")
        print("")
        decision = input()

        if decision == "Next":
            counter = counter + 1
            for i in range(0, (rowCount + 5)):
                print("\033[A                             \033[A")

        if counter >= rowCount:
            print("End of Table")
            print("Returning to Page 1...")
            counter = 0
            time.sleep(5)
            print("\033[A                             \033[A")
            print("\033[A                             \033[A")


except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB: {e}")

finally:
    # close the database connection at the end
    if "connection" in locals() and connection.is_connected():
        connection.close()
        print("the connection is closed")
