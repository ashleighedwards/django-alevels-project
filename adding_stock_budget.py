import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT budget_total FROM Budget")
budget_total = cursor.fetchall()
budget_list = []
for a in range(len(budget_total)):
    for b in budget_total[a]:
        budget_list.append(b)
cursor.execute("SELECT item_choice, many_items FROM project_addtheitems")
item_names = cursor.fetchall()
items = []
for a in range(len(item_names)):
    for b in item_names[a]:
        items.append(b)
cursor.execute("SELECT name,in_stock FROM items")
items_columns = cursor.fetchall()
items_list = []
for i in items_columns:
    for a in i:
        items_list.append(a)
cursor.execute("SELECT name, price FROM items")
item_names = cursor.fetchall()
items_price = []
for a in range(len(item_names)):
    for b in item_names[a]:
        items_price.append(b)

final_list = []
for i in range(0, len(items),2):
    for a in range(0, len(items_list),2):
        mini_list = []
        if items[i] == items_list[a]:
            items_list[a+1] +=items[i+1]
            mini_list.append(items_list[a])
            mini_list.append(items_list[a+1])
            final_list.append(mini_list)
print(final_list)
new_budget = 0
for new_items in range(0,len(items),2):
    for i in range(0,len(items_price),2):
        if items[new_items] == items_price[i]:
            new_budget += (items[new_items+1]*items_price[i+1])
            for b in budget_list:
                new_budget = b - new_budget
print(new_budget)
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print("error")
    return None
def update_budget(conn, new_budget):
    sql = '''UPDATE Budget
             SET budget_total = ?
             WHERE id = 1 '''
    cur = conn.cursor()
    cur.execute(sql, new_budget)
    return cur.lastrowid
def update_item(conn, item):
    sql = ''' UPDATE items
              SET in_stock = ?
              WHERE name = ?'''
    cur = conn.cursor()
    cur.execute(sql, item)
    return cur.lastrowid
def delete_records(conn):
    sql = '''DELETE FROM project_addtheitems
             WHERE user_id = 1'''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.lastrowid
def main1():
    database = "db.sqlite3"
    conn = create_connection(database)
    with conn:
        new_budget_list = []
        new_budget_list.append(new_budget)
        update_budget(conn, new_budget_list)
        for i in range(len(final_list)):
            item = (final_list[i], final_list[i-1])
            for a in item:
                b = a
                print(b)
                item = (b[1],b[0])
                update_item(conn, item)
        delete_records(conn)
        print("deleted")

if __name__ == '__main1__':
    main()
