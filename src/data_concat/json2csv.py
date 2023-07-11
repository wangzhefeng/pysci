# -*- coding: utf-8 -*-


# ***************************************************
# * File        : json2csv.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-09-22
# * Version     : 0.1.092217
# * Description : 解析平台 api 获取的 json 数据 .py
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# ***************************************************


import pandas as pd
import json
import glob
import time


def convert2csv(path, type = "merge"):
    if path == '':
        json_files = glob.glob('*.json')
    else:
        json_files = glob.glob(path + '/' + '*.json')
    print("json_files:", json_files)

    if type == 'merge':
        all_df = pd.DataFrame()
        all_df['time'] = ''
        for json_file in json_files:
            with open(json_file,'r') as load_f:
                result_dict = json.load(load_f)
            key = result_dict['name']
            data = result_dict['data']

            times = []
            values = []

            for d in data:
                times.append(d['name'])
                values.append(d['value']['sum']/d['value']['cnt'])

            df = pd.DataFrame({"time":times,key:values})
            df['time'] = df['time'].apply(lambda x:x.split('.')[0][1:])
            df['time'] = df['time'].apply(lambda x:time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(x))))
            df['time'] = pd.to_datetime(df['time'])

            all_df = pd.merge(all_df,df,on='time', how='outer')
        all_df.to_csv('{}/result-{}.csv'.format(path, time.strftime('%m%d_%H%M%S',time.localtime(time.time()))), index=False)

    elif type == 'concat':
        all_df = pd.DataFrame()
        for json_file in json_files:
            with open(json_file,'r') as load_f:
                result_dict = json.load(load_f)
            key = result_dict['name']
            data = result_dict['data']

            times = []
            values = []

            for d in data:
                times.append(d['name'])
                values.append(d['value']['sum']/d['value']['cnt'])

            df = pd.DataFrame({"time":times,key:values})
            df['time'] = df['time'].apply(lambda x:x.split('.')[0][1:])
            df['time'] = df['time'].apply(lambda x:time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(x))))
            df['time'] = pd.to_datetime(df['time'])

            all_df = pd.concat([all_df,df],axis=0)
            print(all_df)
        all_df.to_csv('{}/result-{}.csv'.format(path, time.strftime('%m%d_%H%M%S',time.localtime(time.time()))),index=False)



if __name__ == '__main__':
    #path:json文件目录，如果多个json文件的metric要生成到同一个csv文件里变成多列，可将其放到同一目录下，然后函数type='merge'
    #如果多个json文件是同一metric的，将其放在同一目录下，然后函数type='concat'，生成只有一个metric的csv文件
    path = "/mnt/e/dev/data-download/result/yida_data"
    convert2csv(path, type='merge')

