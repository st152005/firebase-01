import pyrebase

rows =[
    {"ename": "x5", "sal":"500000"},
    {"ename": "x3", "sal":"300000"},
    {"ename": "x1", "sal":"100000"},
    {"ename": "x2", "sal":"200000"},
    {"ename": "x4", "sal":"400000"}
]

fbConfig ={
  "apiKey": "AIzaSyArn0ZhlPLIlOhvDZ4SlOvujTJEvdgnUok",
  "authDomain": "fbprj1a-94757.firebaseapp.com",
  "databaseURL": "https://fbprj1a-94757-default-rtdb.firebaseio.com",
  "projectId": "fbprj1a-94757",
  "storageBucket": "fbprj1a-94757.firebasestorage.app",
  "messagingSenderId": "1094015731404",
  "appId": "1:1094015731404:web:5ed90a28d06c7bad72e469"
}

try:
    eid = 2001
    fb = pyrebase.initialize_app(fbConfig)
    db = fb.database()
    for row in rows:
        db.child(str(eid)).set(row)
        eid += 1
    print('Added 5 row(s)')

except Exception as e:
    print("Error.:",e)
        
'''
output:
Added 5 row(s)
'''
