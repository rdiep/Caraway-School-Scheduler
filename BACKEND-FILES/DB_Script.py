#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#--------------------------------DB_SCRIPT.PY-----------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#
# THIS IS A LIBRARY THAT YOU CAN USE BY ADDING THE LINE
# import DB_Script.py
# TO THE TOP OF YOUR PYTHON FILE, GIVEN IT IS IN THE SAME DIRECTORY.
#
#-------------------------------------------------------------------------------
#FUNCTIONS IN THIS LIBRARY:
#-------------------------------------------------------------------------------
#test() - creates the tables, the DB, and adds the test data to the login table
#         for Raymond's testing
#addToUserTableTestData() - enters test data to the LOGIN table
#initDB() - initializes the database and creates all the main tables
#startDB() - creates the database file and initializes the cursor variable
#closeConnection() - closes the database
#mkEmptyMonthTable(month,year) - makes an empty month table given the name of
#                                the month and the year of the month
#createUserPassTable() - makes an empty "UserPass" table with the columns ID,
#                        username, password, and type
#createUsersTable() - makes an empty table with the columns ID, username,
#                     firstname, lastname, and facilitator-child
#createHoursTable() - creates an empty table with the columns ID, username, 
#                     facilitator child-num, needed-hours-week,
#                     total-hours-lifetime, total-hours-monthly, and 
#                     total-hours-weekly.
#checkValid(username,password) - returns account type iff valid, otherwise false
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# IMPORTS & GLOBAL VAR DECLARATIONS
#-------------------------------------------------------------------------------
import sqlite3 #Type "sqlite3.version" into python shell to ensure 
               #that sqlite3 working (no install necessary)
import datetime

global DB
global cursor

#-------------------------------------------------------------------------------
# FUNCTIONS
#-------------------------------------------------------------------------------

def test():
    initDB()
    addToUserTableTestData()
    closeConnection()
    return

#Author: Lukas
#Purpose: To execute all of the functions to create the DB and populate it with
#         the empty tables with the appropriate columns
#Parameters: None
#Return Value: 0 (Placeholder int)
#Side effects: DataBase.db is created in dir data
def initDB():
    startDB()
    months = ['January','February','March','April','May','June','July',\
              'August','September','October','November','December']
    now = datetime.datetime.now()
    mkEmptyMonthTable(months[(now.month)-1],now.year)
    createUserPassTable()
    createUsersTable()
    createHoursTable()
    return 0

#Author: Lukas
#Purpose: To initialize the SQLite embedded DB
#Parameters: None
#Return Value: 0 (Placeholder int)
def startDB():
    #DB = sqlite3.connect(':memory:') #Creates temporary database with RAM
    DB = sqlite3.connect('data/DataBase.db') #Creates file where SQLite DB is stored
    cursor = DB.cursor()
    return 0

#Author: Lukas
#Purpose: To close the connection to the SQLite DB
#Parameters: None
#Return Value: 0 (Placeholder int)
def closeConnection():
    DB.close()
    return 0

#-------------------------------------------------------------------------------
# TABLE CREATION FUNCTIONS
#-------------------------------------------------------------------------------

#Author: Lukas
#Purpose: To create a new empty table representing a month in the SQLite DB
#Paramters: month: str value representing month name, e.g. "March"
#           year: int value representing the year of the month being created
#Return Value: 0 (Placeholder int)
def mkEmptyMonthTable(month,year):
    with con:
        cur = con.cursor()    
    leapYear=0 #Set leapYear to 0 (False) by default
    if(month=="February"):
        #Determine if this is a leap year and if so set leapYear to 1 (True)
        if( (year%4==0) and (year%100==0) and (year%400==0) ):
            leapYear=1
    # Case where month being added is 31 days long
    if(month=="January" or month=="March" or month=="May" or month=="July"\
       or month=="August" or month=="October" or month=="December"):
        cur.execute('''CREATE TABLE {tn}(ID INTEGER PRIMARY KEY,1  TEXT 2 TEXT\
        3 TEXT 4 TEXT 5 TEXT 6 TEXT 7 TEXT 8 TEXT 9 TEXT 10 TEXT 11 TEXT 12 TEXT\
        13 TEXT 14 TEXT 15 TEXT 16 TEXT 17 TEXT 18 TEXT 19 TEXT 20 TEXT 21 TEXT\
        22 TEXT 23 TEXT 24 TEXT 25 TEXT 26 TEXT 27 TEXT 28 TEXT 29 TEXT 30 TEXT\
        31 TEXT'''.format(tn=month))
    # Case where month being added is 30 days long
    if(month=="April" or month=="June" or month=="September" or month=="November"):
        cur.execute('''CREATE TABLE {tn}(ID INTEGER PRIMARY KEY, 1 TEXT 2 TEXT\
        3 TEXT 4 TEXT 5 TEXT 6 TEXT 7 TEXT 8 TEXT 9 TEXT 10 TEXT 11 TEXT 12 TEXT\
        13 TEXT 14 TEXT 15 TEXT 16 TEXT 17 TEXT 18 TEXT 19 TEXT 20 TEXT 21 TEXT\
        22 TEXT 23 TEXT 24 TEXT 25 TEXT 26 TEXT 27 TEXT 28 TEXT 29 TEXT 30 TEXT\
        '''.format(tn=month))
    # Pesky February case
    if(month=="February"):
        # If leap year, february has 29 days
        if(leapYear==1):
            cur.execute('''CREATE TABLE {tn}(ID INTEGER PRIMARY KEY, 1 TEXT 2 TEXT\
            3 TEXT 4 TEXT 5 TEXT 6 TEXT 7 TEXT 8 TEXT 9 TEXT 10 TEXT 11 TEXT 12 TEXT\
            13 TEXT 14 TEXT 15 TEXT 16 TEXT 17 TEXT 18 TEXT 19 TEXT 20 TEXT 21 TEXT\
            22 TEXT 23 TEXT 24 TEXT 25 TEXT 26 TEXT 27 TEXT 28 TEXT 29 TEXT'''.format(tn=month))
        # If not a leap year, february has 28 days
        elif(leapYear==0):
            cur.execute('''CREATE TABLE {tn}(ID INTEGER PRIMARY KEY, 1 TEXT 2 TEXT\
            3 TEXT 4 TEXT 5 TEXT 6 TEXT 7 TEXT 8 TEXT 9 TEXT 10 TEXT 11 TEXT 12 TEXT\
            13 TEXT 14 TEXT 15 TEXT 16 TEXT 17 TEXT 18 TEXT 19 TEXT 20 TEXT 21 TEXT\
            22 TEXT 23 TEXT 24 TEXT 25 TEXT 26 TEXT 27 TEXT 28 TEXT'''.format(tn=month))
    DB.commit()
    return 0

