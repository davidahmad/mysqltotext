# mysqltotext
### This script will convert one or more MYSQL queries to a text file in tab delimited format.

This script is intended to be used on Windows but will also work on Unix/Linux.<br/>
This script is written in Python 2.7 and uses the MySQLdb interface for connecting to a MYSQL database.<br/>

### Purpose
As an Engineer working with data, I always find myself enhancing the ETL process. This small script is quite useful during the transforming and loading steps. There are times when a table or combined parts of multiple tables need to be extracted and saved in a tab delimited text file. This text file can then be loaded to another database or used by another script in your ETL process. <br/>
All that's needed is the definition for your MYSQL connection, the definition of where to save files, and the query you wish to have saved as a text file.<br/>


The generated text file can be opened in Excel for an easily readable view of your mysql query (or queries).<br/>

### You will need to install the MySQLdb interface in order to use this script. <br/>
MySQLdb is an api for accessing MySQL databases using python. It is built on top of the MySQL C API.<br/>

### Download and install the MySQLdb interface for Windows here:<br/>
https://sourceforge.net/projects/mysql-python/
