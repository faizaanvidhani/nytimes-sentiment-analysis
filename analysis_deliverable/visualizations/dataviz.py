from utils import *
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import plotly.figure_factory as ff
import seaborn as s


#global variable name for column
h_score = '???'
a_score = '???'


def parse_args():
    """
    Parses the CLI args with argparse
    :return: args from command line
    """
    parser = argparse.ArgumentParser(description='Machine Learning song_clustering (Problem 2)')
    parser.add_argument('-d', help='path to data file', default='../data/ml/spotify.csv')
    parser.add_argument('-o', help='path to output data directory', default='output')
    return parser.parse_args()



#H1: Is there a significant difference between the sentiment scores of a headline and its corresponding article?
def plot_sentiment_box():
    '''
    Plots a histogram displaying differences between sentiment scores
    '''
    pass




# H2: Are the sentiment scores of arts headlines significantly different from the sentiment scores of technology headlines?
def plot_category_bar(a,b):
    """
    Plots a two-key bar graph displaying the article count per sentiment score for categories a and b
    Inputs:
    - a : first category we want to compare
    - b : second categry we want to compare
    """
    df = pd.read_csv("cleaned_nyt.csv") 
    df = df.loc[ (df["Category"]== a) | (df["Category"]== b) ] 

    df = df[df["Category",h_score]]
    df['frequency'] = df[h_score].map(df[h_score].value_counts()) 

    
    graph = sns.catplot( data = df,
                         kind = 'bar'
                         x = h_score 
                         y = count,
                         hue = "Category",
                         height = 10,
                         aspect = 10 )

    graph.set(title = "Sentiment Scores for News Headlines in Arts and Technology")

def plot_category_box(a,b):
    """
    Plots box plot for average sentiment score for categories a and b
    """
    pass




# H3: Is the mean difference in sentiment scores for headlines and their corresponding articles for a given author the same across all authors?
def plot_author_line():
    '''
    Plots a line graph containing the headline and article sentiment scores across authors, in addition to line graph displaying mean difference
    '''
    pass

  
  
