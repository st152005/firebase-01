import pyrebase

rows =[
    {"sname": "x5", "m1": "56.5", "m2": "63"},
    {"sname": "x3", "m1": "36.5", "m2": "43"},
    {"sname": "x1", "ml": "45.5", "m2": "52"},
    {"sname": "x2", "ml": "98", "m2": "20"},
    {"sname": "x4", "m1": "61", "m2": "45.5"}
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
    rno = 1001
    fb = pyrebase.initialize_app(fbConfig)
    db = fb.database()
    for row in rows:
        db.child(str(rno)).set(row)
        rno += 1
    print('Added 5 row(s)')

except Exception as e:
    print("Error:", e)
