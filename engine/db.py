import csv
import sqlite3

con = sqlite3.connect("javiah.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
cursor.execute(query)
con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'google', 'https://www.google.com/')"
cursor.execute(query)
con.commit()

# edge
query = "INSERT INTO web_command VALUES (null,'microsoft edge', 'https://www.bing.com/search?q=')"
cursor.execute(query)
con.commit()

# wikipedia
query = "INSERT INTO web_command VALUES (null,'wikipedia', 'https://www.wikipedia.org/')"
cursor.execute(query)
con.commit()


# testing module
app_name = "android studio"
app_path = "c:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
cursor.execute('INSERT INTO sys_command (name, path) VALUES (?, ?)', (app_name, app_path))
con.commit()

# fetch the path of the app
cursor.execute('SELECT path FROM sys_command WHERE name = ?', (app_name,))
results = cursor.fetchall()
if results:
    print(results[0][0])
else:
    print("No path found for app:", app_name)

# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
desired_columns_indices = [0, 30]

# Read data from CSV and insert into SQLite table for the desired columns
with open('C:\\Users\\BEST\\Documents\\CodSoft\\CodeSoft_ChatBot\\www\\assets\\contacts\\contacts.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        selected_data = [row[i] for i in desired_columns_indices]
        cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
con.commit()

if con:
    cursor = con.cursor()
    query = "INSERT INTO contacts VALUES (null,'lucy', '1234567890', 'null')"
    cursor.execute(query)
    con.commit()
else:
    print("Cannot operate on a closed database.")

query = 'Edwin'
query = query.strip().lower()

cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
results = cursor.fetchall()
print(results[0][0])

# Close the connection after all operations are done
con.close()