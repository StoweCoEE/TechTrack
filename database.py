import sqlite3

##============================================================
## SQLITE STATEMENT VARIABLES
##

assetTableCreation = """CREATE TABLE IF NOT EXISTS asset(
               assetID INTEGER PRIMARY KEY,
               asset_type INTEGER,
               asset_name TEXT,
               asset_cost INTEGER,
               asset_purchase_date INTEGER,
               asset_model_no INTEGER);"""

worksiteTableCreation = """CREATE TABLE IF NOT EXISTS worksite(
               worksiteID INTEGER PRIMARY KEY,
               orderID INTEGER,
               worksite_type INTEGER,
               worksite_address TEXT,
               worksite_city TEXT,
               worksite_zip INTEGER);"""

assignmentTableCreation = """CREATE TABLE IF NOT EXISTS assignment(
               assignmentID INTEGER PRIMARY KEY,
               assetID INTEGER,
               worksiteID INTEGER,
               FOREIGN KEY(assetID) REFERENCES asset(assetID)
               FOREIGN KEY(worksiteID) REFERENCES worksite(worksiteID));"""

assetData = "INSERT INTO asset(asset_type, asset_name, asset_cost, asset_purchase_date, asset_model_no) VALUES (?,?,?,?,?);"

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

def addWorksite():
    pass

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