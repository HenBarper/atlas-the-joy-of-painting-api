import csv

# Initialize an empty list to store the titles
titles = [] # Colors used -
seasons = [] # Colors used -
episodes = [] # Colors used -
ep_colors = [] # Colors used -
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
        all_subjects.append('null-subject')
        # subjects_used.append(current_subjects)
        subjects_used.append(','.join(map(str, current_subjects)))

with open('data/colors_used.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Read the header row
    header_row = next(reader)

    # Extract the items from index 10 to 27 in the header row
    all_colors = header_row[10:28] # length 18
    all_colors = [phrase.lower().replace('_', ' ').title() for phrase in all_colors]

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
        all_colors.append('null-colors')
        data.append(info)

rows = zip(titles, seasons, episodes, ep_colors, colors_used, image_srcs, youtube_srcs, all_colors, all_subjects, air_dates, months, notes, subjects_used)

# Specify the file name
csv_file = 'data/clean_data.csv'

# Write rows to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Season', 'Episode Number', 'Colors', 'Color IDs', 'Image Links', 'Youtube Links', 'All Colors', 'Subject Matter', 'Air Dates', 'Months', 'Notes', 'Subjects'])  # Write header
    writer.writerows(rows)  # Write rows
