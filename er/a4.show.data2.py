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

try:    
    fb = pyrebase.initialize_app(fbConfig)
    db = fb.database()
    rows = db.get()
    for row in rows.each():
        print(row.key(), row.val())
except Exception as e:
    print("Error:", e)

'''
output:
1001 {'m1': '56.5', 'm2': '63', 'sname': 'x5'}
1002 {'m1': '36.5', 'm2': '43', 'sname': 'x3'}
1003 {'m1': '45.5', 'm2': '52', 'sname': 'x1'}
1004 {'m1': '98', 'm2': '20', 'sname': 'x2'}
1005 {'m1': '61', 'm2': '45.5', 'sname': 'x4'}
-Ohz7_Lu2rjQUxc84-L7 {'m1': '56.5', 'm2': '63', 'rno': '1001', 'sname': 'x5'}
drink {'categories': {'soft': 'grapes, cherry, oraange juices'}}
'''
