# Code README

## Data Scraper:

At a high level our data scraper is very simple in its functionality and design. Essentially, the inner workings of the scrapper can be broken down into the following steps: 

1.	Retrieve Data from New York Times API
2.	Scrape Article Text
3.	Process Data
4.	Save Data to Database

*Before going further into the functionality of our scraper it is important to note that for our scraper to work you must provide it with an active API key to the New York Times Developer Portal. You can find more information about this here: https://developer.nytimes.com*

Given an API key, our scraper uses the Python “requests” module to create a GET request to retrieve articles from 2018-2022 from the following categories: Business Day, Technology, Science, Education, Arts, Health, and Opinion. The NYT API however only lets you create a GET request for 10 articles at a time and imposes a mandatory 6 request limit per minute. To solve this issue, we made sure to add a 10 second pause between each GET request our scraper made which unfortunately made get article data take a long time. 

The data response returned by each GET request included useful information such as article headline, publication date, article URL, and article authors but does not include the full text of an article. To retrieve this information, we decided to use the Python Beautiful Soup package to scrape each article’s text. This was a relatively simple task since the New York Times used the same CSS styling tags across all their online publications meaning we could extract article text using the same Beautiful Soup Script. However, it is important to note that we discovered the New York Times periodically change the name of these tags to prevent continous scraping so if the scraper doesn't work this could be a potential area to look into.

Once, we had all our data we went ahead and cleaned it using the NLTK processing library and removed things such as punctuation and stop words along with tokenizing our text and preforming lemmatization. With all our data cleaned and pre-processed we went ahead and added it to our SQLite database. 

To run our scraper, you must first create an valid API key and run the scraper.py file from your terminal. 

## LSTM Model:

For our machine learning model we decided to use an LSTM architecture given that they are used in lots of NLP tasks including sentiment analysis due to their architecture being well suited for handling long sequential data such as text based documents. Other ML algorithms that we considered using included lexicon-based methods such as AFINN, Textblob, and VADER but decided to opt for an LSTM model we could individually train and test. Similarly, we found that accuracies for Textblob and VADER on the SST-5 have been reported to be 28.4% and 31.5% which is lower than what our LSTM model was able to achieve. We also tried to evaluate our article dataset using AFINN but realized that the range of sentiment values varied significantly with the lowest article headline sentiment score being -9 and the highest being 7 and for article texts the lowest score was -138 and the highest was 196. This was most likely due to the fact that AFINN sentiment scores can vary dramatically with longer texts, which is why we opted not to use this model.

To use our LSTM model just run the results.py script in your terminal. The results.py file can be found in the final_deliverable/model folder.  
