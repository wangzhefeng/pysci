



import pandas as pd
import numpy as np


df = pd.DataFrame({
    "a": [1, 2, 0, 3, 5, 4, np.nan],
})


print(df)
b = [i for i in df["a"].values if i > 0]
print(b)