import re
import pandas as pd
from datetime import datetime

# Specify the path to the input .txt file in the working directory
input_file = "input_data.txt"

# Read the data from the .txt file
with open(input_file, "r") as file:
    data = file.read()

# Define the regex pattern
pattern = r'TO_(.*?)\/'

# Extract data using regex
matches = re.findall(pattern, data)

# Create a DataFrame with the extracted data
df = pd.DataFrame(matches, columns=['Extracted Data'])

# Add a timestamp to the Excel file name
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
excel_filename = f'output_{timestamp}.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(excel_filename, index=False)

print(f'Data has been saved to an Excel file: {excel_filename}')
