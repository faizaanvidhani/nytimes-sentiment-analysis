
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#global variable name for column
h_score = 'headline_ratings'
a_score = 'text_ratings'


#H1: Is there a significant difference between the sentiment scores of a headline and its corresponding article?
def sentiment_score_histogram(data):
 
    df0 = data.groupby("category")
    print(df0)
    df = data.groupby('category', as_index=False)['headline_ratings'].mean()
    df = df.rename(columns={"headline_ratings": "mean"})
    df['text_type'] = 'headline'

    df2 = data.groupby('category', as_index=False)['text_ratings'].mean()
    df2 = df.rename(columns={"text_ratings": "mean"})
    df2['text_type'] = 'article'

    result = pd.concat([df, df2])
    fig, axs = plt.subplots()
    fig.set_size_inches(10, 6)
    fig.tight_layout()

    graph = sns.catplot(
        data=result, 
        kind="bar",
        x="category", 
        y="mean", 
        hue="text_type", 
        palette="dark", 
        alpha=.6, 
        height=6
    )
    plt.ylim(0, 3)
    plt.show()


def plot_sentiment_box():
    '''
    Plots a histogram displaying differences between sentiment scores
    '''
    pass




# H2: Are the sentiment scores of arts headlines significantly different from the sentiment scores of technology headlines?
def plot_category_bar(a, b, data):
    """
    Plots a two-key bar graph displaying the article count per sentiment score for categories a and b
    Inputs:
    - a : first category we want to compare
    - b : second categry we want to compare
    - data: The data used to make the visualization
    """

    df = data.loc[(data["category"]== a) | (data["category"]== b) ] 
    df = df.groupby([h_score, 'category'], as_index=False).size()

    df = df.rename(columns={"category": "Article Category"})
    
    fig, axs = plt.subplots()
    fig.set_size_inches(10, 6)
    fig.tight_layout()

    graph = sns.catplot(
        data=df, 
        kind="bar",
        x="headline_ratings", 
        y="size", 
        hue="Article Category", 
        palette="dark", 
        alpha=.6, 
        height=6
    )

    graph.despine(left=True)
    graph.set_axis_labels("Sentiment Score", "Number of Articles")
    graph.set(title = "Sentiment Scores for News Headlines in Arts and Technology")
    plt.subplots_adjust(top=0.9)
    plt.show()

def h2_box_plot(data):

    art_articles = data.loc[(data["category"] == 'Arts')]
    tech_articles = data.loc[(data["category"] == 'Technology')]
    
    fig, axs = plt.subplots(ncols=2)
    fig.tight_layout()
    fig.set_size_inches(9, 5)
    fig.suptitle('Distribution of Sentiment Scores for Art and Technology Articles', fontweight='bold')
    fig.subplots_adjust(top=.9)
    fig.subplots_adjust(bottom=.1)
    
    sns.boxplot(y=art_articles['headline_ratings'], color='#377eb8', ax=axs[0])
    sns.boxplot(y=tech_articles['headline_ratings'], color='#ff7f00', ax=axs[1])
    # graph1 = sns.histplot(data=art_articles, x="headline_ratings", color='#377eb8', ax=axs[0])
    # graph2 = sns.histplot(data=tech_articles, x="headline_ratings", color='#ff7f00', ax=axs[1])

    plt.show()

# # H3: Is the mean difference in sentiment scores for headlines and their corresponding articles for a given author the same across all authors?
def plot_author_line():
    '''
    Plots a line graph containing the headline and article sentiment scores across authors, in addition to line graph displaying mean difference
    '''
    pass

  
  
if __name__ == "__main__":
    data = df = pd.read_csv("../updated_nyt_data.csv")
    sentiment_score_histogram(data)
    # h2_box_plot(data)
    # plot_category_bar('Arts', 'Technology', data)
