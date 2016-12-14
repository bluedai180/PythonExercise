import mysql.connector

def create():
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

def insert():
    cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Dai'])

def update():
    cursor.execute('update user set name = "chen" where name = "Dai"')

def find():
    cursor.execute('select * from user where id = %s', ('2',))
    values = cursor.fetchall()
    print(values)

def delete():
    cursor.execute('delete from user where id = 1')

if __name__ == "__main__":
    conn = mysql.connector.connect(user='root', password='blue', database='test')
    cursor = conn.cursor()
    insert()
    find()
    print(cursor.rowcount)
    cursor.close()
    conn.close()
