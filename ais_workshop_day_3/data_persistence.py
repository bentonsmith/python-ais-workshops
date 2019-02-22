'''
################################
# Data Persistence with Python #
################################
'''
'''

REVIEW:
 * We can utilize local data persistence using the following
    1) Raw Text-Bsaed Files (TXT, CSV, JSON, XML) 
    2) Pickle 
    3) Shelve 

 * In addition to these, Python includes a local relational database in the Python Standard Library (sqlite3)

 * Local storage is great, it allows us to persist data between reboots, power outages, and application restarts.
 * However, if multiple applications need access to our data, we may want to consider a full blown database
   application. Usually stored on a separate server.

* PROS of LOCAL
-----------------------
    * Faster
    * Easier (No maintenance of a 3rd party application)

* CONS of LOCAL
-----------------------
    * Unable to access from multiple applications
    * Not as robust (Think of all the advantages SQL Server provides)
'''

########################
# Connecting to a DBMS #
########################
'''
A great starting point: https://wiki.python.org/moin/DatabaseProgramming

Python makes it simple with: DB API v2.0 (PEP 249) - A Guide for accessing databases with Python

* PEP 249 (Python Enhancement Proposals) >>> https://www.python.org/dev/peps/pep-0249/
    * This PEP encourages similarity between all Python Modules used to access databases.
    * This makes the process of swapping out databases much easier.
    * Consistent access methods for all databases.
    
* Any type of database will follow a generic interface
    * https://wiki.python.org/moin/DatabaseInterfaces    

* ODBC - Open Database Connectivity
    -> https://wiki.python.org/moin/ODBC
    -> Many provide DB API 2.0 Drivers (For ODBC Compliant Databases)
    -> pyodbc is a good one for Microsoft SQL Server, obviously debatable that it is the "best".

* ORM - Object Relational Mapper
    -> Maps objects to relational db model
    -> SQLAlchemy is very popular ORM in the Python community
    https://wiki.python.org/moin/HigherLevelDatabaseProgramming
'''