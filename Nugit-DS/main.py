#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr
import json
from collections import OrderedDict
from linear_regression import linear_regression


def sectionA(X, y):
    """
    Attributes: Independent Variables, X (pandas.DataFrame),
                Dependent Variable, y (pandas.DataFrame).
    Function computes quantities asked in SectionA.
    Returns linear model, gradient, intercept, max SEM, max SEM impact on SEO,
    median SEM, median SEM impact on SEO

    """
    # Import linear_regression function
    linear_fit = linear_regression(X, y, plot_flag=False)

    maxSEM = max(input_data['SEM'].values)
    maxSEMimpact = linear_fit.predict(maxSEM)

    medianSEM = np.median(input_data['SEM'].values)
    medianSEMimpact = linear_fit.predict(medianSEM)

    return linear_fit, round(linear_fit.coef_, 2), round(linear_fit.intercept_, 2),\
        int(maxSEM), int(maxSEMimpact), int(medianSEM), int(medianSEMimpact)


def sectionB(linear_fit, X, y):
    """
    Attributes: Regressor, linear_fit (linear_model.base.LinearRegression),
                Independent Variables, X (pandas.DataFrame),
                Dependent Variables, y (pandas.DataFrame).
    Function returns correlation coefficient and coefficient of determination
    as tuple.
    """

    r, _ = pearsonr(X.values, y.values)
    rsquared = linear_fit.score(X, y)
    return round(r, 3), round(rsquared, 3)


def sectionC(filename, data, dataranges):
    """
    Attributes: File Name, filename (str),
                Dataset, data (pandas.DataFrame)
                Data Range, dataranges (list)

    Function to calculate the quantities asked in SectionA and SectionB for
    different dataranges.
    Returns a list of dictionaries with values ordered as given in sample
    output.
    """

    keys = ['filename', 'datarange', 'gradient', 'yintercept', 'maxSEM',
            'maxSEMimpact', 'medianSEM', 'medianSEMimpact', 'r', 'rsquared']
    list_output = []

    for datarange in dataranges:

        # Reduce data set for the datarange
        data_reduced = data[-datarange:]

        # To be consistent with the sample output
        datarange = str(datarange) + 'weeks'

        X = data_reduced[['SEM']]
        y = data_reduced[['SEO']]

        linear_fit, gradient, yintercept, maxSEM, maxSEMimpact, medianSEM,\
        medianSEMimpact = sectionA(X, y)

        r, rsquared = sectionB(linear_fit, X, y)
        # Build an Ordered Dictionary as given in sample output
        output = OrderedDict([(k, locals()[k]) for k in keys])
        list_output.append(output)

        # Outlier check
        # outliers = data_reduced[get_outlier_idx(linear_fit, X, y)]
        # print outliers

    return list_output


def get_outlier_idx(linear_fit, X, y):

    errors = (y - linear_fit.predict(X))
    outlier_idx = errors.values >= np.percentile(errors.values, 75)
    return outlier_idx


if __name__ == '__main__':
    # To run: python main.py

    # Read data from csv using pandas as a DataFrame
    file_name = 'data/sample_data_Oct.csv'
    print ('Reading data from \"' + str(file_name)) + '\"'
    input_data = pd.DataFrame.from_csv(file_name, sep='\t', index_col=False)

    # For the dataranges as asked in SectionC, using code template as
    # was provided in the example
    num_weeks = [26, 12]
    print ("Computing Regression for " + str(num_weeks) + " weeks")
    result = sectionC(file_name, input_data, num_weeks)

    # Write results in json
    print ("Writing results to " + "output.json")
    with open('output.json', 'w') as outfile:
        json.dump(result, outfile, indent=2)
