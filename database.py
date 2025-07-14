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

##============================================================
## SQLITE DATABASE INITIATION
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
        connection.execute(assetData, (order_ID, worksite_type, worksite_address, worksite_city, worksite_zip))

def addAssignment():
    pass

def updateEntity():
    pass

def deleteEntity():
    pass

def viewAssets():
    pass

def viewWorksites():
    pass