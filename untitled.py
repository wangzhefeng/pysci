#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loguru import logger
import pandas as pd 
from pandas import Grouper
import matplotlib.pyplot as plt 
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from tslearn.utils import to_time_series, to_time_series_dataset
from tsfresh.examples.robot_execution_failures import \
    download_robot_execution_failures, \
    load_robot_execution_failures
from tsfresh import extract_features
from tsfresh.utilities.dataframe_functions import impute
from tsfresh import select_features
from tsfresh import extract_relevant_features
import warnings
warnings.filterwarnings("ignore")





def main():
    pass

if __name__ == "__main__":
    main()
