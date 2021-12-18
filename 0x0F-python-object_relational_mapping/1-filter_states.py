#!/usr/bin/python3
"""
   script that lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2],
                         db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
