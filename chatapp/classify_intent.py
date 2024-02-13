import tensorflow as tf
import numpy as np
import pandas as pd
import joblib
import random
from keras_preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model
from .classify_entity import extract_entities
from .ml_module import responses

MAX_SEQUENCE_LENGTH = 10

# Define paths to your model and tokenizer
TOKENIZER_PATH = 'chatapp/data/tokenizer.pickle'
TOKENIZER_CONFIG_PATH = 'chatapp/data/tokenizer_config.pickle'
MODEL_PATH = 'chatapp/data/intent_classification.h5'

# Load the tokenizer and configuration
with open(TOKENIZER_CONFIG_PATH, 'rb') as handle:
    tokenizer_config = joblib.load(handle)

with open(TOKENIZER_PATH, 'rb') as handle:
    tokenizer = joblib.load(handle)

tokenizer.num_words = tokenizer_config['num_words']
tokenizer.word_index = tokenizer_config['word_index']

loaded_model = load_model(MODEL_PATH, compile=False)


# Preprocess user input and perform intent classification
def classify_intent(user_input):
    try:

        sequences_new = tokenizer.texts_to_sequences(user_input)
        data_new = pad_sequences(sequences_new, maxlen=MAX_SEQUENCE_LENGTH)

        # Make predictions using the loaded model
        loaded_model.compile(loss='binary_crossentropy',
                      optimizer=tf.keras.optimizers.Adam(),  # Use tf.keras.optimizers
                      metrics=['accuracy'])
        predictions = loaded_model.predict(data_new)
        predicted_class = predictions.argmax(axis=-1)[0]

        predict_class = 0
        print(f"Predicted Class {predict_class}")

        if(predict_class == 0):
            response = responses(str(user_input))
            return response     

        elif(predict_class == 1):
            response = extract_entities(user_input)
            return response

        elif(predict_class == 2):
            response = extract_entities(user_input)
            return response

        elif(predict_class == 3):
            response = extract_entities(user_input)
            return response

    except Exception as e:
        return str(e)
