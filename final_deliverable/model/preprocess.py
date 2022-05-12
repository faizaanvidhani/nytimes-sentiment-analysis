import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
import tensorflow as tf
import hyperparameters as hp
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def remove_punctuation(text):
    final = "".join(u for u in text if u not in ("?", ".", ";", ":",  "!",'"'))
    return final

def remove_stopwords(text):
    stop = stopwords.words('english')    
    return ' '.join([word for word in text.split() if word not in (stop)])

def lemmatize_text(text):
    word_list = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
    return lemmatized_output

def decode_article(text,reverse_word_index):
    '''Converts an encoded article back into words with oov tokens for words outside the vocabulary'''
    return ' '.join([reverse_word_index.get(i, '?') for i in text])

def prepare_df(df,cols):
    for col in cols:
        # Remove punctuation
        df[col] = df[col].apply(remove_punctuation)
        # Remove stopwords (words that have very little impact on sentence meaning)
        df[col] = df[col].apply(remove_stopwords)
        # Lemmatize the text
        df[col] = df[col].apply(lemmatize_text)
        return df

def get_data():
    # Read in the file
    train_df = prepare_df(pd.read_csv (r'sst_data/train.csv'),['text'])
    test_df = prepare_df(pd.read_csv (r'sst_data/test.csv'),['text'])
    # Tokenize text (Abstracts the process of creating a vocab and replaces words not in the vocabulary with 'UNK')
    tokenizer = Tokenizer(num_words = hp.VOCAB_SIZE, oov_token=hp.OOV_TOKEN)
    tokenizer.fit_on_texts(train_df['text'])
    word_index = tokenizer.word_index
    dict(list(word_index.items())[0:10])
    sequences = tokenizer.texts_to_sequences(train_df['text'])
    # Pad the data so that each sequence is of the same length
    train_padded = pad_sequences(sequences, maxlen=hp.MAX_LENGTH, padding=hp.PADDING_TYPE, truncating=hp.TRUNC_TYPE)
    # No need to tokenize ratings because they are integers
    train_label_seq = np.array(train_df.rating)
    # Create a dictionary that maps from word to index
    reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
    # Repeat relevant steps for test data
    sequences = tokenizer.texts_to_sequences(test_df['text'])
    test_padded = pad_sequences(sequences, maxlen=hp.MAX_LENGTH, padding=hp.PADDING_TYPE, truncating=hp.TRUNC_TYPE)
    test_label_seq = np.array(test_df.rating)
    return train_padded, train_label_seq, test_padded, test_label_seq, reverse_word_index

nltk.download('wordnet')