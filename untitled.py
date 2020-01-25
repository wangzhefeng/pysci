#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loguru import logger
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import torch





def main():
    x = torch.empty(5, 3)
    x = torch.rand(5, 3)
    x = torch.zeros(5, 3, dtype = torch.long)
    x = torch.tensor([5.5, 3])
    x = x.new_ones((5, 3), dtype = torch.double)
    x = torch.randn_like(x, dtype = torch.float)
    print(x)
    print(x.size())




if __name__ == "__main__":
    main()
