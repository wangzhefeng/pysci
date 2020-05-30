#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")



bob = ["Bob Smith", 42, 30000, "software"]
sue = ["Sue Jones", 45, 40000, "hardware"]
people = [bob, sue]
people.append(["Tom", 50, 0, None])
print(people)
