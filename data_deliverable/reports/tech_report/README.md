# Tech Report

### Where is the data from?
* The New York Times article was collected from the New York Times, a liberal American newspaper based in NYC.  
* The data was web-scraped using NYCI API. 

### How did you collect your data?
* The New York Times article was collected from the New York Times, a liberal American newspaper based in NYC.  
* The data was web-scraped using NYCI API. 

### Is the source reputable?
* Since the NYT is a highly reputable newspaper, this source of data also appears to be very reputable. 
* We have concerns regarding the target audience of the NYT. 
* Since the NYT caters to a largely liberal audience, the views presented in the articles may be skewed to be more liberal

### How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?
* The sample is comparably large as it contains records ranging from 2022 to 2018. Since the sample spans a few years, the sample is fairly representative of the recent content in the NYT.

### Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)
* Our only concern is that the newspaper may be slightly biased towards a more liberal demographic, which could be something that we need to take into consideration when testing our hypotheses and forming conclusions

### How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently, but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)
* We performed an initial check of the cleanliness by closely inspecting the data and brainstorming ways in which we could enhance the cleanliness
* Our reference for cleanliness is the guidelines specified in class regarding NLP 

### How many data points are there total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)? Do you think this is enough data to perform your analysis later on?
* We have 1,425 records in our nyt_articles database
* The NYT articles can be split into groups with the following number of articles in each group:
Business: 250
Technology: 250
Science: 250
Education: 85
Arts: 250
Health: 250
Opinion: 90
* 1,425 records is a sufficient enough sample size to conduct our analyses
* If needed, we are able to collect more data from the NYC data

### Are there missing values? Do these occur in fields that are important for your project's goals?
* Upon inspection, we see that some entries in our data set lack author names.
* Some entries are not classified as a particular sub category 
* Certain entries lack print headline values

### Are there duplicates? Do these occur in fields that are important for your project's goals?
* Some entries have duplicate values for the ‘headline’ attribute. For example, some articles have “Bulletin Board” as the headline, which is a generic headline that was not created based on the content of a given article.
* For our purposes, it is best if we remove such entries since our hypotheses depend on specific headlines as opposed to generic headlines

### How is the data distributed? Is it uniform or skewed? Are there outliers? What are the min/max values? (focus on the fields that are most relevant to your project goals)
* Since we are primarily dealing with text processing, we do not have a specific distribution or outliers in the data.
* All values in the New York City dataset are from the same time period. 

### Are there any data type issues (e.g. words in fields that were supposed to be numeric)? Where are these coming from? (E.g. a bug in your scraper? User input?) How will you fix them?
* None at the moment, probably be fixed by re-evaluation of scraper

### Do you need to throw any data away? What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw?
* Since our data was collected from the NYT API and is fairly clean we don’t anticipate needing to throw away any data. 

### Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. (approximately 3-5 sentences)
* The biggest challenge that we encountered was having to scrape the text for each article in our database due to the amount of time it took to collect our data. For example, we first had to query the NYT API to get articles meeting our requirements, then scrape the article text using the url provided from the api response, then preprocess the text, and finally insert it into our database. Since there is a query limit per minute on the NYT API and since we had to scrape and preprocess our data it took significantly longer than we had expected. In the future we could optimize the way we implement this. Now that our data is collected our next steps are the following: training our sentiment analysis model, running it on our NYT dataset, and performing data analysis on our model’s results. 
