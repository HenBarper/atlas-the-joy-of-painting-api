import psycopg2

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(
    dbname="Bob_Ross",
    user="postgres",
    password="p0$tGR3z",
    host="localhost"  # or your host address
)

# Create a cursor object using the connection
cur = conn.cursor()

# Define the CREATE TABLE query
create_table_query = '''
CREATE TABLE IF NOT EXISTS your_table_name (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    note TEXT
)
'''

# Execute the CREATE TABLE query
cur.execute(create_table_query)

# Assuming you have lists of titles, ids, and notes
titles = ['Title 1', 'Title 2', 'Title 3']
ids = [1, 2, 3]
notes = ['Note 1', 'Note 2', 'Note 3']

# Iterate through the lists and insert data into the database
for i in range(len(titles)):
    cur.execute(
        "INSERT INTO your_table_name (title, id, note) VALUES (%s, %s, %s)",
        (titles[i], ids[i], notes[i])
    )

# Commit the transaction
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()
