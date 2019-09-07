import pymysql

db = pymysql.connect("localhost","root","root","wallet")


cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM wallet_balance")
data = cursor.fetchone()
print(data)
db.close()