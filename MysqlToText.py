#!C:\Python27\python.exe	

___doc___ = """
MysqlToText.py

This script will convert one or more MYSQL queries to a text file in tab delimited format.
You can open the generated text file in Excel so that it's easily readable. 
This script is written in Python 2.7 and uses the MySQLdb interface for connecting to a MYSql database.

"""

import MySQLdb
import sys
import os

# MYSQL Connection parameters----------------------------------------------
MYSQL_DataBase_Server = "Server's IP address or hostname goes here. e.g. 10.1.1.13"
MYSQL_User = "mysql username"
MYSQL_User_Password = "mysql password"
DataBase_Name = "Database to connect to"
# --------------------------------------------------------------------------

# File output location------------------------------------------------------
Output_Directory_Location = "C:/path/to/directory/"
# --------------------------------------------------------------------------

# Connect to Database--------------------------------------------------------
db_connection = MySQLdb.connect(MYSQL_DataBase_Server, MYSQL_User, MYSQL_User_Password, DataBase_Name)

# Cursor Object For Query Execution
cursor = db_connection.cursor()
# ---------------------------------------------------------------------------


# Method for defining MYSQL query1 and file output name.
def query1():

    #output file name
    output_File = "query_output1.txt"

    #query to be produced in output file.
    query = "SELECT * FROM TABLE_NAME;"

    # Write query to output txt file
    GenerateTXTFile(query, output_File)

    return


# Method for defining MYSQL query2 and file output name.
def query2():

    #output file name
    output_File = "query_output2.txt"

    #query to be produced in output file.
    query = "SELECT * FROM TABLE_NAME;"

    # Write query to output txt file
    GenerateTXTFile(query, output_File)

    return

# This method will transform the query into a text file in tab delimited format.
def GenerateTXTFile(query, output_File):

    # Execute query
    cursor.execute(query)

    # fetch all rows of query
    query_output = cursor.fetchall()

    # File to be written to. If file is there, script will overwrite. If file is not there, script will create.
    newfile = open(Output_Directory_Location + output_File, "w")

    # The following for loop will write the fieldnames of the query into the text file.
    # If you do not need the fieldnames then comment the following for loop out.
    field_names = [i[0] for i in cursor.description]
    if field_names:
        for name in field_names:
            newfile.write("%s\t" % str(name))
        newfile.write("\n")

    # If the query returned something then continue.
    if query_output:
        # Write query into .txt file in tab delimited format.
        # query_output gets returned a "list of tuples", so a nested for loop is necessary to properly
        # generate each row in a tab delimited format.
        for row in query_output:
            for rowElements in row:
                # if the values in a row are not blank, then write the value to text file
                if rowElements != None:
                    newfile.write("%s\t" % str(rowElements))

                # if values are blank then write an extra tab.
                else:
                    newfile.write("\t")
            #new line at the end of each row
            newfile.write("\n")
    else:
        print("No Output for query")
        return


# Call query1.
query1()
# Call query2
query2()

# Close Database Connection
db_connection.close()
