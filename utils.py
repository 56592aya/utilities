# utils.py

import config
import pandas as pd
import numpy as np

def logger(func):
    """this is a decorator for logging a specific function and running it
    use with @logger before a function definitions if needs to be logged
    Args:
        func : a first class function

    Returns:
        : wrapped function return value
    """
    import logging
    logging.basicConfig(filename=f"{func.__name__}.log", level = logging.INFO)
    def wrapper(*args, **kwargs):
        """adds the functionality of logging for then func
        Returns:
            executed func
        """
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')  
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    """a decorator to time the execution of func
    use with @timer before a function definitions if needs to be timed

    Args:
        func : a first class function

    Returns:
         wrapped function return value
    """
    import time
    def wrapper(*args, **kwargs):
        """adds the functionality of timing the exectable func

        Returns:
            executed func
        """
        t0 = time.time()
        ret = func(*args, **kwargs)
        t1 = time.time() - t0
        print(f'{func.__name__} elapsed {t1} sec')
        return ret
    return wrapper

#instead there are np.ndarray.flatten or np.ravel

# def deep_flatten(xs):
#     """flattens everyhitng there is a list of lists in anay form

#     Args:
#         xs : all the elements

#     Returns:
#         : flattened data
#     """
#     flat_list = []
#     [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
#     return flat_list
# implements this also for np
def chunk(list, size):
    """chunks a list to portions of size

    Args:
        list : list of elemetns
        size : chunk size

    Returns:
        : list of chunks
    """
    return [list[i:i+size] for i in range(0,len(list), size)]

def difference(a, b):
    """difference between two collection, no need to convert to set

    Args:
        a : [first collection]
        b : [second collection]

    Returns:
        the list of the remaining elements 
    """
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)

def merge_dictionaries(a, b):
    """given two dictionaries a and b merge them together

    Args:
        a : first dictionary
        b : second dictionary

    Returns:
        the merged dictionary
    """
    return {**a, **b}


def to_dictionary(keys, values):
    """given a key and values convert them to dictionary

    Args:
        keys : list of keys
        values : list of values associated with the keys

    Returns:
        dictionary of keys:values
    """
    return dict(zip(keys, values))


# subset params
def params_selector(*args, **full_params):
    """Given a dict of fullparams, we want to select a subset of them\
        to be sent to different functions.\
    
    args and full_params are of the following form
    
    `args = ['p2_1', 'p2_2', ...,]`
    `full_params = {'p1_1':val1_1, 'p1_2':val1_2, 'p2_1':val2_1, 'p2_2':val2_2, ...}`
    Also refer to select_params(selectpr, full_params)
    e.g full_params is a merged of (**process_params, **model_params)\
        at the input we choose for the both in advance and we want to \
        separate the **kwargs to be applied separately to functions.   
    """
    param_dict = {}
    for arg in args:
        param_dict[arg] = full_params[arg]
    return param_dict


# some pandas related functions
def drop_MultiIndex_col(self, inplace=False):
    """This is a pandas.DataFrame method added to drop the MultiIndex column names in a meaninful way by combining names
    Args:
        inplace (Bool, optional): to determine whether the method is inplace or not. Defaults to False.

    Returns:
        depending on the inplace parameter it is either None, or a modified dataframe with dropped column levels
    """
    if inplace:
        self.columns = ['_'.join(tup) for tup in self.columns]
        #returns None
    else:
        data = self.copy()
        data.columns = ['_'.join(tup) for tup in data.columns]
        return data
pd.DataFrame.drop_MultiIndex_col = drop_MultiIndex_col 

# def summarize_df(df, groupby_col=[None], cols_selector=[None], funcs_selector=['None']):
#     """This function will accept a dataframe and summarizes its information, given 

#     Args:
#         df ([type]): [description]
#         groupby_col ([type], optional): [description]. Defaults to [None].
#         cols_selector ([type], optional): [description]. Defaults to [None].
#         funcs_selector ([type], optional): [description]. Defaults to [None].

#     Returns:
#         [type]: [description]
#     """
#     summary_df = pd.DataFrame()
#     return summary_df

# plotting recipes within matplotlib and sns and pandas

# pipeline feature transformers, with fit and without

# data loader class template

# model class


