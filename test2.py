import csv

# Initialize an empty list to store the titles
titles = []
data = []

# Open the CSV file
with open('data/episode_dates.txt', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    # Skip the header row
    next(reader)
    # Iterate over each row in the CSV file
    for row in reader:
        # Extract the title from the first column
        title = row[0].strip('"')
        # Append the title to the list
        data.append(title)

# Split the data into lines
# lines = data#.strip().split('\n')

for line in data[0:]:
    # Split each line by parentheses and extract the title (first part)
    title = line.split('(')[0].strip()
    # Remove the surrounding quotes from the title
    title = title.strip('"')
    # Append the title to the list
    titles.append(title)

# Print the list of titles
counter = 1
for title in titles:
  print(f'{counter}. {title}')
  counter += 1
