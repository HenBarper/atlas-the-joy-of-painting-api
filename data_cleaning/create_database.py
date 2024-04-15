import psycopg2

# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="password",
    host="127.0.0.1",  # localhost or 127.0.0.1
    port="5432"
)

# Create a cursor object using the connection
cur = conn.cursor()

# Define the CREATE TABLE query
create_table_query = '''
CREATE TABLE "episodes" (
  "episode_id" integer PRIMARY KEY,
  "title" varchar,
  "season" integer,
  "episode" integer,
  "colors" varchar,
  "subjects" varchar,
  "air_date" varchar,
  "month" varchar,
  "notes" varchar,
  "image_src" varchar,
  "youtube_src" varchar
);

CREATE TABLE "subjects" (
  "subject_id" integer PRIMARY KEY,
  "subject_name" varchar
);

CREATE TABLE "colors" (
  "color_id" integer PRIMARY KEY,
  "color_name" varchar
);

-- Join table
CREATE TABLE "episode_subjects" (
  "episode_id" integer,
  "subject_id" integer,
  PRIMARY KEY("episode_id", "subject_id")
);
ALTER TABLE "episode_subjects" ADD FOREIGN KEY ("episode_id") REFERENCES "episodes" ("episode_id");
ALTER TABLE "episode_subjects" ADD FOREIGN KEY ("subject_id") REFERENCES "subjects" ("subject_id");

-- Join Table
CREATE TABLE "episode_colors" (
  "episode_id" integer,
  "color_id" integer,
  PRIMARY KEY("episode_id", "color_id")
);
ALTER TABLE "episode_colors" ADD FOREIGN KEY ("episode_id") REFERENCES "episodes" ("episode_id");
ALTER TABLE "episode_colors" ADD FOREIGN KEY ("color_id") REFERENCES "colors" ("color_id");

'''

# Execute the CREATE TABLE query
cur.execute(create_table_query)

# Commit the transaction
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()
