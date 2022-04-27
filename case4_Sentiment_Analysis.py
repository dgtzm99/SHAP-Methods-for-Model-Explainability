#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:18:04 2022

@author: dgtzm99
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression # model used in case 1
from sklearn.model_selection import train_test_split # splitting data for validation
from sklearn.metrics import mean_squared_error, mean_absolute_error # model evaluation

import shap # feature importance

import transformers
#from datasets import load_dataset

'''
Sentiment analysis: process of identifying and categorizing opinions from pieces of text. Find attitued towards a particular topic is positive, negative or neutral
'''

#%%
test = load_dataset("poem_sentiment")


#%%