import pandas as pd
import re
import random
import json
import spacy
from spacy.util import minibatch, compounding
import warnings
import matplotlib.pyplot as plt
from spacy.tokens import DocBin
from tqdm import tqdm


training_path = "Backend\\AudioProcessing\\trainingData\\"

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)

def change_data_to_v3(TRAIN_DATA):
    nlp = spacy.blank("en") # load a new spacy model
    db = DocBin() # create a DocBin object

    for text, annot, in tqdm(TRAIN_DATA): # data in previous format
        doc = nlp.make_doc(text) # create doc object from text
        ents = []
        for start, end, label in annot["entities"]: # add character indexes
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents # label the text with the ents
        db.add(doc)
    return db

def save_spacy_format(TRAIN_DATA, VALIDATION_DATA):
    symptoms_train = change_data_to_v3(TRAIN_DATA)
    symptoms_validate = change_data_to_v3(VALIDATION_DATA)
    symptoms_train.to_disk("Backend\\AudioProcessing\\trainingData\\symptomsML_training.spacy")
    symptoms_validate.to_disk("Backend\\AudioProcessing\\trainingData\\symptomsML_validate.spacy")

def get_cvs_data_symptoms():
#load the file of medical information and clean it
    med_transcript = pd.read_csv(training_path + "medicalData.csv")
    med_transcript.dropna(subset=['trackable_type'], inplace=True)

    #grab only the relevant information
    relevant_info = med_transcript[['trackable_type', 'trackable_name']]

    #only keep the symptoms and delete all duplicates
    symptoms = relevant_info[relevant_info['trackable_type'] == 'Symptom']
    symptoms = symptoms['trackable_name'] #keep just the symptoms name
    symptoms = symptoms[symptoms.str.contains("[^a-zA-Z ]") == False]
    symptoms = symptoms[symptoms.str.split().apply(len) <= 3].drop_duplicates()
    symptoms.info()

    one_worded_symptoms = symptoms[symptoms.str.split().apply(len) == 1]
    two_worded_symptoms = symptoms[symptoms.str.split().apply(len) == 2]
    three_worded_symptoms = symptoms[symptoms.str.split().apply(len) >= 3]

    # create a bar plot
    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.bar([1, 2, 3], [one_worded_symptoms.size, two_worded_symptoms.size, three_worded_symptoms.size])

    # label the x-axis instances
    # ax.set_xticks([1, 2, 3])
    # ax.set_xticklabels(["one", "two", "three"])

    # # set the title and the xy-axis labels
    # plt.title("Number of Words in Symptoms Entities")
    # plt.xlabel("Number of Words")
    # plt.ylabel("Symptoms Entities")

    # # display the plot
    # plt.show()

    # total number of symptoms
    total_num_symptoms = round(one_worded_symptoms.size / 45 * 100)

    # shuffle the 2-worded and 3-worded symptoms since we'll be slicing them
    two_worded_symptoms = two_worded_symptoms.sample(frac=1)
    three_worded_symptoms = three_worded_symptoms.sample(frac=1)

    # append the symptoms together 
    symptoms = one_worded_symptoms.append(two_worded_symptoms[:round(total_num_symptoms * 0.30)]).append(three_worded_symptoms[:round(total_num_symptoms* 0.25)])
    pd.set_option('display.max_rows', None)
    print(symptoms.head(100))
    # print the resulting sizes
    for i in range(3):
        print(f"{i+1}-worded symptoms entities:", symptoms[symptoms.str.split().apply(len) == i + 1].size)
    return symptoms

#-----------------------------------------------DATA SELECTED, CREATING DATA SET ------------------------------
def create_data_sets(symptoms,sentence_limit = 167):
    symptoms_templates = load_data(training_path + "symptoms_template.json")
    TRAIN_SYMP_DATA = {
        "one_word": [],
        "two_words": [],
        "three_words": []
    }
    TEST_SYMP_DATA = {
        "one_word": [],
        "two_words": [],
        "three_words": []
    }

    # one_food, two_food, and three_food combinations will be limited to 167 sentences
    SYMP_SENTENCE_LIMIT = sentence_limit

    # helper function for deciding what dictionary and subsequent array to append the food sentence on to
    def get_symptom_data(count):
        return {
            1: TRAIN_SYMP_DATA["one_word"] if len(TRAIN_SYMP_DATA["one_word"]) < SYMP_SENTENCE_LIMIT else TEST_SYMP_DATA["one_word"],
            2: TRAIN_SYMP_DATA["two_words"] if len(TRAIN_SYMP_DATA["two_words"]) < SYMP_SENTENCE_LIMIT else TEST_SYMP_DATA["two_words"],
            3: TRAIN_SYMP_DATA["three_words"] if len(TRAIN_SYMP_DATA["three_words"]) < SYMP_SENTENCE_LIMIT else TEST_SYMP_DATA["three_words"],
        }[count]

    # the pattern to replace from the template sentences
    pattern_to_replace = "{}"

    # shuffle the data before starting
    symptoms = symptoms.sample(frac=1)

    # the count that helps us decide when to break from the for loop
    symptoms_entity_count = symptoms.size - 1

    # start the while loop, ensure we don't get an index out of bounds error
    while symptoms_entity_count >= 2:
        entities = []

        # pick a random food template
        sentence = symptoms_templates[random.randint(0, len(symptoms_templates) - 1)]

        # find out how many braces "{}" need to be replaced in the template
        matches = re.findall(pattern_to_replace, sentence)

        # for each brace, replace with a food entity from the shuffled food data
        for match in matches:
            symptom = symptoms.iloc[symptoms_entity_count].lower()
            symptoms_entity_count -= 1

            # replace the pattern, but then find the match of the food entity we just inserted
            sentence = sentence.replace(match, symptom, 1)
            match_span = re.search(symptom, sentence).span()

            # use that match to find the index positions of the food entity in the sentence, append
            entities.append((match_span[0], match_span[1], "SYMPTOM"))

        # append the sentence and the position of the entities to the correct dictionary and array
        get_symptom_data(len(matches)).append((sentence, {"entities": entities}))
    # print the number of food sentences, as well as an example sentence
    TRAIN_DATA = TRAIN_SYMP_DATA["one_word"] + TRAIN_SYMP_DATA["two_words"] + TRAIN_SYMP_DATA["three_words"]
    TEST_DATA = TEST_SYMP_DATA["one_word"] + TEST_SYMP_DATA["two_words"] + TEST_SYMP_DATA["three_words"]

    for key in TRAIN_SYMP_DATA:
        print("{} {} sentences: {}".format(len(TRAIN_SYMP_DATA[key]), key, TRAIN_SYMP_DATA[key][0]))

    for key in TEST_SYMP_DATA:
        print("{} {} items: {}".format(len(TEST_SYMP_DATA[key]), key, TEST_SYMP_DATA[key][0]))
    
    return TRAIN_DATA, TEST_DATA

#symptoms = get_cvs_data_symptoms()
symptoms = pd.read_json(training_path + "symptoms_data.json", typ="series") 

TRAIN_DATA, TEST_DATA = create_data_sets(symptoms, 10)
TRAIN_DATA = TRAIN_DATA + load_data(training_path + "symptomsML_training.json")
save_spacy_format(TRAIN_DATA, TEST_DATA)