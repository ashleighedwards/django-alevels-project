import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

cursor.execute("SELECT name,price,in_stock FROM items")
result = cursor.fetchall()
re = []
for r in result:
    for i in r:
        re.append(i)
all_list2 = []
n = 3
for a in range(0,len(re),3):
    all_list2.append(re[a:n])
    n+=3

calc = []

for a in range(1,len(re),3):
    c = re[a]/re[a+1]
    calc.append(re[a-1])
    calc.append(c)

dictionary = {}
for i in range(1,len(calc),2):
    dictionary[calc[i-1]] = calc[i]
sorted_d = sorted((value, key) for (key,value) in dictionary.items())

popular_list = []
for a in reversed(sorted_d):
    for b in range(0,len(a),2):
        popular_list.append(a[b-1])

top_four = popular_list[:4]

top_top_four = []
for b in top_four:
    for a in range(len(re)):
        if b == re[a]:
            top_top_four.append(re[a])
            top_top_four.append(re[a+1])
            top_top_four.append(re[a+2])

