from google.colab import drive
drive.mount('/content/drive')

import os

# List files in the root of your Google Drive
os.listdir('/content/drive/My Drive')

"""
Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).
['sparsematrixtodecisiontree_algorithm_fortemplatebased_humantomachineinteraction_18.01-2010_0152hr.gsheet',
 'Culture.pptx',
 'Stuffs',
 :
 'JD.gdoc',
 'alice.gdoc']
"""

# Reading a file
with open('/content/drive/My Drive/my_csv_old.csv', 'r') as file:
    content = file.read()
    print(content)

# Writing to a file
with open('/content/drive/My Drive/example_output.txt', 'w') as file:
    file.write('Hello, Google Drive!')    

"""

"""

import pandas as pd

df = pd.read_csv('/content/drive/My Drive/my_csv_old.csv')
print(df.head())

"""

"""
# conduct file processing
import nltk
from nltk.corpus import words

# Ensure the NLTK words corpus is downloaded
nltk.download('words')

# Set file paths
input_file_path = './sample_data/TEA_Text_Editor_Areana.txt'
output_file_path = './sample_data/out.txt'

# Load NLTK word corpus
valid_words = set(words.words())

# Function to filter out non-dictionary words
def filter_words(input_text):
    # Split text into words, and filter out non-dictionary words
    filtered_words = [word for word in input_text.split() if word.lower() in valid_words]
    return '\n'.join(filtered_words)

# Read input file
with open(input_file_path, 'r') as input_file:
    input_text = input_file.read()

# Filter out non-dictionary words
filtered_text = filter_words(input_text)

# Write the filtered output to a new file
with open(output_file_path, 'w') as output_file:
    output_file.write(filtered_text)

print(f"Filtered text has been written to {output_file_path}")
