import pandas as pd
import re
import matplotlib.pyplot as plt

# Function to extract file type from the file path
def extract_file_type(filepath):
    filename = filepath.split('/')[-1]  # Extract the last part after the last '/'
    if '.' in filename:
        return filename.split('.')[-1]
    else:
        return None  # Return None for files without extension

# Read data from file
file_path = r'C:\Users\chenz\Desktop\sr\sr_project1_data\the_entire_process\open.txt'
with open(file_path, 'r') as file:
    data = file.read()

# Parsing the data
lines = data.strip().split("\n")
pattern = re.compile(r"(\d+)\s(\d+:\d+:\d+)\sopenat\(.*?,\s\"(.+?)\"")

parsed_data = []
for line in lines:
    match = pattern.match(line)
    if match:
        pid, time, filepath = match.groups()
        file_type = extract_file_type(filepath)
        if file_type:  # Only append if file_type is not None
            parsed_data.append([pid, time, filepath, file_type])

# Print parsed data for debugging
print("Parsed Data:")
for item in parsed_data:
    print(item)

df = pd.DataFrame(parsed_data, columns=["PID", "Time", "Filepath", "Filetype"])

# Check the unique file types
unique_filetypes = df['Filetype'].unique()
print("Unique file types:", unique_filetypes)

# Filter out invalid file types based on manual inspection
valid_filetypes = set([
    "aff", "dat", "db", "dic", "ht", "odp", "res", "so", "sod",
    "soe", "theme", "tmp", "ttf", "txt", "xlb", "xlc", "xml"
])
df = df[df['Filetype'].isin(valid_filetypes)]

# Aggregate the counts of each file type
filetype_counts = df['Filetype'].value_counts()

# Print filetype counts for debugging
print("Filetype Counts:")
print(filetype_counts)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
if not filetype_counts.empty:
    bars = filetype_counts.plot(kind='bar', color='blue', ax=ax)

    # Set labels and title
    ax.set_xlabel("File Type")
    ax.set_ylabel("Count of Files Opened")
    ax.set_title("Total Count of Each File Type Opened")

    # Annotate each bar with the count
    for bar in bars.patches:
        ax.annotate(f'{bar.get_height()}',
                    (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("No valid file types found to plot.")
