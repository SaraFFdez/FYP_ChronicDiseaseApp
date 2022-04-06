import pandas as pd
import re
import random
import spacy
from spacy.util import minibatch, compounding
import warnings
import matplotlib.pyplot as plt


training_path = "Backend\\AudioProcessing\\trainingData\\"

#load the file of medical information and clean it
med_transcript = pd.read_csv(training_path + "medicalData.csv")
med_transcript.dropna(subset=['trackable_type'], inplace=True)

#grab only the relevant information
relevant_info = med_transcript[['trackable_type', 'trackable_name']]

#only keep the symptoms and delete all duplicates
symptoms = relevant_info[relevant_info['trackable_type'] == 'Symptom']
symptoms = symptoms['trackable_name'] #keep just the symptoms name
symptoms = symptoms[symptoms.str.split().apply(len) <= 3].drop_duplicates()
symptoms.info()
print(symptoms.head())

one_worded_foods = symptoms[symptoms.str.split().apply(len) == 1]
two_worded_foods = symptoms[symptoms.str.split().apply(len) == 2]
three_worded_foods = symptoms[symptoms.str.split().apply(len) >= 3]

# create a bar plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar([1, 2, 3], [one_worded_foods.size, two_worded_foods.size, three_worded_foods.size])

# label the x-axis instances
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(["one", "two", "three"])

# set the title and the xy-axis labels
plt.title("Number of Words in Food Entities")
plt.xlabel("Number of Words")
plt.ylabel("Food Entities")

# display the plot
plt.show()