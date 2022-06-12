import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="operaciones"
    )

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE Operation (description VARCHAR(50) PRIMARY KEY, category VARCHAR(50), amount FLOAT(10))")
# mycursor.execute("INSERT INTO Operation (description, category, amount) VALUES (%s, %s, %s)", ("GTA V", "Game", 2000.00))
# db.commit()

# mycursor.execute("SELECT * FROM Operation")

searched = input("What do you want to delete (description)? ")
searchedObj = mycursor.execute("SELECT * FROM Operation WHERE description = %s", (searched,))
row = mycursor.fetchone()
if row is not None:
    print("The following operation will be deleted: ")
    print(" ----------------------- ")
    print("|",row,"|")
    print(" ----------------------- ")
    mycursor.execute("DELETE FROM Operation WHERE description = %s", (searched,))
    db.commit()
    print("Operation deleted")
else:
    print("Operation not found")

