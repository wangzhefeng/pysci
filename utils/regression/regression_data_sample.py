







def data_sample(df, x, y, group_number, quantile):
    """
    分组选点法
    x: 分组变量
    y: 取值变量
    """
    group_width = (np.max(df[x]) - np.min(df[x])) / group_number   # 分组宽度
    x_group = np.arange(np.min(df[x]), np.max(df[x]), group_width) # 分组的X
    # 选取每组中设定的分位数的点, 对点数大于零的组选点
    if len(quantile) == 3:
        data_x = np.array([])
        data_y = np.array([])
        for i in x_group:
            if len(df[(df[x] >= i) & (df[x] < i + group_width)]) > 0:
                temp_y = np.array(df[(df[x] >= i) & (df[x] < i + group_width)][y].quantile(quantile))
                temp_x = np.array([(i + group_width / 4), (i + group_width / 2), (i + 3 * group_width / 4)])
                data_x = np.concatenate([data_x, temp_x], axis = 0)
                data_y = np.concatenate([data_y, temp_y], axis = 0)
    elif len(quantile) == 1:
        data_x = []
        data_y = []
        for i in x_group:
            if len(df[(df[x] >= i) & (df[x] < i + group_width)]) > 0:
                temp_y = float(df[(df[x] >= i) & (df[x] < i + group_width)][y].quantile(quantile))
                temp_x = float(i + group_width / 2)
                data_x.append(temp_x)
                data_y.append(temp_y)
    
    return data_x, data_y