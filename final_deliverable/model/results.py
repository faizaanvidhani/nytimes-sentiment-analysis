from model import create_model
from preprocess import prepare_df
import hyperparameters as hp
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Import data
nyt_df = prepare_df(pd.read_csv (r'nyt_data/nyt_clean_data.csv'),['preprocessed_headline','preprocessed_article_summary','preprocessed_article_text'])
nyt_df.dropna(subset = ["preprocessed_article_text"], inplace=True)
train_df = prepare_df(pd.read_csv (r'sst_data/train.csv'),['text'])
# Fit the tokenizer on the training data
tokenizer = Tokenizer(num_words = hp.VOCAB_SIZE, oov_token=hp.OOV_TOKEN)
tokenizer.fit_on_texts(train_df['text'])
# 
sequences1 = tokenizer.texts_to_sequences(nyt_df['preprocessed_headline'])
# sequences2 = tokenizer.texts_to_sequences(nyt_df['preprocessed_article_summary'])
sequences3 = tokenizer.texts_to_sequences(nyt_df['preprocessed_article_text'])

pad1 = pad_sequences(sequences1, maxlen=hp.MAX_LENGTH, padding=hp.PADDING_TYPE, truncating=hp.TRUNC_TYPE)
# pad2 = pad_sequences(sequences2, maxlen=hp.MAX_LENGTH, padding=hp.PADDING_TYPE, truncating=hp.TRUNC_TYPE)
pad3 = pad_sequences(sequences3, maxlen=hp.MAX_LENGTH, padding=hp.PADDING_TYPE, truncating=hp.TRUNC_TYPE)

model = create_model()
model.load_weights('saved_model/model4.ckpt')

probabilities1 = model.predict(pad1)
headline_ratings = np.argmax(probabilities1,axis=1)
# summary_ratings = model.predict(pad2)
probabilities3 = model.predict(pad3)
text_ratings = np.argmax(probabilities3,axis=1)
nyt_df.insert(nyt_df.shape[1],'headline_ratings',headline_ratings)
nyt_df.insert(nyt_df.shape[1],'text_ratings',text_ratings)
nyt_df.to_csv('updated_nyt_data.csv', index=False)