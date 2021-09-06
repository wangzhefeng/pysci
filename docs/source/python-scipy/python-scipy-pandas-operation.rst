
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





.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import numpy as np
    import pandas as pd
    from pandas import Series, DataFrame
    ########################################################################
    #                               Series
    ########################################################################
    # 1.Series(, index = ) .values .index
    obj1 = Series([4, 7, -5, 3])
    print(obj1)
    # .values
    print(obj1.values)
    # .index
    print(obj1.index)

    # 2.索引，数组运算，字典函数in
    obj2 = Series([4, 7, -5, 3], index = ['d', 'b', 'a', 'c'])
    print(obj2)
    # 索引
    print(obj2['a'])
    print(obj2[['a']])
    print(obj2[['c', 'a', 'd']])
    print(obj2[obj2 > 0])
    # 数组运算
    print(obj2 * 2)
    print(np.exp(obj2))
    # 字典函数 in
    print('b' in obj2)

    # 3.通过字典创建Series
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    obj3 = Series(sdata)
    print(obj3)

    # 4. pd.isnull() pd.notnull() .isnull() .notnull()
    states = ['California', 'Ohio', 'Oregon', 'Texas']
    obj4 = Series(sdata, index = states)
    print(obj4)
    # pd.isnull() .isnull()
    print(pd.isnull(obj4))
    print(obj4.isnull())
    # pd.notnull() .notnull()
    print(pd.notnull(obj4))
    print(obj4.notnull())
    # 算术运算
    print(obj3 + obj4)
    # .name .index.name
    obj4.name = 'population'
    print(obj4.name)
    obj4.index.name = 'state'
    print(obj4.index.name)
    print(obj4)
    ########################################################################
    #                               1.读入或生成数据表
    ########################################################################
    # 1.利用Python读取外部数据文件
    ## 1.1 读取文本文件的数据，如txt文件和csv文件
    #------------- Txt File ---------------------
    gapminderDataFiveYear1 = pd.read_table('https://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/gapminder/data/gapminderDataFiveYear.txt', 
                                        sep = '\t', 
                                        encoding = 'utf-8')
    print(gapminderDataFiveYear1.head())
    print(gapminderDataFiveYear1.tail())
    gapminderDataFiveYear2 = pd.read_table('/home/wangzhefeng/project/data/gapminderDataFiveYear.txt', 
                                        sep = '\t', 
                                        encoding = 'utf-8')
    print(gapminderDataFiveYear2.head()) 
    print(gapminderDataFiveYear2.tail())

    #-------------- CSV file ----------------------
    iris_csv = pd.read_csv('/home/wangzhefeng/project/data/iris.csv', 
                        sep = ',', 
                        encoding = 'utf-8')
    print(iris_csv.head())
    print(iris_csv.tail())
    mtcars_csv = pd.read_csv('/home/wangzhefeng/project/data/mtcars.csv',
                        sep = ',', 
                        encoding = 'utf-8')
    print(mtcars_csv.head())
    print(mtcars_csv.tail())

    ## 1.2 读取电子表格文件，如Excel-(xlsx)文件
    iris_xlsx = pd.read_excel('/home/wangzhefeng/project/data/iris.xlsx', 
                            sep = '', 
                            encoding = 'utf-8')
    print(iris_xlsx.head())
    print(iris_xlsx.tail())
    mtcars_xlsx = pd.read_excel('/home/wangzhefeng/project/data/mtcars.xlsx',
                                sep = '',
                                encoding = 'utf-8')
    print(mtcars_xlsx.head())
    print(mtcars_xlsx.tail())

    ## 1.3 读取统计软件生成的数据文件，如 SAS 数据集、SPSS 数据集等
    ## 1.4 读取数据库数据，如MySQL数据、SQL Server数据
    # ---------------- pymssql(SQL Server) -----------------
    import pymssql
    conn = pymssql.connect(host = 'localhost',
                        user = 'SA',
                        password = 'Alvin123',
                        database = 'tinker')
    cur = conn.cursor()
    cur.execute('''select 
                        no_plate 
                from USEGD_TrackNos 
                where status is null or status != '派送完成' 
                order by printdate''')
    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    #------------------ pymysql(MySQL) ----------------------
    import pymysql
    conn = pymysql.connect(host = '192.168.1.252:5678', 
                        user = 'tom.dong',
                        password = 'oig123456',
                        database = 'dmj')
    cur = conn.cursor()
    cur.execute('''select 
                        no_plate 
                from USEGD_TrackNos 
                where status is null or status != '派送完成' 
                order by printdate''')

    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    ## 1.5 JSON数据
    obj = """
    {"name": "Wes",
    "places_lived": ["United States", "Spain", "Germany"],
    "pet": null,
    "siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"}, 
                {"name": "Katie", "age": 33, "pet": "Cisco"}]
    }
    """
    import json
    result = json.loads(obj)
    print(result)
    asjson = json.dumps(result)
    print(asjson)
    # 外层键为列名，内层键为行名，可以进行转置
    siblings = DataFrame(result['siblings'], columns = ['name', 'age', 'pet'])
    print(siblings)

    # 2. 将数据写入文本(txt, csv), 写入Excel等
    df.to_excel()
    df.to_csv()




    ##############################################################
    # 2. 利用Python生成数据表
    df = DataFrame({'id':[1001, 1002, 1003, 1004, 1005, 1006], 
                    'date':pd.date_range('20130102', periods = 6), 
                    'city':['Beijing', 'SH', 'guangzhou', 'Shengzhen', 'Shanghai', 'BEIJING'],
                    'age':[23, 44, 54, 32, 34, 32],
                    'category':['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                    'price':[1200.0, np.nan, 2133, 5433, np.nan, 4432]}, 
                    columns = ['id', 'date', 'city', 'category', 'age', 'price'])
    print(df)

    #################################################################
    #                         2.数据输出
    #################################################################
    # df_inner.to_excel('excel_to_python.xlsx', sheet_name = 'bluewhale_cc')
    # df_inner.to_csv('excel_to_python.csv')


    #################################################################
    #                         3.检查数据表
    #################################################################
    # 2.1 数据维度
    print(df.shape)
    # 2.2 数据信息
    print(df.info())
    # 2.3 数据格式
    print(df.dtypes)
    print(df['date'].dtypes)
    # 2.4 缺失值查看
    print(df.isnull())
    print(pd.isnull(df))
    print(df['price'].isnull())
    print(pd.isnull(df['price']))
    print(df.notnull())
    # 2.5 唯一值查看
    print(df['city'].unique())
    obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
    # 2.6 值出现频率
    print(pd.value_counts(df['age']))
    print(pd.value_counts(df['age'], sort = False))
    # 2.7 成员资格
    mask = df['age'].isin([23, 32])
    print(mask)
    print(df['age'][mask])
    # 2.8 查看数据数值(数组的形式)
    print(df.values)
    # 2.9 查看数据列名
    print(df.columns)
    # 2.10 查看部分数据
    print(df.head())
    print(df.tail())
    #################################################################
    #                         3 数据清洗
    ################################################################# 
    # 3.1 缺失值处理
    print(df.dropna(how = 'any'))
    print(df.fillna(value = 0))
    print(df.fillna(df['price'].mean()))
    # 3.2 去除数据中的空格
    df['city'] = df['city'].map(str.strip)
    print(df)
    # 3.3 大小写转换
    df['city'] = df['city'].str.lower()
    print(df)
    df['city'] = df['city'].str.upper()
    print(df)
    # 3.4 更改数据格式
    # print(df['price'].astypes('int'))

    # 3.5 更改列名称
    df.rename(columns = {'category':'category-size'})
    print(df)
    # 3.6 删除重复值
    print(df['city'].drop_duplicates())
    print(df['city'].drop_duplicates(keep = 'last'))
    # 3.7 数值修改及替换
    print(df['city'].replace('SH', 'SHANGHAI'))

    #################################################################
    #                         4.数据预处理
    #################################################################
    ## 4.1 数据合并 (left/right/inner/outer_join)
    df = DataFrame({'id':[1001, 1002, 1003, 1004, 1005, 1006], 
                    'date':pd.date_range('20130102', periods = 6),
                    'city':['beijing', 'shanghai', 'guangzhou', 'shengzhen', 'shanghai', 'beijing'],
                    'age':[23, 44, 54, 32, 34, 32],
                    'category':['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                    'price':[1200.0, np.nan, 2133, 5433, np.nan, 4432]}, 
                    columns =['id', 'date', 'city', 'category', 'age', 'price'])
    print(df)
    df1 = DataFrame({'id':[1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
                    'gender':['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
                    'pay':['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y'],
                    'm-point':[10, 12, 20, 40, 40, 40, 30, 20]})
    print(df1)

    df_inner = pd.merge(df, df1, how = 'inner')
    print(df_inner)
    df_left = pd.merge(df, df1, how = 'left')
    print(df_left)
    df_right = pd.merge(df, df1, how = 'right')
    print(df_right)
    df_outer = pd.merge(df, df1, how = 'outer')
    print(df_outer)

    ## 4.2 设置索引列
    df_inner.set_index('id')
    df_inner.set_index(['id', 'gender'])
    df_inner.set_index(['id', 'gender'], drop = False)
    print(df_inner)

    print(df_inner.reset_index())


    ## 4.3 排序(按索引，按数值)
    # Series
    obj = Series(range(4), index = ['d', 'a', 'b', 'c'])
    print(obj)
    print(obj.sort_index())
    obj1 = Series([4, 7, -3, -2])
    print(obj1.order())
    obj2 = Series([4, np.nan, 7, np.nan, -3, 2])
    print(obj2.order())
    # DataFrame
    frame = DataFrame(np.arange(8).reshape((2, 4)), 
                    index = ['three', 'one'], 
                    columns = ['d', 'a', 'b', 'c'])
    print(frame.sort_index())
    print(frame.sort_index(axis = 1))
    print(frame.sort_index(ascending = False))

    frame = DataFrame({'b':[4, 7, -3, 2], 'a':[0, 1, 0, 1]})
    print(frame)
    print(frame.sort_index(by = 'b'))
    print(frame.sort_index(by = ['b', 'a']))

    # rank() 排名
    obj = Series([7, -5, 7, 4, 2, 0, 4])
    print(obj)
    print(obj.rank())
    print(obj.rank(method = 'first'))
    print(obj.rank(method = 'max'))
    print(obj.rank(method = 'min'))
    print(obj.rank(method = 'average'))
    print(obj.rank(ascending = False, method = 'max'))



    ## 4.4 数据分组
    df_inner['group'] = np.where(df_inner['price'] > 3000, 'high', 'low')
    print(df_inner)

    df_inner.loc[(df_inner['city'] == 'beijing') & (df_inner['price'] >= 4000), 'sign'] = 1
    print(df_inner)

    ## 4.5 数据分列
    split = pd.DataFrame((x.split('-') for x in df_inner['category']), 
                        index = df_inner.index, 
                        columns = ['category', 'size'])
    df_inner = pd.merge(df_inner, split, left_index = True, right_index = True)
    print(df_inner)

    #################################################################
    #                         5.数据提取
    #################################################################
    ## 5.1 按索引提取(loc)
    print(df_inner.loc[3])
    print(df_inner.loc[3:5])

    df_inner.reset_index()
    df_inner = df_inner.set_index('date')
    print(df_inner)
    print(df_inner.loc[:'2013-01-04'])
    ## 5.2 按位置提取(iloc)
    print(df_inner.iloc[:3, :2])
    print(df_inner.iloc[[0, 2, 5], [4, 5]])
    ## 5.3 按标签和位置提取(ix)
    print(df_inner.ix[:'2013-01-04', :4])
    ## 5.4 按条件提取(区域, 条件值)
    print(df_inner['city'].isin(['BEIJING']))
    print(df_inner.loc[df_inner['city'].isin(['beijing', 'shanghai'])])

    category = df_inner['category_x']
    print(category)
    print(pd.DataFrame(category.str[:3]))
    #################################################################
    #                         6.数据筛选
    #################################################################
    ## 6.1 按条件筛选（与，或，非）
    print(df_inner.loc[(df_inner['age'] > 25) & (df_inner['city'] == 'beijing'), 
        ['id','city','age','category','gender']])

    print(df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beijing'), 
        ['id','city','age','category','gender', 'price']].sort_values(by = ['age']).price.sum())

    print(df_inner.loc[df_inner['city'] != 'BEIJING', 
        ['id','city','age','category','gender', 'price']].sort_values(by = ['id']).city.count())

    print(df_inner.query("city == ['beijing', 'shanghai']").price.sum())
    #################################################################
    #                         7.数据汇总
    #################################################################
    ## 7.1 分类汇总
    print(df_inner)
    print(df_inner.groupby('city').count())
    print(df_inner.groupby('city')['id'].count())
    # or
    print(df_inner.groupby('city').count()['id'])
    print(df_inner.groupby(['city', 'size'])['id'].count())
    print(df_inner.groupby('city')['price'].agg([len, np.sum, np.mean]))
    ## 7.2 数据透视表
    print(pd.pivot_table(df_inner, 
                        index = ['city'], 
                        values = ['price'], 
                        columns = ['size'],
                        aggfunc = [len, np.sum],
                        fill_value = 0, 
                        margins = True))

    #################################################################
    #                         8.数据统计
    #################################################################
    ## 8.1 数据采样
    print(df_inner.sample(n = 2))
    weights = [0, 0, 0, 0, 0.5, 0.5]
    print(df_inner.sample(n = 2, weights = weights))
    print(df_inner.sample(n = 5, replace = True))
    print(df_inner.sample(n = 5, replace = False))
    ## 8.2 描述统计
    print(df_inner.describe().round(2).T)
    print(df_inner['price'].std())
    print(df_inner['price'].cov(df_inner['m-point']))
    print(df_inner.cov())

    print(df_inner['price'].corr(df_inner['m-point']))
    print(df_inner.corr())

    ######################################################
    # 						索引对象
    ######################################################



    #####################################################
    # 						重新索引
    #####################################################
    # .reindex(, fill_value = , method = '')

    ## 1.重新索引(索引重排)
    obj = Series([4.5, 7.2, -5.3, 3.6], index = ['d', 'b', 'a', 'c'])
    print(obj)
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
    print(obj2)

    ## 2.缺失值填充
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value = 0)
    print(obj2)

    ## 3.插值处理
    obj3 = Series(['blue', 'purple', 'yellow'], index = [0, 2, 4])
    ### 3.1前项值填充
    obj3.reindex(range(6), method = 'ffill')
    obj3.reindex(range(6), method = 'pad')
    ### 3.2后向填充
    obj3.reindex(range(6), method = 'bfill')
    obj3.reindex(range(6), method = 'backfill')
    ######################################################
    # 						删除行或列
    ######################################################
    ## 删除行
    obj = Series(np.arange(5.0), index = ['a', 'b', 'c', 'd', 'e'])
    print(obj)
    new_obj = obj.drop('c')
    new_obj = obj.drop(['d', 'c'])
    #
    data = DataFrame(np.arange(16).reshape((4, 4)), 
                    index = ['Ohio', 'Colorado', 'Utha', 'New York'], 
                    columns = ['one', 'two', 'three', 'four'])
    print(data)

    print(data.drop('Colorado'))
    print(data.drop('Colorado', axis = 0))

    print(data.drop(['Colorado', 'Ohio']))
    print(data.drop(['Colorado', 'Ohio'], axis = 0))
    ## 增加 & 删除列 
    ### del & .drop(, axis = 1)

    data['five'] = np.arange(4)
    print(data)

    del data[['five', 'six']]
    print(data)

    print(data.drop('two', axis = 1))
    print(data.drop(['two', 'four'], axis = 1))
    ######################################################
    #					索引、切片、过滤
    #######################################################
    # Series
    obj = Series(np.arange(4.0), index = ['a', 'b', 'c', 'd'])
    print(obj)
    ## 索引
    obj['a']
    obj[0]
    obj[['b', 'a', 'd']]
    obj[[1, 0, 3]]

    ## 条件索引
    obj[obj < 2]

    ## 切片
    obj[1:2]
    obj['b':'c'] # 与obj[1:2]不同，包含 obj['c']

    # DataFrame


    ###############################################
    # 			算术运算和数据对齐
    ###############################################
    s1 = Series([7.3, -2.5, 3.4, 1.5], index = ['a', 'c', 'd', 'e'])
    s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index = ['a', 'c', 'e', 'f', 'g'])
    print(s1)
    print(s2)
    print(s1 + s2)

    df1 = DataFrame(np.arange(9.0).reshape((3, 3)), 
                    index = ['Ohio', 'Texas', 'Colorado'],
                    columns = list('bcd'))
    df2 = DataFrame(np.arange(12.0).reshape((4, 3)), 
                    index = ['Utah', 'Ohio', 'Texas', 'Oregon'], 
                    columns = list('bde'))
    print(df1)
    print(df2)
    print(df1 + df2)

    df1 = DataFrame(np.arange(12.0).reshape((3, 4)), columns = list('abcd'))
    df2 = DataFrame(np.arange(20.0).reshape((4, 5)), columns = list('abcde'))
    print(df1 + df2)
    print(df1.add(df2, fill_value = 0))
    print(df1.sub(df2, fil_value = 0))
    print(df1.mul(df2, fill_value = 0))
    print(df1.div(df2, fill_value = 0))

    # 广播
    arr = np.arange(12.0).reshape((3, 4))
    print(arr)
    print(arr[0])
    print(arr - arr[0])

    frame = DataFrame(np.arange(12.0).reshape((4, 3)), 
                    index = ['Utah', 'Ohio', 'Texas', 'Oregon'], 
                    columns = list('bde'))
    print(frame)
    series = frame.ix[0]
    print(series)

    # 行
    print(frame - series)

    # 行(并集)
    series2 = Series(range(3), index = ['b', 'e', 'f'])
    print(frame + series2)

    # 列
    series3 = frame['d']
    print(frame.sub(series3, axis = 0))



    ###############################################
    # 			汇总和计算描述统计
    ###############################################
    df = DataFrame([[1.4, np.nan], 
                [7.1, -4.5], 
                [np.nan, np.nan], 
                [0.75, -1.3]], 
                index = ['a', 'b', 'c', 'd'], 
                columns = ['one', 'two'])
    print(df)
    # .count()
    df.count()
    df.count(axis = 1)
    # .max() .min() # .idmax() .idmin() # .argmax() .argmin() .cummax() .cummin()
    df.max()
    df.max(axis = 1)
    df.min()
    df.min(axis = 1)
    df.idxmax()
    df.idxmax(axis = 1)
    df.idxmin()
    df.idxmin(axis = 1)
    df.cummax()
    df.cummin()
    # .sum # .cumsum()
    df.sum()
    df.sum(axis = 1)
    df.sum(axis = 1, skipna = False)
    df.sum(axis = 1, skipna = False, level = 1)
    df.cumsum()
    df.cumsum(axis = 1)
    # .describe()
    df.describe()
    # .quantile(0-1)
    df.quantile()
    # .mean()
    df.mean()
    # .median()
    df.median()
    # .mad() 根据平均值计算平均绝对离差
    df.mad()
    # .var()
    df.var()
    # .std()
    df.std()
    # .skew()
    df.skew()
    # .kurt()
    df.kurt()
    # .cumprod()
    df.cumprod()
    # .diff() 计算一阶差分
    df.diff()
    # .pct_change()  计算百分数变化
    df.pct_change()
    # 相关系数与协方差
    s1.corr(s2)
    s1.cov(s2)
    df.corr()
    df.cov()
    df1.corrWith(df2)
    df1.corrWith(df2, axis = 1)
    #################################################
    # 				函数应用和映射
    #################################################
    frame = DataFrame(np.random.randn(4, 3), 
                    index = ['Utah', 'Ohio', 'Texas', 'Oregon'], 
                    columns = list('bde'))
    print(frame)
    # Numpy的ufuncs(元素级数组方法)
    print(np.abs(frame))
    # apply()
    f = lambda x: x.max() - x.min()
    print(frame.apply(f))
    print(frame.apply(f, axis = 0))
    print(frame.apply(f, axis = 1))
    # applymap()(元素级的Pythn函数方法)
    formater = lambda x: '%.2f' %x
    print(frame.applymap(formater))
    # Series的map()
    print(frame['e'].map(formater))

    #################################################
    # 			带有重复值的轴索引
    ################################################
    obj = Series(range(5), index = ['a', 'a', 'b', 'b', 'c'])
    print(obj)
    print(obj.index.is_unique)


    ####################################################
    # 					层次化索引
    ####################################################
    data = Series(np.random.randn(10), 
                index = [['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], 
                            [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
    print(data)
    print(data.index)
    print(data['b'])
    print(data['b':'c'])
    print(data[:, 2])
    print(data.unstack())
    print(data.unstack().stack())

    frame = DataFrame(np.arange(12).reshape(4, 3), 
                    index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]], 
                    columns = [['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
    print(frame)
    frame.index.names = ['key1', 'key2']
    frame.columns.names = ['state', 'color']
    print(frame)

    print(frame.swaplevel('key1', 'key2'))
    print(frame.sortlevel(1))

    print(frame.sum(level = 'key2'))


    ######################################################################################################
    #                           groupby -- split-apply-combine
    ######################################################################################################
    import pandas as pd
    import numpy as np


    # ======================================
    # groupby 技术
    # ======================================
    # example 1 (分组键为series)
    df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                    'key2': ['one', 'two', 'one', 'two', 'one'],
                    'data1': np.random.randn(5),
                    'data2': np.random.randn(5)})

    grouped_mean1 = df['data1'].groupby(df['key1']).mean()
    grouped_mean11 = df.groupby('key1')['data1'].mean()
    grouped_mean111 = df.groupby('key1')[['data1']].mean()
    grouped_mean1111 = df.groupby('key1').mean()

    grouped_mean2 = df['data1'].groupby([df['key1'], df['key2']]).mean()
    grouped_mean22 = df.groupby(['key1', 'key2'])['data1'].mean()
    grouped_mean222 = df.groupby(['key1', 'key2'])[['data1']].mean()
    grouped_mean2222 = df.groupby(['key1', 'key2']).mean()
    print(grouped_mean2.unstack())
    type(grouped_mean2.unstack())


    # example 2 (分组键为任何适当长度的array)
    states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
    years = np.array([2005, 2005, 2006, 2005, 2006])
    df['data1'].groupby([states, years]).mean()

    # example 3 (.size()方法)
    df.groupby(['key1', 'key2']).size()

    # example 4 (GroupBy对象支持迭代, 可以产生一组二元array, 由name(分组名)和group(数据块)组成)
    for name, group in df.groupby('key1'):
        print(name)
        print(group)
    for (k1, k2), group in df.groupby(['key1', 'key2']):
        print(k1, k2)
        print(group)

    pieces = dict(list(df.groupby('key1'))) # 将数据片段做成字典
    print(pieces)
    print(pieces['a'])
    print(pieces['b'])

    # example 5 在列上分组
    print(df.dtypes)
    grouped = df.groupby(df.dtypes, axis = 1)
    dict(list(grouped))

    # example 6 (通过字典或series进行分组)(列分组)
    people = pd.DataFrame(np.random.randn(5, 5),
                        columns = ['a', 'b', 'c', 'd', 'e'],
                        index = ['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
    people.ix[2:3, ['b', 'c']] = np.nan
    mapping = {'a': 'red',
            'b': 'red',
            'c': 'blue',
            'd': 'blue',
            'e': 'red',
            'f': 'orange'}
    by_column1 = people.groupby(mapping, axis = 1).sum()

    map_series = pd.Series(mapping)
    by_column2 = people.groupby(map_series, axis = 1).count()

    # example 7 (通过函数进行分组)(函数作用在行索引值上, 返回值作为分组建)
    people.groupby(len).sum()

    key_list = ['one', 'one', 'one', 'two', 'two']
    people.groupby([len, key_list]).min()

    # example 8 (根据索引级别进行分组)
    columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                        [1, 3, 5, 1, 3]],
                                    names = ['cty', 'tenor'])
    hier_df = pd.DataFrame(np.random.randn(4, 5), columns = columns)
    hier_df.groupby(level = 'cty', axis = 1).count()

    # ======================================
    # 数据聚合
    # ======================================
    # 聚合函数
    # agg(func)
    # aggregate(func)
    # count()
    # sum()
    # mean()
    # median()
    # std()
    # var()
    # min()
    # max()
    # prod()
    # first()
    # last()


    # example 1
    grouped = df.groupby('key1')['data1']
    grouped.quantile(0.9)

    # example 2 (self function)
    grouped = df.groupby('key1')['data1']
    def peak_to_peak(arr):
        return arr.max() - arr.min()
    grouped.agg(peak_to_peak)
    grouped.aggregate(peak_to_peak)

    # example 3 (not aggregate function)
    grouped.describe()

    # example 4
    tips = pd.read_csv('/home/wangzhefeng/project/data/tips.csv')
    tips['tip_pct'] = tips['tip'] / tips['total_bill']

    grouped_pct = tips.groupby(['sex', 'smoker'])['tip_pct']
    grouped_pct.agg('mean')
    grouped_pct.agg(['mean', 'std', peak_to_peak])
    grouped_pct.agg([('foo', 'mean'), ('bar', np.std)]) # 改变列名


    # example 5 (对不同列应用相同函数)
    functions = ['count', 'mean', 'max']
    grouped = tips.group(['sex', 'smoker'])
    result = grouped['tip_pct', 'total_bill'].agg(functions)
    print(result['tip_pct'])
    print(result['total_bill'])

    # example 6 (传入带自定义名称的元组列表)
    ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
    grouped['tip_pct', 'total_bill'].agg(ftuples)


    # example 7 (对不同列应用不同函数)
    grouped.agg({'tip': np.max, 'size': 'sum'})
    grouped.agg({'tip_pct': ['min', 'max', 'mean', 'std'],
                'size': 'sum'})

    # example 8 (无索引的形式返回聚合函数)
    tips.groupby(['sex', 'smoker']).mean()                  # 有索引
    tips.groupby(['sex', 'smoker']).mean().reset_index()    # 无索引
    tips.groupby(['sex', 'smoker'], as_index = False).mean()# 无索引

    # ==================================
    # transfrom apply
    # ==================================
    k1_means = df.groupby('key1').mean().add_prefix('mean_')
    pd.merge(df, k1_means, left_on = 'key1', right_index = True)

    key = ['one', 'two', 'one', 'two', 'one']
    people.groupby(key).mean()
    people.groupby(key).transform(np.mean)

    def demean(arr):
        return arr - arr.mean()

    demeaned = people.groupby(key).transform(demean)

    # apply
    def top(df, n = 5, column = 'tip_pct'):
        return df.sort_index(by = column)[-n:]
    top(tips, n = 6)

    tips.groupby('smoker').apply(top)
    tips.groupby(['smoker', 'day']).apply(top, n = 1, column = 'total_bill')

    result = tips.groupby('smoker')['tip_pct'].describe()
    result.unstack('smoker')

    f = lambda x: x.describe()
    grouped.apply(f)

    tips.groupby('smoker', group_keys = False).apply(top)

    # 分位数和桶分析
    frame = pd.DataFrame({'data1': np.random.randn(1000),
                        'data2': np.random.randn(1000)})
    factor = pd.cut(frame.data1, 4)

    def get_stats(group):
        return {'min': group.min(),
                'max': group.max(),
                'count': group.count(),
                'mean': group.mean()}
    grouped = frame.data2.groupby(factor)
    grouped.apply(get_stats).unstact()
    grouped.apply(get_stats).unstact()

    grouping = pd.qcut(frame.data1, 10, labels = False)
    grouped = frame.data2.groupby(grouping)
    grouped.apply(get_stats).unstack()


    # ===========================
    # 透视表和交叉表
    # ===========================






    ######################################################################################################
    #                          Time Series
    ######################################################################################################
    # 三种时间序列数据：
    # timestamp
    # period
    # interval

    from datetime import datetime, date, time, timedelta
    # import time
    # import calendar

    # datetime中的四种数据类型：
    # date: 以公历形式存储日期year, month, day
    # time: 将时间存储为hour, minute, second, microsecond
    # datetime: 存储日期和时间(year, month, day, hour, minute, second, microsecond)
    # timedelta: 表示两个datetime值之间的差(days, seconds, microsecond)


    # datetime.now()
    now = datetime.now()
    print(now)
    print(now.year)
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(now.microsecond)

    # date
    today_date = date(2017, 12, 19)
    print(today_date)

    # time()
    today_time = time(10, 41, 14, 20)
    print(today_time)

    # datetime()
    today_datetime = datetime(2011, 1, 7)
    print(today_datetime)

    # timedelta(obj) timedelta(days)
    # timedelta(days, seconds, microsecind, milliseconds, minutes, hours, weeks)
    delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
    print(delta)
    print(delta.days)
    print(delta.seconds)

    print(today_datetime + timedelta(days = 12))
    print(today_datetime - 2 * timedelta(days = 12))

    #--------------------------------------------------------------------
    # 字符串和datetime的相互转换: dt.strftime('%') datetime.strptime(str, '%')
    stamp = datetime(2011, 1, 3)
    str(stamp)
    stamp.strftime('%Y-%m-%d')
    stamp.strftime('%F')
    # %Y：四位数的year
    # %y: 两位数的year
    # %m: 两位数的month
    # %d: 两位数的day
    # %H: hour(24)
    # %I: hour(12)
    # %M: 两位数的minute
    # %S: second
    # %w: 用整数表示的星期几
    # %U: 每年的第几周(00~53),星期天被认为是每周的第一天,每年的第一个星期天之前的那几天被认为是“第0周”
    # %W: 每年的第几周(00~53),星期一被认为是每周的第一天,每年的第一个星期一之前的那几天被认为是“第0周”
    # %z: 以+HHMM或-HHMM表示的UTC时区偏移量,如果时区位naive,则返回空字符串
    # %F: %Y-%m-%d简写形式
    # %D: %m/%d/%y简写形式
    #------------------------
    # %a: 星期几的简称
    # %A: 星期几的全称
    # %b: 月份的简称
    # %B: 月份的简称
    # %c: 月份的全称
    # %p: 完整的日期和时间(Tue 01 May 2012 04:20:57 PM)
    # %x: 适合于当前环境的日期
    # %X: 适合于当前环境的时间

    value = '2011-01-03'
    datetime.strptime(value, 'F')
    datestrs = ['7/6/2011', '8/6/2011']
    print([datetime.strptime(x, '%D') for x in datestrs])

    #------------------------------------------------
    # dateutil可以解析几乎所有人类能够理解的日期表示形式
    from dateutil.parser import parse
    print(parse('2011-01-03'))
    print(parse('Jan 31, 1997 10:45 PM'))
    print(parse('6/12/2011', dayfirst = True))

    #----------------------------------------
    # pandas.to_datetime()
    datestrs = ['7/6/2011', '8/6/2011']
    print(pd.to_datetime(datestrs))

    idx = pd.to_datetime(datestrs + [None])
    print(idx)
    print(pd.isnull(idx))


    ###########################################################################################################
    #                           时间序列基础
    ###########################################################################################################
    # pandas 最基本的时间序列类型就是以时间戳(通常以python字符串或datetime对象表示)为索引的Series
    import pandas as pd
    import numpy as np
    from datetime import datetime

    dates = [datetime(2011, 1, 2),
            datetime(2011, 1, 5),
            datetime(2011, 1, 7),
            datetime(2011, 1, 8),
            datetime(2011, 1, 10),
            datetime(2011, 1, 12)]
    ts = pd.Series(np.random.randn(6), index = dates)
    print(ts)             # 时间序列数据
    print(ts.index)       # DatetimeIndex
    print(type(ts))       # pandas.core.series.Series
    print(ts.index.dtype) # datetime64[ns]
    print(ts + ts[::2])   # 算术运算自动按日期对齐
    stamp = ts.index[0]   # 标量值是pandas的Timestamp对象
    print(stamp)          # pandas.Timestamp
    #------------------------------------------------
    # 索引、选取、子集构造
    stamp = ts.index[2]
    print(ts[stamp])
    print(ts['1/10/2011'])
    print(ts['20110110'])

    # 较长的时间序列
    longer_ts = pd.Series(np.random.randn(1000),
                        index = pd.date_range('1/1/2000', periods = 1000))
    print(longer_ts)
    print(longer_ts['2001'])    # 取出所有2001年的数据
    print(longer_ts['2001-05']) # 取出所有2001年5月的数据
    print(longer_ts[datetime(2001, 1, 7):])

    # 范围查询
    print(ts['1/6/2011':'1/11/2011']) # '1/6/2011' and '1/11/2011' not in ts.index
    print(ts.truncate(before = '1/7/2011', after = '1/9/2011'))

    dates = pd.date_range('1/1/2000', periods = 100, freq = 'W-WED')
    long_df = pd.DateFrame(np.random.randn(100, 4),
                        index = dates,
                        columns = ['Colorado', 'Texas', 'New York', 'Ohio'])
    print(long_df.ix['5-2001'])
