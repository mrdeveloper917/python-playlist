import os

# Specify the directory path
directory_path = '/'

# Get the list of entries in the directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)
