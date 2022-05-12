import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict


#global variable name for column
h_score = 'headline_ratings'
a_score = 'text_ratings'


#H1: Is there a significant difference between the sentiment scores of a headline and its corresponding article?
def sentiment_score_histogram(data):

    df_headline = data[['category', 'headline_ratings']]
    df_headline = df_headline.groupby('category', as_index=False)['headline_ratings'].mean()
    print(df_headline)
    df_headline['Text Type'] = 'Headline'
    df_headline = df_headline.rename(columns={"headline_ratings": "mean"})

    df_text = data[['category', 'text_ratings']]
    df_text = df_text.groupby('category', as_index=False)['text_ratings'].mean()
    df_text['Text Type'] = 'Article'
    df_text = df_text.rename(columns={"text_ratings": "mean"})

    result = pd.concat([df_headline, df_text])

    graph = sns.catplot(
        data=result, 
        kind="bar",
        x="category", 
        y="mean", 
        hue="Text Type", 
        palette="dark", 
        alpha=.6, 
        height=6
    )

    graph.set_axis_labels("News Category", "Mean Sentiment Score")
    graph.set(title = "Mean Sentiment Scores by Category for Articles and Headlines")
    graph.fig.subplots_adjust(top=.9)
    
    plt.ylim(0, 3)
    plt.show()


# H2: Are the sentiment scores of arts headlines significantly different from the sentiment scores of technology headlines?
def plot_category_bar(a, b, data):
    """
    Plots a two-key bar graph displaying the article count per sentiment score for categories a and b
    Inputs:
    - a : first category we want to compare
    - b : second categry we want to compare
    - data: The data used to make the visualization
    """

    # Getting data for article categories of interest
    df = data.loc[(data["category"]== a) | (data["category"]== b) ] 

    # Grouping Data by Headline Ratings and Category
    df = df.groupby(["headline_ratings", 'category'], as_index=False).size()

    # Converting Numerical Sentiment Score to Category Value
    sentiment_score_mapping = {
        0: "Strongly Negative",
        1: "Weakly Negative",
        2: "Neutral",
        3: "Weakly Positive",
        4: "Strongly Positive"
    }

    df = df.replace({"headline_ratings": sentiment_score_mapping})
    df = df.rename(columns={"category": "Article Category"})
    
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
    graph.set_axis_labels("Article Sentiment", "Number of Articles")
    graph.set(title = "Art Articles vs Technology Articles Sentiment Analysis")
    plt.subplots_adjust(top=0.9)
    plt.show()

def h2_box_plot(data):

    df = data[["category", "headline_ratings"]]
    business_articles = df.loc[(data["category"] == 'Business Day')]
    tech_articles = df.loc[(data["category"] == 'Technology')]
    science_articles = df.loc[(data["category"] == 'Science')]
    education_articles = df.loc[(data["category"] == 'Education')]
    art_articles = df.loc[(data["category"] == 'Arts')]
    health_articles = df.loc[(data["category"] == 'Health')]
    opinion_articles = df.loc[(data["category"] == 'Opinion')]

    data_dict = {
        "Business" : business_articles['headline_ratings'],
        "Technology": tech_articles['headline_ratings'],
        "Science" : science_articles['headline_ratings'],
        "Education" : education_articles['headline_ratings'],
        "Art" : art_articles['headline_ratings'],
        "Health" : health_articles['headline_ratings'],
        "Opinion" : opinion_articles['headline_ratings']
    }
    
    fig, ax1 = plt.subplots(figsize=(9, 4))
    fig.tight_layout()
    fig.set_size_inches(9, 5)
    fig.suptitle('Distribution of Headline Sentiment Scores by Article Category')
    fig.subplots_adjust(top=.9)
    fig.subplots_adjust(bottom=.1)
    
    bplot = ax1.boxplot(data_dict.values(), vert=True, patch_artist=True, labels=data_dict.keys())

    colors = ['#227C9D', '#17C3B2', '#FFCB77', '#FEF9EF', '#FE6D73', '#CBB3BF', '#EF959C']
    
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    ax1.set_xlabel("News Category")
    ax1.set_ylabel("Headline Sentiment Score")
   
    plt.show()


