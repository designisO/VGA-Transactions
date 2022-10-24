import sqlite3

# define the connect and cursor
conn = sqlite3.connect('vga_transactions.db')

# creating cursor
cur = conn.cursor()

# create stores table
command1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""
cur.execute(command1)

# create purchases table

command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT,
FOREIGN KEY(store_id) REFERENCES stores(store_id)"""
cur.execute(command2)


# Add Records to the stores table
cur.execute("INSERT INTO stores VALUES (25, 'Columbia, SC')")
cur.execute("INSERT INTO stores VALUES (180, 'Manhattan, NY')")
cur.execute("INSERT INTO stores VALUES (300, 'Los Angeles, CA')")


# Add records to the purchases table
cur.execute("INSERT INTO purchases VALUES (60, 30, 20.23)")
cur.execute("INSERT INTO purchases VALUES (22, 68, 30.24)")

# Get Results
cur.execute("SELECT * FROM purchases")

results = cur.fetchall()
print(results)

# update
cur.execute("UPDATE purchases SET total_cost = 4 WHERE purchase_id = 68")

# delete
cur.execute("DELETE FROM purchases WHERE purchase_id = 68")

