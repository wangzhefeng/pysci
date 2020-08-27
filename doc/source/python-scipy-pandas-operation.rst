
Pandas 高级技巧
===================



1.用 `Pyjanitor` 更好地进行数据清洗与处理
------------------------------------------

.. code-block:: python

    # ----------------------
    # data 
    # ----------------------
    import numpy as np
    import pandas as pd
    
    df = pd.DataFrame({
        "a": [None, 2, None, None, 5, 6],
        "b": [1, None, None, 4, None, 6],
    })
    print(df)

    # ----------------------
    # 取两列中的非空数据的交集，pd.apply
    # ----------------------
    def get_valid_value(col_x, col_y):
        if not pd.isna(col_x) and pd.isna(col_y):
            return col_x
        elif pd.isna(col_x) and not pd.isna(col_y):
            return col_y
        elif not (pd.isna(col_x) or pd.isna(col_y)):
            return col_x
        else:
            return np.nan
    
    df["c"] = df.apply(lambda x: get_valid_value(x["a"], x["b"]), axis = 1)
    print(df)
    

.. code-block:: python

    import numpy as np
    import pandas as pd
    import janitor

    # ----------------------
    # data 
    # ----------------------
    df = pd.DataFrame({
        "a": [None, 2, None, None, 5, 6],
        "b": [1, None, None, 4, None, 6],
    })
    print(df)
    # ----------------------
    # Pyjanitor
    # ----------------------
    df = df.coalesce(column_names = ["a", "b"],
                new_column_name = "c",
                delete_columns = False)
    print(df)

