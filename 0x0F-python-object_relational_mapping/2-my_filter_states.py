#!/usr/bin/python3
"""
   script that takes in an argument and displays all values in the table
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2],
                         db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name= '{}'\
        ORDER BY id ASC".format(argv[4]))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
