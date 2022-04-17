import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.stem.snowball import SnowballStemmer
st = SnowballStemmer('english')


conn = sq3.connect('data.db')

text_query = """
SELECT id, authors, pub_date, category, sub_category, headline, print_headline, article_summary, article_text, web_url
FROM nyt_articles
"""

df = pd.read_sql(text_query, conn)

def clean_data(df, col, clean_col):
    # change to lower and remove spaces on either side
    df[clean_col] = df[col].apply(lambda x: x.lower().strip())

    # remove extra spaces in between
    df[clean_col] = df[clean_col].apply(lambda x: re.sub(' +', ' ', x))

    # remove punctuation
    df[clean_col] = df[clean_col].apply(lambda x: re.sub('[^\w\s]', ' ', x))

    # remove stopwords and get the stem
    df[clean_col] = df[clean_col].apply(lambda x: ' '.join(st.stem(text) for text in x.split() if text not in stop_words))

    return df

df = clean_data(df, 'headline', 'preprocessed_headline')
df = clean_data(df, 'article_summary', 'preprocessed_article_summary')
df = clean_data(df, 'article_text', 'preprocessed_article_text')

df.to_csv('cleaned_nyt.csv')