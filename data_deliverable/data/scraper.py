from pprint import pprint
import requests
import sqlite3
import time
from bs4 import BeautifulSoup
import string
from config import apikey, headers
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
import math

def get_articles(apikey, section_name, page, date):
    begin_date = date[0]
    end_date = date[1]
    query = f'document_type:(\"article\") AND type_of_material:(\"News\") AND section_name:(\"{section_name}\")'
    page = str(page)  # <0-100>
    sort = "relevance" # newest, oldest
    query_url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?" \
                f"fq={query}" \
                f"&api-key={apikey}" \
                f"&begin_date={begin_date}" \
                f"&end_date={end_date}" \
                f"&page={page}" \
                f"&sort={sort}"

    time.sleep(6) 

    # Query NYT API
    r = requests.get(query_url)
    json_obj = r.json()
    response_obj = json_obj["response"]
    
    # Extract API Response Data
    articles = []
    article_list = response_obj['docs']
    for article in article_list:
        authors = extract_authors(article['byline']['person'])
        headline = article['headline']['main']
        pub_date = article['pub_date']
        category = article['section_name']
        web_url = article['web_url']
        article_summary = article['snippet']
        article_text = get_text(web_url)

        print_headline = article['headline']['print_headline']
        if 'subsection_name' in article:
            sub_category = article['subsection_name']
        else:
            sub_category = None

        articles.append({
            'authors': authors,
            'headline': headline,
            'print_headline': print_headline,
            'pub_date': pub_date,
            'category': category,
            'article_summary': article_summary,
            'sub_category': sub_category,
            'web_url': web_url,
            'article_text': article_text,
        })

    return articles

def extract_authors(author_data):
    authors = []
    if len(author_data) > 0:
        for author in author_data:
            firstname = 'Unknown'
            lastname = ''
            if 'firstname' in author and author['firstname'] != None:
                firstname = author['firstname']
            if 'lastname' in author and author['lastname'] != None:
                lastname = author['lastname']
            authors.append(firstname + ' ' + lastname)
    return authors

def get_text(web_url):
    req = requests.get(web_url, headers=headers)
    req.raise_for_status() # Raises an error if the request fails
    bs = BeautifulSoup(req.content, 'html.parser')
    paragraphs = bs.find_all("p", {"class":"css-g5piaz evys1bk0"})

    full_text = ''
    for p in paragraphs:
        full_text = full_text + ' ' + p.text

    return full_text

def create_tables(conn):
    curr = conn.cursor()
    # Delete tables if they exist
    curr.execute('DROP TABLE IF EXISTS "nyt_articles";')

    sql_create_nyt_articles_table = """ CREATE TABLE IF NOT EXISTS nyt_articles (
                                            id integer primary key autoincrement,
                                            authors text,
                                            pub_date text,
                                            category text,
                                            sub_category text,
                                            headline text,
                                            preprocessed_headline text,
                                            print_headline text,
                                            preprocessed_print_headline text,
                                            article_summary text,
                                            preprocessed_article_summary text,
                                            article_text text,
                                            preprocessed_article_text,
                                            web_url text
                                        ); """

    curr.execute(sql_create_nyt_articles_table)

def add_article_data(conn, data):
    curr = conn.cursor()
    authors = 'Unknown'
    if len(data['authors']) > 0: 
        authors = ', '.join(data['authors'])

    headline = data['headline']
    print_headline = data['print_headline']
    pub_date = data['pub_date']
    category = data['category']
    article_summary = data['article_summary']
    sub_category = data['sub_category']
    article_text = data['article_text']
    web_url = data['web_url']

    preprocessed_headline = preprocess(data['headline'])
    preprocessed_print_headline = preprocess(data['print_headline']) if data['print_headline'] else None
    preprocessed_article_summary = preprocess(data['article_summary']) if data['article_summary'] else None
    preprocessed_article_text = preprocess(data['article_text'])
   
    command = ''' INSERT INTO nyt_articles(authors,
                                        pub_date,
                                        category,
                                        sub_category, 
                                        headline,
                                        preprocessed_headline,
                                        print_headline,
                                        preprocessed_print_headline,
                                        article_summary,
                                        preprocessed_article_summary,
                                        article_text,
                                        preprocessed_article_text,
                                        web_url)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    items = (authors, pub_date, category, sub_category, headline, preprocessed_headline, print_headline, preprocessed_print_headline, article_summary, preprocessed_article_summary, article_text, preprocessed_article_text, web_url)
    curr.execute(command, items)
    conn.commit()

# converts string to lowercase,remove punctuation, remove stop words
def preprocess(text):
    # convert to lower case
    s = text.lower()

    # remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    
    # remove stop words
    s_tokens = word_tokenize(s)
    tokens_without_sw = [word for word in s_tokens if not word in stopwords.words()]

    # lemmatize list of words
    lemmatizer = WordNetLemmatizer()
    lemmatized_output = ' '.join([lemmatizer.lemmatize(word) for word in tokens_without_sw])

    return lemmatized_output

def get_num_pages(dates):
    categories = {
        "Business Day" : [],
        "Technology" : [],
        "Science" : [],
        "Education" : [],
        "Arts" : [],
        "Health" : [],
        "Opinion" : []
    }
    
    for date in dates: 
        begin_date = date[0]
        end_date = date[1]
        for category in categories:
            query = f'document_type:(\"article\") AND type_of_material:(\"News\") AND section_name:(\"{category}\")'
            query_url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?" \
                        f"fq={query}" \
                        f"&begin_date={begin_date}" \
                        f"&end_date={end_date}"\
                        f"&api-key={apikey}" \
                      
            time.sleep(6) 
            r = requests.get(query_url)
            json_obj = r.json()
            response_obj = json_obj["response"]
            hits = response_obj['meta']['hits']
            num_pages = 5 if hits > 50 else math.ceil(hits / 10)
            categories[category].append(num_pages)
        
    return categories

def main():
    dates = [
        ("20180101","20181231"),
        ("20190101", "20191231"),
        ("20200101", "20201231"),
        ("20210101", "20211231"),
        ("20220101", "20221231")
    ]
    
    pages_per_category_per_year = get_num_pages(dates)
    print(pages_per_category_per_year)
    articles = []
   

    for idx, date in enumerate(dates):
        print(f"Getting Data for {date}")
        for category in pages_per_category_per_year: 
            print(f"Getting Data for {category}")
            num_pages = pages_per_category_per_year[category][idx]
            print(f"Number of Pages: {num_pages}")
            # for page in range(num_pages):
            for page in range(num_pages):
                print(f"Page: {page}")
                articles += get_articles(apikey, category, page, date)
               
    conn = sqlite3.connect('data.db')
    create_tables(conn)

    for article in articles:
        add_article_data(conn, article)

    conn.close()

if __name__ == "__main__":
    main()