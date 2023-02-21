import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT item_choice, many_items, crime_type FROM project_removetheitems")
removed = cursor.fetchall()
removed_list = []
for a in range(len(removed)):
    for d in removed[a]:
        removed_list.append(d)
cursor.execute("SELECT name, in_stock FROM items")
items_columns = cursor.fetchall()
items_list = []
for i in items_columns:
    for j in i:
        items_list.append(j)
improved_list = []
for item in range(0, len(removed_list),3):
    for a in range(0, len(items_list),2):
        mini_list = []
        if removed_list[item] == items_list[a]:
            removed_list[item+1] = items_list[a+1]-removed_list[item+1]
            mini_list.append(removed_list[item])
            mini_list.append(removed_list[item+1])
            mini_list.append(removed_list[item+2])
            improved_list.append(mini_list)
print(improved_list)
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        print("error")
    return None

def update_item(conn, item):
    sql = ''' UPDATE items
              SET in_stock = ?
              WHERE name = ?'''

    cur = conn.cursor()
    cur.execute(sql, item)
    return cur.lastrowid

def delete_records(conn):
    sql = '''DELETE FROM project_removetheitems
             WHERE user_id >0'''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.lastrowid

def main():
    database = "db.sqlite3"
    conn = create_connection(database)
    with conn:
        for i in range(len(improved_list)):
            item = (improved_list[i], improved_list[i-1])
            print(item)
            for a in item:
                b = a
                print(b)
                item = (b[1],b[0])
                update_item(conn, item)
                print("updated")
        delete_records(conn)
        print("deleted")
     
if __name__ == '__main__':
    main()


