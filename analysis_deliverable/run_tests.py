from scipy.stats import ttest_ind, ttest_rel, f_oneway, levene
import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel, chi2_contingency

def hypothesis_test_one(df):
    """
    Hypothesis 1:
        -Is there a significant difference between the sentiment scores of a headline and its corresponding article?
    H0:
        -The mean difference in sentiment scores between headlines and their corresponding articles is zero. 
        -Mathematically, uD = uH - uA =  0.
    Ha:
        -The mean difference in sentiment scores between headlines and their corresponding articles is not zero. 
        -Mathematically, uD = uH - uA !=  0.
    Type of Test: Two-tailed paired t-test

    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    headline_ratings = df["headline_ratings"].to_numpy()
    text_ratings = df["text_ratings"].to_numpy()
    tstats, pvalue = ttest_rel(headline_ratings, text_ratings)
    return tstats, pvalue


def hypothesis_test_two(df):
    """
    Hypothesis Test #2
        -Are the sentiment scores of arts headlines significantly different from the sentiment scores of technology headlines?

    H0:
        -The mean sentiment score of arts headlines is equal to the mean sentiment score of technology headlines. 
        -Mathematically, uA = uT . 
    Ha:
        -The mean sentiment score of arts headlines is significantly different from the mean sentiment score of technology headlines. 
        -Mathematically, uA != uT .
    Type of Test: Two-tailed Two-sample t-test

    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    arts = df.query('category == "Arts"')
    tech = df.query('category == "Technology"')

    arts_headline_ratings = arts["headline_ratings"]
    tech_headline_ratings = tech["headline_ratings"]
    tstats, pvalue = ttest_ind(arts_headline_ratings, tech_headline_ratings)
    return tstats, pvalue


def hypothesis_test_three(df):
    """
    Hypothesis Test #3
        -Is the difference in sentiment scores for headlines and their corresponding articles the same across all authors?

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
    df_copy = df.copy()
    
    # Removing rows where there are multiple authors or an unknown author corresponding to a given article
    df_copy = df_copy[df_copy["authors"].str.contains(",")==False]
    df_copy = df_copy[df_copy["authors"].str.contains("Unknown")==False]
    
    df_copy['diff'] = df_copy['headline_ratings'] - df_copy['text_ratings']
    df_diffs = df_copy.groupby('authors')['diff'].apply(list).reset_index(name='diff list')
    
    # Obtaining a list of the differences in the sentiment ratings between headlines and articles for all authors
    diff_lists = df_diffs['diff list'].to_list()

    # Levene's test can be carried out to check that variances are equal for all samples before running one-Way ANOVA. 
    _, lev_p = levene(*diff_lists)
    if lev_p < 0.05:
        print("Homogeneity of variances condition is NOT met. Cannot proceed with one-way ANOVA.")
        return None, None
    else:
        print("Homogeneity of variances condition is met! Proceeding with one-way ANOVA.")
    F, p = f_oneway(*diff_lists)
    return F, p

if __name__ == "__main__":
    df = pd.read_csv('updated_nyt_data.csv')

    # HYPOTHESIS TEST #1
    print("Running Hypothesis Test #1...")
    tstats1, pvalue1 = hypothesis_test_one(df)
    print("Hypothesis Test #1 Results - tstats: " + str(tstats1) + ", pvalue: " + str(pvalue1))

    # HYPOTHESIS TEST #2
    print("Running Hypothesis Test #2...")
    tstats2, pvalue2 = hypothesis_test_two(df)
    print("Hypothesis Test #2 Results - tstats: " + str(tstats2) + ", pvalue: " + str(pvalue2))

    # HYPOTHESIS TEST #3
    print("Running Hypothesis Test #3...")
    F, p = hypothesis_test_three(df)
    print("Hypothesis Test #3 Results - F-value: " + str(F) + ", pvalue: " + str(p))
