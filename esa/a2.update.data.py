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
    editData={"2001": {"sal": "600000"},"2003": {"sal":"200000"}}
    db.update(editData)
    print('Updated 2 row(s)')
    
except Exception as e:
    print("Error:", e)

'''
output:
Updated 2 row(s)
'''
