# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:49:30 2017

@author: Wangzf
"""

#==============================================================================
# statsmodels is a Python module that provides classes and functions
# for the estimation of many different statistical models,
# as well as for conducting statistical tests, 
# and statistical data exploration. 
# An extensive list of result statistics are available for each 
# estimator. The results are tested against existing statistical 
# packages to ensure that they are correct. 
# The package is released under the open source Modified BSD (3-clause) 
# license. The online documentation is hosted at statsmodels.org.
#==============================================================================

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load data
dat = sm.datasets.get_rdataset('Guerry', 'HistData').data
# print(dat)

# 
