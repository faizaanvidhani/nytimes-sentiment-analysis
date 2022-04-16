import numpy as np
import pandas as pd
from util import all_variable_names_in_df
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel, chi2_contingency

def hypothesis_test_one(dataset):
    """
    Hypothesis 1:
        -Is there a significant difference between the sentiment scores of a headline and its corresponding article?
    H0:
        -The mean difference in sentiment scores between headlines and their corresponding articles is zero. 
        -Mathematically, uD = uH - uA =  0.
    Ha:
        -The mean difference in sentiment scores between headlines and their corresponding articles is not zero. 
        -Mathematically, uD = uH - uA !=  0.
    Type of Test: Paired t-test

    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """

def hypothesis_test_two(dataset):
    """
    Hypothesis Test #2
        -Are the sentiment scores for technology article headlines significantly greater than the sentiment scores for business day article headlines?

    H0:
        -The mean sentiment score of technology article headlines is equal to the mean sentiment score of business day article headlines. 
        -Mathematically, uT = uB . 
    Ha:
        -The mean sentiment score of technology article headlines is significantly greater than the mean sentiment score of business day article headlines. 
        -Mathematically, uT > uB .
    Type of Test: Two-sample t-test

    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """

def hypothesis_test_three(dataset):
    """
    Hypothesis Test #3
        -Is the difference in sentiment scores for a particular headline and its corresponding article the same across all authors?

    H0:
        -The difference in sentiment scores for a particular headline and its corresponding article is the same across all authors. 
        -Mathematically, u1 = u2 =...= uj  where j is the number of authors.
    Ha
        -The difference in sentiment scores for a particular headline and its corresponding article is not the same for all authors. 
        -Mathematically, ui != uk for at least one pair of i, k {1,2,...,j}, i != k.
    Type of Test: ANOVA

    Input:
        - dataset: A Pandas DataFrame
    Output:
        - F: F-value (float)
        - p: p-value (float)
    """
