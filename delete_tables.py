import psycopg2

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="p0$tGR3z",
    host="127.0.0.1",  # localhost or 127.0.0.1
    port="5432"
)

# Create a cursor object using the connection
cur = conn.cursor()

# Delete the tables
cur.execute("DROP TABLE episode_colors")
cur.execute("DROP TABLE episode_subjects")
cur.execute("DROP TABLE episodes")
cur.execute("DROP TABLE colors")
cur.execute("DROP TABLE subjects")

# Commit the transaction
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()