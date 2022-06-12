import os
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="operaciones"
    )

mycursor = db.cursor()

clear = lambda: os.system('cls')

def add():
    rta = 'y'
    while(rta == "y"):
        clear()
        money = float(input("How much money did it cost? "))
        category = input("What category is it in? ")
        description = input("What is the description? ")

        mycursor.execute("INSERT INTO Operation (amount, category, description) VALUES (%s, %s, %s)", (money, category, description))
        db.commit()
        print("Operation added")

        rta = input("Do you want to add another operation? (y/n)")

def view():
    mycursor.execute("SELECT * FROM Operation")
    for operation in mycursor:
        print(" ----------------------- ")
        print("|",operation,"|")
        print(" ----------------------- ")

    mycursor.execute("SELECT SUM(amount) FROM Operation")
    print("Total amount: ", mycursor.fetchone()[0])

    
def edit():
    searched = input("What do you want to edit (description)? ")
    mycursor.execute("SELECT * FROM Operation WHERE description = %s", (searched,))
    row = mycursor.fetchone()
    if row is not None:    
        print("The following operation will be edited: ")
        print(" ----------------------- ")
        print("|",row,"|")
        print(" ----------------------- ")
        newDescription = input("What is the new description? ")
        newCategory = input("What is the new category? ")
        newAmount = float(input("What is the new amount? "))
        mycursor.execute("UPDATE Operation SET description = %s, category = %s, amount = %s WHERE description = %s", (newDescription, newCategory, newAmount, searched))
        db.commit()
    else:
        print("The description doesn't exist")

def delete():
    searched = input("What do you want to delete (description)? ")
    mycursor.execute("SELECT * FROM Operation WHERE description = %s", (searched,))
    row = mycursor.fetchone()
    if row is not None:
        print("The following operation will be deleted: ")
        print(" ----------------------- ")
        print("|",row,"|")
        print(" ----------------------- ")
        rta = input("Are you sure you want to delete it? (y/n) ")
        if rta == "y":
            mycursor.execute("DELETE FROM Operation WHERE description = %s", (searched,))
            db.commit()
            print("Operation deleted")
        else:
            print("Operation not deleted")
    else:
        print("Operation not found")


if __name__ == "__main__":
    clear()
    print("Welcome to the CRUD app")
    print("My name is Boris and I'm a software developer")
    print("I'm here to help you manage your money")
    decision = input("What do you want to do? (a)dd, (v)iew, (e)dit, (d)elete, (q)uit: ")
    while(decision != "q"):
        clear()
        if(decision == "a"):
            add()
        elif(decision == "v"):
            view()    
        elif(decision == "e"):
            edit()
        elif(decision == "d"):
            delete()
        else:
            print("Invalid option")
        decision = input("What do you want to do? (a)dd, (v)iew, (e)dit, (d)elete, (q)uit: ")

            
