[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Database1 Analyzer

VisualText version 1.4 introduces database connectivity functions within NLP++.  The database1 sample analyzer (in VisualText\apps) connects to a database, sends commands to it, retrieves data from it, and prints the results to a file.  Some features:

- Uses the **[interactive](../interactive.md)**() function to alter the behavior of the analyzer when running within VisualText as opposed to standalone

- Uses the **exittopopup**() function within VisualText to have the user type in a command such as "SELECT * FROM sql;".  Then a subsequent pass can grab the type-in using **getpopupdata**().

- Includes an example of fetching every supported database type.  Everything except the various BLOB data types is handled.

- Includes the first use of call-by-reference in NLP++, with the calls to **[dbbindcol](../dbbindcol.md)**().  This is the only built-in function to use call-by-reference at present.  User-defined NLP++ functions cannot take advantage of call-by-reference yet.

- Includes a standalone executable version of the analyzer.  Can be run with: **c:\apps\database1\Release\database1.exe input\misc\xxx.txt**

To set up the precise example within this analyzer, you will first need to install a database.  We recommend downloading MySQL and MyODBC and configuring them as described at their respective web sites.  Copy the database1 folder from samples to c:\apps.  Then set up an ODBC connection to a database called test (making sure to match the account information to that in c:\apps\database1\data\createdb).  Then one can run a command such as

c:\mysql\bin\mysql test < c:\apps\database1\data\createdb

in order to create the same "test" database tables and values as used in the database1 analyzer.

The two pass files within the database1 analyzer contain further notes regarding this application.
