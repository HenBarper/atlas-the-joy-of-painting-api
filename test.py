data = """
"Title" (date) notes
"A Walk in the Woods" (January 11, 1983)
"Mount McKinley" (January 11, 1983)
"Ebony Sunset" (January 18, 1983)
"Wilderness Day" (May 17, 1994)
"""

# Split the data into lines
lines = data.strip().split('\n')

# Initialize an empty list to store the titles
titles = []

# Iterate over the lines starting from the second line (skipping the header)
for line in lines[1:]:
    # Split each line by parentheses and extract the title (first part)
    title = line.split('(')[0].strip()
    # Remove the surrounding quotes from the title
    title = title.strip('"')
    # Append the title to the list
    titles.append(title)

# Print the list of titles
for title in titles:
  print(title)
