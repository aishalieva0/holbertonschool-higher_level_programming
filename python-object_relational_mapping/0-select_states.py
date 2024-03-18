#!/usr/bin/python3
import MySQLdb
import sys


def main():
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    db = MySQLdb.connect(user=u, passwd=p, db=d, host='localhost', port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")

    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
