import pymysql

def connect_e():
    db=pymysql.connect("localhost","root","Culacapu07","soh")
    cursor=db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS am(username TEXT, password TEXT, shopname TEXT, mobile TEXT, email TEXT, aadhar TEXT)")
    db.commit()
    print("CONNECTED")
    db.close()
    
def search(a,b):
    db=pymysql.connect("localhost","root","Culacapu07","soh")
    cursor=db.cursor()
    s=cursor.execute("select shopname from am where username='%s' and password='%s'"%(a,b))
    return s

def connect_s():
    db=pymysql.connect("localhost","root","Culacapu07","soh")
    cursor=db.cursor()
    cursor.execute("CREATE TABLE scoops(flavourname TEXT, price INTEGER")
    db.commit()
    db.close()


def insert(a,b,c,d,e,f):
    db=pymysql.connect("localhost","root","Culacapu07","soh")
    cursor=db.cursor()
    cursor.execute("INSERT INTO am VALUES ('%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f))
    db.commit()   
    db.close()
    
def insert_c(a,b):
    db=pymysql.connect("localhost","root","Culacapu07","soh")
    cursor=db.cursor()
    cursor.execute("INSERT INTO employeedetail VALUES (NULL,'%s','%s')"%(a,b))
    db.commit()   
    db.close()
    


def insert_s(a,b):
    db=pymysql.connect("localhost","root","Culacapu07","soh")
    cursor=db.cursor()
    cursor.execute("INSERT INTO scoops VALUES ('%s','%d')"%(a,b))
    db.commit()   
    db.close()

def delete(fn):
    conn=pymysql.connect("localhost","root","Culacapu07","soh")
    cur=conn.cursor()
    cur.execute("DELETE FROM scoops WHERE flavourname='%s'"%(fn))
    conn.commit()
    conn.close()

def update(p,f):
    conn=pymysql.connect("localhost","root","Culacapu07","soh")
    cur=conn.cursor()
    cur.execute("UPDATE scoops SET price='%d' WHERE flavourname='%s'"%(p,f))
    conn.commit()
    conn.close()


def view():
    conn=pymysql.connect("localhost","root","Culacapu07","soh")
    cur=conn.cursor()
    cur.execute("SELECT * FROM scoops")
    rows=cur.fetchall()
    conn.close()
    return rows


