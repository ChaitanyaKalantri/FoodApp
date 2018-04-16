#!/usr/bin/python
import MySQLdb
import sys
sys.path.insert(0, "/Users/chaitanyakalantri/Desktop/Zappos Data Science/ZapposFoodApp")
from createdb import createdatabase, dropdb

def testcreatedb():
    connection = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
    try:
        dropdb()
    except:
        pass
    try:
        with connection.cursor as c:
            c.execute("show tables")
            assert c.fetchall()[0][0] == None
    except:
        pass
    
    createdatabase()
    
    try:
        with connection.cursor as c:
            c.execute("show tables")
            assert c.fetchall()[0][0] != None
    except:
        pass
    dropdb()

def testdropdb():
    connection = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
    createdatabase()

    try:
        with connection.cursor as c:
            c.execute("show tables")
            assert c.fetchall()[0][0] != None
    except:
        pass
    
    dropdb()
    
    try:
        with connection.cursor as c:
            c.execute("show tables")
            assert c.fetchall()[0][0] == None
    except:
        pass



if __name__ == "__main__":
    testcreatedb()

    testdropdb()

