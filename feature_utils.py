'''
In this file, you file various recipes for data transformations.
The goal is to include :
- variable type selectors
- Creating new features
'''

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureSelector(BaseEstimator, TransformerMixin):
    """For selecting dtype-based features"""
    def __init__(self, dtype='categorical'):
        self.dtype = dtype
    
    def fit(self, X, y=None):
        # Nothing here
        return self
    def transform(self, X, y=None):
        if self.dtype  == 'category':
            cat_cols = X.columns[X.dtypes == object].tolist()
            return X[cat_cols]
        elif self.dtype == 'numeric':
            num_cols = X.columns[X.dtypes != object].tolist()
            return X[num_cols]
        else: # if some other type is reached for 
            select_cols = X.columns[X.dtypes == self.dtype].tolist()
            return X[select_cols]


class ColumnFeature(TransformerMixin,BaseEstimator):
    """
    Use this to create new features based on the current data
    Or use this format to create whatever new features are needed
    """
    def __init__(self, func):
        # func has to work on the dataframe
        self.func= func

    def fit(self, X, y=None,**kwargs):
        # Nothing to fit
        return self

    def transform(self, X, y=None, **kwargs):

        return self.func(X, **kwargs)
 




        