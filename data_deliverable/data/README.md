# :newspaper: Breaking News Data Spec

Welcome to the Breaking News Data Spec! Some important things to note before diving into our wonderful datasets and their attributes. First, you should note that there are two data sets included in this spec: `SST-5 Fine-Grdained Classificaition` and `nyt_articles` (currently called data.db). The `SST-5 Fine-Grdained Classificaition` data will be used to train our ML model to then later perform sentiment analyis on the `nyt_articles` data we collected. For more information please continue reading and we hope you enjoy!

# SST-5 Fine-Grained Classification Dataset Spec 

### Creating the Model: 
For our project we will be training a model to conduct sentiment analysis using the SST-5 Fine-grained classification dataset. The dataset turns the typical sentiment analysis from what is typically a binary classification problem into a multi-class classification problem by introducing integer labels ranging from 0 - 4 (inclusive), detailing a Strongly Negative, Weakly Negative, Neutral, Weakly Positive, and Strongly Positive sentiments respectively. The labels are attributed to 11,855 sentences extracted from movie reviews. If we choose to, we can also leverage the 215,154 phrases that comprise the sentences in the reviews in order to conduct an even finer grained analysis. Further information is provided in the 
Attributes for our data where extracted SST-5 Fine-Grained Classification Dataset. 

**Links to Data:**

[Treeset Download Link](https://nlp.stanford.edu/sentiment/index.html)

[Raw Text Link](https://drive.google.com/drive/folders/1TYR-yRw3NXqfXnMSvFDxGTdf1urGfrPY)

[Sample Data Link](https://docs.google.com/spreadsheets/d/1mu5RmXbWU3va15VOGFOvOljR2aPsFQwDX5G4TKLzG04/edit#gid=0)


### Data Attributes: 
**`rating:`** Numerical rating of the movie review's sentiment.

| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `Integer`          |
| Range            | 0 - 4  (inclusive) |
| Required         | :heavy_check_mark: |

Distribution of Ratings in Test Set 
(should be representative of entire dataset)
| Rating           |     Occurences     |  
| -------------    |:-------------:     |
| 0                |        278         |
| 1                |        633         |
| 2                |        389         |
| 3                |        510         |
| 4                |        399         |


**`text:`** The text review
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Required         | :heavy_check_mark: |


# nyt_articles Data Set:

Attributes for our data where extracted from the response object returned by querying the New York Times (NYT) Article Search API. Only the `article_text` attribute is not part of the JSON object returned by the NYT API. The data found in the `article_text` feild was scraped using the `url` returned by the NYT API. 

**NYT Article Search API:**
https://developer.nytimes.com/docs/articlesearch-product/1/overview

### NYT Article Search API JSON Response:

The following demonstrates the JSON response object for the feilds we decided to extract. For the full schema of the response object returned by NYT Article Search API refer to this [Link](https://developer.nytimes.com/docs/articlesearch-product/1/routes/articlesearch.json/get)
```json=
response: {
    docs: {
        article {
            web_url: string,
            snippet: string,
            headline: {
                main: string,
                print_headline: string
            },
            pub_date: string,
            byline: {
                person: Array {
                    firstname: string
                    lastname: string  
                }
            },
            section_name: string,
            subsection_name: string,
        }  
    }
}
```

Our Data Attributes: 
----
**`id:`** Primary key used to identify each unique article in our database.

| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `Integer`          |
| Default Value    | We use SQLs autoincrement to assign primary keys as we input new rows into our database so the default value is always the next integer in the autoincrement funciton.  |
| Range            | `0 - 1,425`        |
| Distribution     | :x:                |
| Identifier       | :white_check_mark: |
| Required         | :white_check_mark: |
| Unique Value     | :white_check_mark: |
| Used in Analysis | :x:                |
| Sensative Info   | :x:                |

**`authors:`** A string containing the author(s) of the article.
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | A string with the text `Unknown`  |
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :white_check_mark: |
| Unique Value     | :x:                |
| Used in Analysis | :x:                |
| Sensative Info   | :x:                |


**`pub_date:`** String representing the date in which the article was published. Example of date format:`2022-02-23T15:35:33+0000`
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `Empty String`     |
| Range            | `2018-01-01` to `2022-12-31`    |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :white_check_mark: |
| Unique Value     | :x:                |
| Used in Analysis | :white_check_mark: |
| Sensative Info   | :x:                |

**`category:`** String representing the article category assigned by the New York Times. Category values can be any of the following: `Business Day`, `Technology`, `Science`, `Education`, `Arts`, `Health`, `Opinion`
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `String`           | 
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :white_check_mark: |
| Unique Value     | :x:                |
| Used in Analysis | :white_check_mark: |
| Sensative Info   | :x:                |

**`sub_category:`** String representing the article sub-category type assigned by the New York Times. Category values can be found [here](https://developer.nytimes.com/docs/articlesearch-product/1/overview).
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `None`             |
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :x:                |
| Unique Value     | :x:                |
| Used in Analysis | :white_check_mark: |
| Sensative Info   | :x:                |

**`headline:`** A string representing the headline of an article.
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `Empty String`     |
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :white_check_mark: |
| Unique Value     | :white_check_mark: |
| Used in Analysis | :x:                |
| Sensative Info   | :x:                |

**`preprocessed_headline:`** A string representing an article headline after data cleaning including tokenization, stopword removal, punctuation removal, and lemminization.

| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `Empty String`     |
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :white_check_mark: |
| Unique Value     | :white_check_mark: |
| Used in Analysis | :white_check_mark: |
| Sensative Info   | :x:                |

**`print_headline:`** A string representing the print headline of the article. Only exists if the article was published in print and isn't just stored as a NYT online article.
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `None`             |
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :x:                |
| Unique Value     | :x:                |
| Used in Analysis | :x:                |
| Sensative Info   | :x:                |

**`preprocessed_print_headline:`** A string representing the print_headline after data cleaning including tokenization, stopword removal, punctuation removal, and lemminization.

| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `None`             |
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :x:                |
| Unique Value     | :x:                |
| Used in Analysis | :white_check_mark: |
| Sensative Info   | :x:                |


**`article_summary:`** A string representing the first few words in the article. Does not include the full article text but enough information to give the article context.
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `Empty String`     |
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :x:                |
| Unique Value     | :x:                |
| Used in Analysis | :x:                |
| Sensative Info   | :x:                |

**`preprocessed_article_summary:`** A string representing the article_summary after data cleaning including tokenization, stopword removal, punctuation removal, and lemminization.
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `Empty String`     |
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :x:                |
| Unique Value     | :x:                |
| Used in Analysis | :white_check_mark: |
| Sensative Info   | :x:                |

**`article_text:`** A string containing the full article text scraped from the New York Times.
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `String`           |
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :white_check_mark: |
| Unique Value     | :white_check_mark: |
| Used in Analysis | :white_check_mark: |
| Sensative Info   | :x:                |

**`preprocessed_article_text:`** A string representing the article_text after data cleaning including tokenization, stopword removal, punctuation removal, and lemminization.
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `String`           |
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :white_check_mark: |
| Unique Value     | :white_check_mark: |
| Used in Analysis | :white_check_mark: |
| Sensative Info   | :x:                |

**`url:`** A String containing the web url of an article.
| Values           |                    |  
| -------------    |:-------------:     |
| Type             | `String`           |
| Default Value    | `String`           |
| Range            | :x:                |
| Distribution     | :x:                |
| Identifier       | :x:                |
| Required         | :white_check_mark: |
| Unique Value     | :white_check_mark: |
| Used in Analysis | :x:                |
| Sensative Info   | :x:                |



