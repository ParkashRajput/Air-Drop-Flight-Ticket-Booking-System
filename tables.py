import sqlite3

# Connect to your Django database
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in db.sqlite3:")
for table in tables:
    table_name = table[0]
    print(f"\nTable: {table_name}")
    
    # Get columns for this table
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    for col in columns:
        col_id, col_name, col_type, notnull, default_value, pk = col
        print(f"  Column: {col_name}, Type: {col_type}, Not Null: {notnull}, PK: {pk}, Default: {default_value}")

conn.close()
