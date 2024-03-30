import csv
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

# Initialize an empty list to store the titles
titles = [] # Colors used -
seasons = [] # Colors used -
episodes = [] # Colors used -
ep_colors = [] # Colors used -
# subjects = [] # Subject matter - 
air_dates = [] # Episode dates -
months = [] # Episode dates -
notes = [] # Episode dates - 
image_srcs = [] # Colors used -
youtube_srcs = [] # Colors used -
colors_used = [] # Colors used -
subjects_used = [] # Subject matter

data = []

all_colors = [] # Colors used
all_subjects = [] # Subject matter

# Open the CSV files
with open('data/episode_dates.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        line = line.strip()  # Remove leading and trailing whitespace, including '\n'
        # Assuming the date is in parentheses after the title
        start_index = line.find('(')
        end_index = line.find(')')
        
        if start_index != -1 and end_index != -1:  # Ensure both parentheses are found
            date_str = line[start_index + 1:end_index]
            
            # Check for additional text after the date (notes)
            notes_start_index = end_index + 1
            if notes_start_index < len(line):
                note = line[notes_start_index:].strip()
            else:
                note = 'empty'  # No notes present
            
            air_dates.append(date_str)
            month = date_str.split()[0]
            months.append(month)
            notes.append(note)

with open('data/subject_matter.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Read the header row
    header_row = next(reader)

    # Extract the items from index 2 to 67 in the header row
    all_subjects = header_row[2:67]
    all_subjects = [phrase.lower().replace('_', ' ').title() for phrase in all_subjects]
    for row in reader:
        # print(len(row))
        current_subjects = []
        if len(row) <= 69:
            # print('asjdhasdkhahk!!!')
            for i in range(2, 69):
                # print(i)
                if row[i].strip() == '1':
                    # print('match!')
                    current_subjects.append(i - 1)
        # all_subjects.append('null-subject')
        # subjects_used.append(current_subjects)
        subjects_used.append(','.join(map(str, current_subjects)))

with open('data/colors_used.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Read the header row
    header_row = next(reader)

    # Extract the items from index 10 to 27 in the header row
    all_colors = header_row[10:28] # length 18

    # Iterate over each row in the CSV file
    for row in reader:
        current_colors = []
        if len(row) <= 28:  # Check if the row has at least 29 columns
            for i in range(10, 28):  # Iterate through columns 11 to 28
                # print(f'column: {i}')
                if row[i].strip() == '1':
                    # print('match!')
                    current_colors.append(i - 9)
                # print(current_colors)
        info = row
        title = row[3]#.strip('"')
        season = row[4]
        episode = row[5]
        colors = row[8]
        image_src = row[2]
        youtube_src = row[7]
        color_data = eval(colors)
        # Convert list to comma-separated string
        csv_color_string = ','.join(color_data)
        list_data_cleaned = csv_color_string.replace('\r', '').replace('\n', '')

        # current_colors = eval(current_colors)
        # current_colors = ','.join(current_colors)
        # current_colors = current_colors.replace('[', '').replace(']', '')

        # Append the title to the list
        titles.append(title)
        seasons.append(season)
        episodes.append(episode)
        # ep_colors.append(csv_string)
        ep_colors.append(list_data_cleaned)
        # colors_used.append(current_colors)
        colors_used.append(','.join(map(str, current_colors)))
        image_srcs.append(image_src)
        youtube_srcs.append(youtube_src)
        # all_colors.append('null-colors')
        data.append(info)

for i in range(len(titles)):
    cur.execute(
        "INSERT INTO episodes (episode_id, title, season, episode, colors, subjects, air_date, month, notes, image_src, youtube_src) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (i + 1, titles[i], seasons[i], episodes[i], colors_used[i], subjects_used[i], air_dates[i], months[i], notes[i], image_srcs[i], youtube_srcs[i])
    )

for i in range(len(all_colors)):
    cur.execute(
        "INSERT INTO colors (color_id, color_name) VALUES (%s, %s)",
        (i + 1, all_colors[i])
    )

for i in range(len(all_subjects)):
    cur.execute(
        "INSERT INTO subjects (subject_id, subject_name) VALUES (%s, %s)",
        (i + 1, all_subjects[i])
    )

# Commit the transaction
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()
