#!/usr/bin/python3
"""
takes in an argument
displays all values in the states table
where name matches the argument
"""
import sys
import MySQLdb


def main():
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    arg = sys.argv[4]

    db = MySQLdb.connect(user=u, passwd=p, db=d, host='localhost', port=3306)

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(arg)
    cur.execute(query)
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