def get_value_counts_table(df, col_name):
    # get counts
    count_dict = defaultdict(int)
    def update_count_dict(r):
        count_dict[r[col_name]] += 1
    df.apply(lambda x: update_count_dict(x), axis=1)
    rows = [[e, count_dict[e]] for e in count_dict]
    count_df = pd.DataFrame(rows, columns=[col_name, "count"])
    x = count_df.sort_values(by=['headline_ratings'])

    # combine 0 and 1 into 'Negative'
    df_negs = x.copy()
    df_negs.loc[df_negs['headline_ratings'] < 2, 'headline_ratings'] = 1
    df_negs = df_negs.groupby('headline_ratings')['count'].sum().reset_index()

    # combine 3 and 4 into 'Positive'
    df_pos = df_negs.copy()
    df_pos.loc[df_pos['headline_ratings'] > 2, 'headline_ratings'] = 3
    df_pos = df_pos.groupby('headline_ratings')['count'].sum().reset_index()


    return df_pos


def art_pie_chart(data):
    # # TODO: Create a figure with just one subplot - hint: the link above
    my_fig, my_ax = plt.subplots(1)

    # TODO: Redefine somewhat_better_plot to satisfy the aforementioned requirements
    # Note: The amount of space should not represent how many things you should pass
    # into the .plot function call!
    somewhat_better_plot = data["count"].plot(kind='pie',
                                                            autopct='%1.1f%%',
                                                            pctdistance=1.2,
                                                            labeldistance=1.2,
                                                            startangle=90,
                                                            title = "Proportion of Arts Headlines by Sentiment Rating",
                                                            ax=my_ax,
                                                            colormap="RdYlGn",
                                                            labels=["" for e in data["headline_ratings"]])



    # TODO: Pass in the review_count_table["review_reason_code"] as the label to draw
    # the legend on the Axes my_ax
    my_ax.set_ylabel("")
    plt.legend(['Negative', 'Positive'], bbox_to_anchor=(.9, .85))
    plt.show()

def tech_pie_chart(data):
    # # TODO: Create a figure with just one subplot - hint: the link above
    my_fig, my_ax = plt.subplots(1)

    # TODO: Redefine somewhat_better_plot to satisfy the aforementioned requirements
    # Note: The amount of space should not represent how many things you should pass
    # into the .plot function call!
    somewhat_better_plot = data["count"].plot(kind='pie',
                                                            autopct='%1.1f%%',
                                                            pctdistance=1.2,
                                                            labeldistance=10000,
                                                            startangle=90,
                                                            title = "Proportion of Technology Headlines by Sentiment Ratings",
                                                            ax=my_ax,
                                                            colormap="RdYlGn",
                                                            labels=["" for e in data["headline_ratings"]])



    # TODO: Pass in the review_count_table["review_reason_code"] as the label to draw
    # the legend on the Axes my_ax
    my_ax.set_ylabel("")
    plt.legend(['Negative', 'Neutral', 'Positive'], bbox_to_anchor=(.9, .85))
    plt.show()

  
  
if __name__ == "__main__":
    data = df = pd.read_csv("../updated_nyt_data.csv")
    # sentiment_score_histogram(data)
    # h2_box_plot(data)
    # plot_category_bar('Arts', 'Technology', data)
    arts = data[data['category'] == 'Arts']
    tech = data[data['category'] == 'Technology']
    arts_headline_counts = get_value_counts_table(arts, "headline_ratings")
    tech_headline_counts = get_value_counts_table(tech, "headline_ratings")
    art_pie_chart(arts_headline_counts)
    tech_pie_chart(tech_headline_counts)
    print(arts_headline_counts)
    print(tech_headline_counts)