#Author: Lukas
#Purpose: To Create the ID/Username/Password/Type relation table (LOGIN)
#Parameters: None
#Return Value: None
def createUserPassTable():
    cur.execute('''CREATE TABLE {td}(ID INTEGER PRIMARY KEY, USERNAME TEXT, \
    PASSWORD TEXT TYPE TEXT'''.format(td=login))
    DB.commit()
    return 0

#Author: Lukas
#Purpose: To Create the ID/Username/Firstname/LastName/Facilitator-Child table (USERS)
#Parameters: None
#Return Value: 0 (placeholder int)
def createUsersTable():
    cur.execute('''CREATE TABLE {td}(ID INTEGER PRIMARY KEY, USERNAME TEXT, \
    FIRSTNAME TEXT LASTNAME TEXT FACILITATOR-CHILD TEXT'''.format(td=users))
    DB.commit()
    return 0

def createHoursTable():
    cur.execute('''CREATE TABLE {td}(ID INTEGER PRIMARY KEY, USERNAME TEXT\
    FACILITATOR INTEGER, CHILD-NUM INTEGER, NEEDED-HOURS-WEEK INTEGER,TOTAL-HOURS-LIFETIME \
    INTEGER, TOTAL-HOURS-MONTHLY INTEGER, TOTAL-HOURS-WEEKLY INTEGER'''.format(td=hours))
    DB.commit()
    return 0

#-------------------------------------------------------------------------------
# END OF TABLE CREATION FUNCTIONS
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# DATA ENTRY FUNCTIONS
#-------------------------------------------------------------------------------

#Author: Lukas
#Purpose: To insert data insto the database
#Parameters: TBA
#Return Value: None
def insertField(tableName,colName,colValue):
    cursor.execute('''INSERT INTO {tableName}({colName}) VALUES({colValue})'''\
                   .format(tableName=tableName,colName=colName,colValue=colValue))
    DB.commit()
    return 0

#Author: Lukas
#Purpose: To insert a ID/Username/Password/Type entry to the LOGIN table
#Parameters:
#Return Value: None
def addToUserTableTestData():
    try:
        cursor.execute('''INSERT INTO login(ID,Username,Password,Type) VALUES (1,\
        'user','12345','Admin')''')
    except sqlite3.IntegrityError:
        print('There was an error inserting into login table.')
    return
    

#-------------------------------------------------------------------------------
# DATA RETURN FUNCTIONS
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# OTHER FUNCTIONS
#-------------------------------------------------------------------------------

#Author:      Lukas
#Purpose:    To query the database and see if the username/password pair matches
#             a pair already in the database, and iff it is, returns the account
#             type, otherwise, returns null.
#Parameters:   username: string representing user entered username
#              password: string representing user entered password
#Return Value: None

def checkValid(username,password):
    valid = False # Default is false
    cursor.execute("SELECT * FROM login")
    entries = cursor.fetchall()
    for entry in entries:
        if(entry[1]==username and entry[2]==password):
            return (entry[3]) # return account type
    return False

#Author: Lukas
#Purpose: To delete a table in the DB - this function is for reference, as a 
#         specific table name has to be used in order to drop the table.
#Parameters: str tableName - name of table to delete
#Return Value: 0 (Placeholder int)

def delTable(tableName):
    cursor.execute('''DROP TABLE {td}'''.format(td=tableName))
    DB.commit()
    return 0
#-------------------------------------------------------------------------------