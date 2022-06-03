import psycopg2

try:
    conn=psycopg2.connect(dbname='postgres', user='wasd64', password='', host='localhost')
    conn.close()
    print("True")
except:
    print("False")