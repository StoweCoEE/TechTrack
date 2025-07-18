import sqlite3

##============================================================
## SQLITE STATEMENT VARIABLES
##

assetTableCreation = """CREATE TABLE IF NOT EXISTS asset(
               asset_ID INTEGER PRIMARY KEY,
               asset_type INTEGER,
               asset_name TEXT,
               asset_cost INTEGER,
               asset_purchase_date INTEGER,
               asset_model_no INTEGER);"""

worksiteTableCreation = """CREATE TABLE IF NOT EXISTS worksite(
               worksite_ID INTEGER PRIMARY KEY,
               order_ID INTEGER,
               worksite_type INTEGER,
               worksite_address TEXT,
               worksite_city TEXT,
               worksite_zip INTEGER);"""

assignmentTableCreation = """CREATE TABLE IF NOT EXISTS assignment(
               assignment_ID INTEGER PRIMARY KEY,
               asset_ID INTEGER,
               worksite_ID INTEGER,
               FOREIGN KEY(asset_ID) REFERENCES asset(asset_ID)
               FOREIGN KEY(worksite_ID) REFERENCES worksite(worksite_ID));"""

assetData = "INSERT INTO asset(asset_type, asset_name, asset_cost, asset_purchase_date, asset_model_no) VALUES (?,?,?,?,?);"

worksiteData = "INSERT INTO worksite(order_ID, worksite_type, worksite_address, worksite_city, worksite_zip) VALUES (?,?,?,?,?);"

deleteAssetData = "DELETE from asset WHERE asset_ID = ?;"

deleteWorksiteData = "DELETE from worksite WHERE worksite_ID = ?;"

viewOneAssetData = "SELECT * FROM asset WHERE asset_ID = ?;"

viewOneWorksiteData = "SELECT * FROM worksite WHERE worksite_ID = ?;"

viewAllAssetData = "SELECT * FROM asset"

viewAllWorksiteData = "SELECT * FROM worksite"

assignmentData = "INSERT INTO assignment(asset_ID, worksite_ID) VALUES (?,?);"

##============================================================
## SQLITE DATABASE CONNECTION AND INITIATION FUNCTIONS
##

def connect():
    return sqlite3.connect('TechTrackDB.db')

def initialize(connection):
    with connection:
        connection.execute(assetTableCreation)
        connection.execute(worksiteTableCreation)
        connection.execute(assignmentTableCreation)

##============================================================
## SQLite Functions
##

def addAsset(connection, asset_type, asset_name, asset_cost, asset_purchase_date, asset_model_no):
    with connection:
        connection.execute(assetData, (asset_type, asset_name, asset_cost, asset_purchase_date, asset_model_no))

def addWorksite(connection, order_ID, worksite_type, worksite_address, worksite_city, worksite_zip):
    with connection:
        connection.execute(worksiteData, (order_ID, worksite_type, worksite_address, worksite_city, worksite_zip))

def addAssignment(connection, asset_ID, worksite_ID):
    with connection:
        connection.execute(assignmentData, (asset_ID, worksite_ID))

def deleteAsset(connection, asset_ID):
    with connection:
        connection.execute(deleteAssetData, (asset_ID,))

def deleteWorksite(connection, worksite_ID):
    with connection:
        connection.execute(deleteWorksiteData, (worksite_ID,))

def updateAsset(connection, asset_ID, asset_type, asset_name, asset_cost, asset_purchase_date, asset_model_no):
    pass

def updateWorksite(connection, worksite_ID, order_ID, worksite_type, worksite_address, worksite_city, worksite_zip):
    pass

def viewOneAsset(connection, asset_ID):
    with connection:
        return connection.execute(viewOneAssetData, (asset_ID,)).fetchone()

def viewOneWorksite(connection, worksite_ID):
    with connection:
        return connection.execute(viewOneWorksiteData, (worksite_ID,)).fetchone()

def viewAllAssets(connection):
    with connection:
        return connection.execute(viewAllAssetData).fetchall()

def viewAllWorksites(connection):
    with connection:
        return connection.execute(viewAllWorksiteData).fetchall()