import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

cursor.execute("SELECT name,price,in_stock FROM items")
result = cursor.fetchall()
print(result)
re =[]
for r in result:
    for b in r:
        re.append(b)
listt = []

n = 3
for a in range(0,len(re),3):
    listt.append(re[a:n])
    print(re[a:n])
    n+=3

