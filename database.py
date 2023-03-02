import datetime
import MySQLdb
from flask import session
from datetime import date
from datetime import timedelta
from datetime import datetime


def db_connect():
    _conn = MySQLdb.connect(host="localhost", user='root',password='root', db='qrcode')
    c = _conn.cursor()

    return c, _conn

# .........................Registration Action Start......................................................................
def storedata(name, fname, dob, hno, colony, location, mandal, dist, pin, rta,photo,usersign,authoritysign,ref,vtype,badge,bloodgroup):
    try:
        c, conn = db_connect()
        print("hi")
        today = date.today()
        issue = today.strftime("%d/%m/%Y")
        year =datetime.now()+timedelta(days=1095) #Added 2Years In Current Date
        val = year.strftime("%d/%m/%Y")
        print(val)
        id="0"
        j = c.execute("insert into userdata (id,name,fname,dob,hno,colony,location,mandal,dist,pin,issue,validity,rta,photo,usersign,authoritysign,ref,vtype,badge,bloodgroup) values ('"+id+"','"+name+"','"+fname+"','"+dob+"','"+hno+"','"+colony+"','"+location+"','"+mandal+"','"+dist+"','"+pin+"','"+issue+"','"+val+"','"+rta+"','"+photo+"','"+usersign+"','"+authoritysign+"','"+ref+"','"+vtype+"','"+badge+"','"+bloodgroup+"')")
        conn.commit()
        conn.close()
        return j
    except Exception as e:
        return(str(e))
# .........................Registration Action End........................................................................
#=========================rc data ========================================================================================
def storercdata(regnum, regowner, address, mclass, vclass, mfgdate, fused, bodytype, cnumber, enumber,cc,wbaase,scapacity,uweight,color,tax,hto,photoname,signname):
    try:
        c, conn = db_connect()
        print("hi")
        today = date.today()
        issue = today.strftime("%d/%m/%Y")
        year =datetime.now()+timedelta(days=5475) #Added 15Years In Current Date
        val = year.strftime("%d/%m/%Y")
        print(val)
        id="0"
        j = c.execute("insert into rcdata (id,regno,regowner,address,mclass,vclass,mfgyr,fuelused,bodytype,cnumber,enumber,cc,wbase,scapacity,uweight,colour,regdate,validity,tax,hto,osign,asign) values ('"+id+"','"+regnum+"','"+regowner+"','"+address+"','"+mclass+"','"+vclass+"','"+mfgdate+"','"+fused+"','"+bodytype+"','"+cnumber+"','"+enumber+"','"+cc+"','"+wbaase+"','"+scapacity+"','"+uweight+"','"+color+"','"+issue+"','"+val+"','"+tax+"','"+hto+"','"+photoname+"','"+signname+"')")
        conn.commit()
        conn.close()
        return j
    except Exception as e:
        return(str(e))
def reg(username,password,dob,email,address,mobile):
    try:
        c,conn = db_connect()
        print("user registration")
        print(username,password,dob,email,address,mobile)
        id="0"
        j=c.execute("insert into user (id,username,password,dob,email,address,mobile) values ('"+id+"','"+username+"','"+password+"','"+dob+"','"+email+"','"+address+"','"+mobile+"')")
        conn.commit()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

#=======================================================Login=============================================================
def user_login(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from user where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def admin_login(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from admin where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))
# .........................View Action Start..............................................................................
def vlicences():
    c, conn = db_connect()
    c.execute("select * from userdata")
    result = c.fetchall()
    conn.close()
    return result

def vlicence(id):
    c, conn = db_connect()
    c.execute("select * from userdata where id='"+id+"'")
    result = c.fetchall()
    conn.close()
    return result

def vrc1():
    c, conn = db_connect()
    c.execute("select * from rcdata")
    result = c.fetchall()
    conn.close()
    return result

def vrc(id):
    c, conn = db_connect()
    c.execute("select * from rcdata where id='"+id+"'")
    result = c.fetchall()
    conn.close()
    return result

def users():
    c, conn = db_connect()
    c.execute("select * from user")
    result = c.fetchall()
    conn.close()
    return result
# .........................View Action End...............................................................................

if __name__ == "__main__":
    print(db_connect())
