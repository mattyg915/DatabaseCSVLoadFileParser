# DatabaseCSVLoadFileParser
A simple python script that I used to parse a CSV file that I needed to load into a database and output a CSV that was ready to load.

It examines the contents of the first column and matches them against the contents of the second. Any value in the second column that matches any value in the first is output to the created file along with the contents of adjacent columns. Currently, the code will only output columns 2 and 3, modification to the write() method is necessary to write additional columns' data.
