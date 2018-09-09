#!/usr/bin/python
import MySQLdb

def createdatabase():
    db = MySQLdb.connect(host="localhost", user="root",  db="pythonspot", password= "Chetu@123")   # name of the database
    # Create a Cursor object to execute queries.
    curr = db.cursor()

    # create the restaurant table
    TABLES = {}
    TABLES['Restaurant'] = (
        "CREATE TABLE IF NOT EXISTS `Restaurant` ("
        "  `restaurant_id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `name` varchar(20) ,"
        "  `street` varchar(20) ,"
        "  `city` varchar(20) ,"
        "  `state` varchar(20) ,"
        "  PRIMARY KEY (`restaurant_id`)"
        ")")

    # create the menu table
    TABLES['Menu'] = (
        "CREATE TABLE IF NOT EXISTS `Menu` ("
        "  `menu_id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `restaurant_id` int(11) ,"
        "  `category` varchar(20) ,"
        "  PRIMARY KEY (`menu_id`)"
    #    "  FORIENGE KEY(`restaurant_id`) references Restaurant(`restaurant_id`) ,"
        ") ")

    # create the menuItems table
    TABLES['MenuItems'] = (
        "CREATE TABLE IF NOT EXISTS `MenuItems` ("
        "  `menu_id` int(11) NOT NULL,"
        "  `category` varchar(20) ,"
        "  `item_name` varchar(20) ,"
        "  `cuisine` varchar(20)"
    #    "  FORIENGE KEY(`menu_id`) references Menu(`menu_id`) ,"
        ")")

    # create the OrderItem table
    TABLES['OrderItem'] = (
        "CREATE TABLE IF NOT EXISTS `OrderItem` ("
        "  `order_id` int(11) NOT NULL,"
        "  `item_name` varchar(20) "
    #    "  FORIENGE KEY(`menu_id`) references Menu(`menu_id`) ,"
        ")")

    # create the Login table
    TABLES['Login'] = (
        "CREATE TABLE IF NOT EXISTS `Login` ("
        "  `id` int(5) NOT NULL AUTO_INCREMENT,"
        "  `name` varchar(15), "
        " `password` varchar(20) NOT NULL,"
        "  PRIMARY KEY (`id`)"
    #    "  FORIENGE KEY(`menu_id`) references Menu(`menu_id`) ,"
        ")")

    for name, ddl in TABLES.items():
        print("Creating table {}: ".format(name))
        curr.execute(ddl)


    # Insert values in the restaurant table
    curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (1, "Kailash", "HealthScience25", "Stony Brook", "New York"))
    curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (2, "CurryClub", "HealthScience25", "Stony Brook", "New York"))
    curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (3, "Panera", "HealthScience25", "Stony Brook", "New York"))
    curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (4, "Sweet", "HealthScience25", "Stony Brook", "New York"))
    curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (5, "Dominos", "HealthScience25", "Stony Brook", "New York"))
    curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (6, "Cutlet", "HealthScience25", "Stony Brook", "New York"))
    curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (7, "Mexican Club", "HealthScience25", "Stony Brook", "New York"))
    curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (8, "Natures Food", "HealthScience25", "Stony Brook", "New York"))

    # Insert values in the menu table
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (1, 1, "Breakfast"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (2, 1, "Lunch"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (3, 1, "Dinner"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (4, 2, "Breakfast"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (5, 2, "Lunch"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (6, 2, "Dinner"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (7, 3, "Breakfast"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (8, 3, "Lunch"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (9, 3, "Dinner"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (10, 4, "Breakfast"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (11, 4, "Lunch"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (12, 4, "Dinner"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (13, 5, "Breakfast"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (14, 5, "Lunch"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (15, 5, "Dinner"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (16, 6, "Breakfast"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (17, 6, "Lunch"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (18, 6, "Dinner"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (19, 7, "Breakfast"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (20, 7, "Lunch"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (21, 7, "Dinner"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (22, 8, "Breakfast"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (23, 8, "Lunch"))
    curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (24, 8, "Dinner"))

    # Insert values in the menuItems table
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (1, "Breakfast", "Idli", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (1, "Breakfast", "Poha", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (2, "Lunch", "Chicken", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (3, "Dinner", "Roti", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (3, "Dinner", "Pizza", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (3, "Dinner", "Paneer", "Indian"))

    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (4, "Breakfast", "Bread", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (4, "Breakfast", "Jam", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (4, "Breakfast", "Butter", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (5, "Lunch", "Turkey", "Mexican"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (5, "Lunch", "Becon", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (5, "Lunch", "Chicken", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (6, "Lunch", "Chicken", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (6, "Dinner", "Roti", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (6, "Dinner", "Pizza", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (6, "Dinner", "Paneer", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (6, "Dinner", "ChickenCurry", "American"))

    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (7, "Breakfast", "Dosa", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (7, "Breakfast", "Samosa", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (8, "Lunch", "Begal", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (8, "Lunch", "Roti", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (8, "Lunch", "Maggi", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (9, "Dinner", "Pasta", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (9, "Dinner", "Beens", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (9, "Dinner", "Paratha", "Indian"))

    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (10, "Breakfast", "Bun", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (10, "Breakfast", "Milk", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (10, "Breakfast", "Egg", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (11, "Lunch", "Nan", "Mexican"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (11, "Lunch", "Ham", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (11, "Lunch", "Burger", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (11, "Lunch", "Chicken", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (12, "Dinner", "Roti", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (12, "Dinner", "Paratha", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (12, "Dinner", "Kulcha", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (12, "Dinner", "Sausage", "American"))


    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (13, "Breakfast", "Bun", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (13, "Breakfast", "Milk", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (13, "Breakfast", "Egg", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (14, "Lunch", "Nan", "Mexican"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (14, "Lunch", "Ham", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (14, "Lunch", "Burger", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (14, "Lunch", "Chicken", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (15, "Dinner", "Roti", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (15, "Dinner", "Paratha", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (15, "Dinner", "Kulcha", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (15, "Dinner", "Sausage", "American"))


    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (16, "Breakfast", "Sausage", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (16, "Breakfast", "Cereals", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (16, "Breakfast", "Egg", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (17, "Lunch", "Idli", "Mexican"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (17, "Lunch", "Paratha", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (17, "Lunch", "Maggi", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (17, "Lunch", "Chicken", "Italian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (18, "Dinner", "Roti", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (18, "Dinner", "Paneer", "American"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (18, "Dinner", "Kulcha", "Indian"))
    curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (18, "Dinner", "Sausage", "American"))

    # Insert values in the Login table
    curr.execute (" insert into Login VALUES ( %s, %s, %s)", (1, "Zappos", "Family"))


    # Display all the restaurant, menu & menuItems tables items; just for verification that the complete code is working properly
    curr.execute("SELECT * FROM Restaurant")
    for row in curr.fetchall() :
        print(row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4])
        
    curr.execute("SELECT * FROM Menu")
    for row in curr.fetchall() :
    	print(row[0], " ", row[1], " ", row[2])


    curr.execute("SELECT * FROM MenuItems")
    for row in curr.fetchall() :
        print(row[0], " ", row[1], " ", row[2], " ", row[3])

    #Finally commit to save the changes and close the connection
    db.commit() 
    curr.close()

def dropdb():
    db = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")   # name of the database
     
    # Create a Cursor object to execute queries.
    curr = db.cursor()
    curr.execute("drop table Restaurant")
    curr.execute("drop table Menu")
    curr.execute("drop table MenuItems")
    curr.execute("drop table OrderItem")
    curr.execute("drop table Login")

    db.commit() 
    curr.close()


if __name__ == "__main__":
    createdatabase()
