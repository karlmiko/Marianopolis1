'''This file contains the code to compute the covariance and
correlations between the measurements (dependent variables) and the
species name (independent variable).

'''

from statistics import mean, pstdev

def covariance(v1, v2):
    '''Compute the covariance between two vectors v1 and v2.'''
    if len(v1) != len(v2):
        print('Error: vectors must have the same length!')
        return -1
    mean1 = mean(v1)
    mean2 = mean(v2)
    total = 0
    # zip() is a builtin function that "zips together" two lists into
    # a single iterable object where each element is a tuple containing
    # a pair of values, one from each list. We will cover it in more
    # detail in class.
    for x1, x2 in zip(v1, v2):
        total += (x1 - mean1) * (x2 - mean2)
    return total / len(v1)

def correlation(v1, v2):
    '''Compute the correlation (Pearson's R score) between a dependent
    and an independent variable, represented as two vectors.'''
    return covariance(v1, v2) / (pstdev(v1) * pstdev(v2))
    
    
