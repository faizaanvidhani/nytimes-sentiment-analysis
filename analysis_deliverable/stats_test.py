import numpy as np
import pandas as pd
from util import all_variable_names_in_df
from scipy.stats import ttest_ind, ttest_rel, f_oneway


def paired_ttest(values_a, values_b):
    """
    Runs a paired t-test.
    """
    tstats, pvalue = ttest_rel(values_a, values_b)
    print("Paired t-test tstats: " + tstats)
    print("Paired t-test pvalue: " + pvalue)
    return tstats, pvalue

def two_sample_ttest(values_a, values_b):
    """
    Runs an two-sample t-test (i.e. independent samples t-test).
    """
    tstats, pvalue = ttest_ind(values_a, values_b)
    print("Two-sample t-test tstats: " + tstats)
    print("Two-sample t-test pvalue: " + pvalue)
    return tstats, pvalue

def one_way_ANOVA_test(values):
    """
    Runs a one-way ANOVA test.
    """
    F, p = f_oneway(values)
    print("One-way ANOVA test F-value: " + F)
    print("One-way ANOVA test p-value: " + p)
    return F, p