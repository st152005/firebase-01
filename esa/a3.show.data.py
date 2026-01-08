import pyrebase

fbConfig ={
  "apiKey": "AIzaSyArn0ZhlPLIlOhvDZ4SlOvujTJEvdgnUok",
  "authDomain": "fbprj1a-94757.firebaseapp.com",
  "databaseURL": "https://fbprj1a-94757-default-rtdb.firebaseio.com",
  "projectId": "fbprj1a-94757",
  "storageBucket": "fbprj1a-94757.firebasestorage.app",
  "messagingSenderId": "1094015731404",
  "appId": "1:1094015731404:web:5ed90a28d06c7bad72e469"
}

def str2float(s):
    try:
        return float(s)
    except:
        return 0

print(f"{'eid':<10}{'ename':<10}{'sal':<10}{'hra':<10}{'da':<10}{'pf':<10}{'gpay':<10}{'npay':<10}")

try:
    fb = pyrebase.initialize_app(fbConfig)
    db = fb.database()
    rows = db.get()
    for row in rows.each():
        dic=row.val()
        rno=row.key()
        ename=dic['ename']
        sal = str2float(dic['sal'])
        hra = sal * 20 /100
        da = sal * 15 /100
        pf = sal * 35 /100
        gpay = sal+hra+da
        npay = gpay-pf
        print(f"{rno:<10}{ename:<10}{sal:<10}{hra:<10}{da:<10}{pf:<10}{gpay:<10}{npay:<10}")
except Exception as e:
    print("Error:", e)

'''
output:
eid       ename     sal       hra       da        pf        gpay      npay      
2001      x5        600000.0  120000.0  90000.0   210000.0  810000.0  600000.0  
2002      x3        300000.0  60000.0   45000.0   105000.0  405000.0  300000.0  
2003      x1        200000.0  40000.0   30000.0   70000.0   270000.0  200000.0  
2004      x2        200000.0  40000.0   30000.0   70000.0   270000.0  200000.0  
2005      x4        400000.0  80000.0   60000.0   140000.0  540000.0  400000.0  
'''
