import spacy
# Add imports for example, as well as textcat config...
from spacy.training import Example
from spacy.pipeline.textcat import single_label_bow_config, single_label_default_config
from thinc.api import Config
import random
import helpers
import numpy as np

def train_classif_symptoms_model(training_data_path = "Backend\\AudioProcessing\\trainingData\\text_classification_symptoms.json"):
    output_dir = 'Backend\\AudioProcessing\\trained_algorithms\\ML\\symptoms_classif_model'
    
    # bow
    config = Config().from_str(single_label_bow_config)
    TRAINING_DATA = helpers.load_data(training_data_path)

    # initialize a blank model
    nlp = spacy.blank("en")
    # categorizer pipeline
    category = nlp.add_pipe("textcat", last=True, config=config)

    category.add_label("POSITIVE")
    category.add_label("NEGATIVE")

    # Start the training
    nlp.begin_training()
    # Loop for 100 iterations
    for i in range(200):
        # Shuffle the training data
        random.shuffle(TRAINING_DATA)
        losses = {}

        # Do minibatch training
        for batch in spacy.util.minibatch(TRAINING_DATA, size=4):
            texts = [nlp.make_doc(text) for text, entities in batch]
            annotations = [{"cats": entities} for text, entities in batch]
            examples = [Example.from_dict(doc, annotation) for doc, annotation in zip(
                texts, annotations
            )]
            nlp.update(examples, losses=losses)
        if i % 50 == 0:
            print(losses)
    nlp.to_disk(output_dir)
    print("Saved model to:", output_dir) 


#train_classif_symptoms_model()
def test_classif_symptoms_model(output_dir = 'Backend\\AudioProcessing\\trained_algorithms\\ML\\symptoms_classif_model'):
    nlp = spacy.load(output_dir)
    test_array = ["I had three headaches today", "I had no headaches", "I didn't have a headache", "I had light sensitivity today"]
    for sents in test_array:
        doc = nlp(sents)
        #max_confidence_label = list(doc.cats.keys())[np.argmax(np.array(list(doc.cats.values())))]
        print(doc.cats)
        #print(doc.cats[max_confidence_label])

train_classif_symptoms_model()
#test_classif_symptoms_model()