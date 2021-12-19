#!/usr/bin/python3
"""
   script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], password=argv[2],
                         db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name\
        FROM cities INNER JOIN states\
        ON cities.state_id= states.id ORDER BY cities.id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
