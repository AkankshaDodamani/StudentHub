
import sqlite3

def loginchecker(n,p):
    database_connection=sqlite3.connect("studenthub.db")
    database_cursor=database_connection.cursor()
    data = database_cursor.execute("select * from login where rollno = ?  and password =  ?  ",(n,p))
    data=data.fetchone()
    if data is not None:
        database_connection.commit()
        database_connection.close()
        return True
    else:
        return False

    
     



# db_conn = sqlite3.connect('studenthub.db')
# db_cursor = db_conn.cursor()
# data = db_cursor.execute('SELECT * FROM login')
# data1 = data.fetchall()
# print(data1)
# print(data1)
# db_conn.commit()
# db_conn.close




def name(n):
    db_conn = sqlite3.connect('studenthub.db')
    db_cursor = db_conn.cursor()
    data = db_cursor.execute('SELECT name FROM detail WHERE rollno= ? ',(n))
    data = data.fetchone()
    print(data)
    db_conn.commit()
    db_conn.close()
    return data

def phone_number(n):
    db_conn = sqlite3.connect('studenthub.db')
    db_cursor = db_conn.cursor()
    data = db_cursor.execute('SELECT phoneno FROM detail WHERE rollno= ? ',(n))
    data = data.fetchone()
    print(data)
    db_conn.commit()
    db_conn.close()
    return data

def Email (n):
    db_conn = sqlite3.connect('studenthub.db')
    db_cursor = db_conn.cursor()
    data = db_cursor.execute('SELECT email FROM detail WHERE rollno= ? ',(n))
    data = data.fetchone()
    print(data)
    db_conn.commit()
    db_conn.close()
    return data

# def PRN_number(n):
#     db_conn = sqlite3.connect('studenthub.db')
#     db_cursor = db_conn.cursor()
#     data = db_cursor.execute('SELECT rollno FROM detail WHERE rollno= ? ',(n))
#     data = data.fetchone()
#     print(data)
#     db_conn.commit()
#     db_conn.close()
#     return data


def academic_details(n):
    db_conn = sqlite3.connect('studenthub.db')
    db_cursor = db_conn.cursor()
    data = db_cursor.execute('SELECT academic_details FROM result WHERE rollno= ? ',(n))
    data = data.fetchone()
    print(data)
    db_conn.commit()
    db_conn.close()
    return data


def internship_details (n):
    db_conn = sqlite3.connect('studenthub.db')
    db_cursor = db_conn.cursor()
    data = db_cursor.execute('SELECT internship_details FROM internship WHERE rollno= ? ',(n))
    data = data.fetchone()
    print(data)
    db_conn.commit()
    db_conn.close()
    return data

def cocurricular_and_sports (n):
    db_conn = sqlite3.connect('studenthub.db')
    db_cursor = db_conn.cursor()
    data = db_cursor.execute('SELECT cocurricular_and_sports FROM cocurricular_and_sports  WHERE rollno= ? ',(n))
    data = data.fetchone()
    print(data)
    db_conn.commit()
    db_conn.close()
    return data


