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

print(f"{'rno':<10}{'sname':<10}{'m1':<10}{'m2':<10}{'total':<10}{'average':<10}{'result':<10}")

try:
    fb = pyrebase.initialize_app(fbConfig)
    db = fb.database()
    rows = db.get()
    for row in rows.each():
        dic=row.val()
        rno=row.key()
        sname=dic['sname']
        m1 = str2float(dic['m1'])
        m2 = str2float(dic['m2'])
        total = m1 + m2
        average = total /2
        result = 'Pass' if m1 > 34.4 and m2 > 34.4 else 'Fail'
        print(f"{rno:<10}{sname:<10}{m1:<10}{m2:<10}{total:<10}{average:<10}{result:<10}")
except Exception as e:
    print("Error:", e)

'''
output:
rno       sname     m1        m2        total     average   result    
1001      x5        56.5      63.0      119.5     59.75     Pass      
1002      x3        36.5      43.0      79.5      39.75     Pass      
1003      x1        45.5      52.0      97.5      48.75     Pass      
1004      x2        98.0      20.0      118.0     59.0      Fail      
1005      x4        61.0      45.5      106.5     53.25     Pass      
'''
