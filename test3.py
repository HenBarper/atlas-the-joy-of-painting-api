import csv

# Initialize an empty list to store the titles
titles = [] # Colors used -
seasons = [] # Colors used -
episodes = [] # Colors used -
ep_colors = [] # Colors used -
subjects = [] # Subject matter
air_dates = []
months = []
notes = []
image_srcs = [] # Colors used -
youtube_srcs = [] # Colors used -
data = []

all_colors = [] # Colors used
all_subjects = [] # Subject matter

# Open the CSV files
with open('data/episode_dates.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Assuming the date is in parentheses after the title
        start_index = line.find('(')
        end_index = line.find(')')
        if start_index != -1 and end_index != -1:  # Ensure both parentheses are found
            date_str = line[start_index + 1:end_index]
            air_dates.append(date_str)
            month = date_str.split()[0]
            months.append(month)

with open('data/subject_matter.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Read the header row
    header_row = next(reader)

    # Extract the items from index 2 to 67 in the header row
    all_subjects = header_row[2:67]
    all_subjects = [phrase.lower().replace('_', ' ').title() for phrase in all_subjects]
    for row in reader:
        all_subjects.append('null-subject')

with open('data/colors_used.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Read the header row
    header_row = next(reader)

    # Extract the items from index 10 to 27 in the header row
    all_colors = header_row[10:28]

    # Iterate over each row in the CSV file
    for row in reader:
        info = row
        title = row[3]#.strip('"')
        season = row[4]
        episode = row[5]
        colors = row[8]
        image_src = row[2]
        youtube_src = row[7]
        color_data = eval(colors)
        # Convert list to comma-separated string
        csv_string = ','.join(color_data)
        list_data_cleaned = csv_string.replace('\r', '').replace('\n', '')

        # Append the title to the list
        titles.append(title)
        seasons.append(season)
        episodes.append(episode)
        # ep_colors.append(csv_string)
        ep_colors.append(list_data_cleaned)
        image_srcs.append(image_src)
        youtube_srcs.append(youtube_src)
        all_colors.append('null-colors')
        data.append(info)

rows = zip(titles, seasons, episodes, ep_colors, image_srcs, youtube_srcs, all_colors, all_subjects, air_dates, months)

# Specify the file name
csv_file = 'output.csv'

# Write rows to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Season', 'Episode Number', 'Colors', 'Image Links', 'Youtube Links', 'All Colors', 'Subject Matter', 'Air Dates', 'Months'])  # Write header
    writer.writerows(rows)  # Write rows
