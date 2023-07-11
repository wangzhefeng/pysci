# -*- coding: utf-8 -*-


# ***************************************************
# * File        : data_download.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2022-01-21
# * Version     : 0.1.012114
# * Description : description
# * Link        : link
# * Requirement : (1)tqdm
# *                 $ pip install tqdm
# *               (2)requests[socks]
# *                 Win:   C:\> pip install requests[socks]
# *                 Linux: $ pip install 'requests[socks]'
# ***************************************************


# python libraries
import os
import time
import traceback
import requests
from tqdm import tqdm
import numpy as np
import pandas as pd
pd.set_option("max_columns", None)

import pprint
pp = pprint.PrettyPrinter(indent = 4)


def generate_config(config_path,
                   url_domain,
                   project_scopes,
                   cookie,
                   from_timestamp,
                   to_timestamp,
                   class_to_be_download):
    """
    生成配置信息
    """
    config_df = pd.read_csv(config_path + "config.csv")
    parameters = {}
    for i in range(len(config_df)):
        if config_df["class"].iloc[i] not in class_to_be_download:
            continue
        temp_dict = {
            config_df["geo"].iloc[i].split("|")[-1] + "_" + config_df["resolution"].iloc[i]:{
                "url_domain": url_domain,
                "project_scope": project_scopes,
                "cookie": cookie,
                "geo": config_df["geo"].iloc[i],
                "from_timestamp": from_timestamp,
                "to_timestamp": to_timestamp,
                "resolution": config_df["resolution"].iloc[i],
                "metrics": pd.read_csv(config_path + config_df["metric_file"].iloc[i])["metric_list"].to_list(),
            }
        }
        parameters.update(temp_dict)
    pp.pprint(f"generate_config: parameters={parameters}")
    return parameters


def query_data(url_domain, 
               project_scope, 
               cookie, 
               local_proxy_port,
               geo, 
               metric, 
               from_timestamp, 
               to_timestamp,
               resolution):
    """
    请求时序数据, 一次只能查一个 geo 的 一个 metric
    """
    # 请求数据参数
    requests.packages.urllib3.disable_warnings()
    url = "https://%s/%s/api/view/metric" % (url_domain, project_scope)
    params = {
        "name": metric,
        "metricType": "timeseries",
        "geo": geo,
        "from": from_timestamp,
        "to": to_timestamp,
        "period": resolution,
        "noPrune": True,
    }
    headers = {
        'Cookie': cookie
    }
    proxies = {
        "http": f"socks5h://127.0.0.1:{local_proxy_port}",
        "https": f"socks5h://127.0.0.1:{local_proxy_port}",
    }
    try:
        # 数据请求
        if local_proxy_port is not None:
            response = requests.get(
                url = url,
                params = params,
                headers = headers,
                verify = False,
                timeout = 100,
                proxies = proxies,
            )
            print(response.url)
        else:
            response = requests.get(
                url = url,
                params = params,
                headers = headers,
                verify = False,
                timeout = 20,
            )
            print(response.url)
        # 数据解析
        if response.status_code == 200:
            result = response.json()
            result = {
                "data": result["data"],
                "name": result["name"],
            }
    except:
        traceback.print_exc()

    return result


def unix2time(value):
    """
    将UNIX时间戳转换为日期时间格式
    """
    format = "%Y-%m-%d %H:%M:%S"
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt


def parse_data(result):
    """
    解析请求到的时序数据, 一次只解析一个 instance 的一个 metric
    """    
    metric_name = result["name"].split(".")[-1]
    df = pd.DataFrame({})
    for col in result["data"]:
        
        col["ts"] = [unix2time(float(col["name"]))]
        col[metric_name] = [col["value"]["sum"] / col["value"]["cnt"]]
        
        temp_df = pd.DataFrame(
            data = {
                "ts": col["ts"],
                metric_name: col[metric_name],
            },
            index = col["ts"], 
            columns = np.array(["ts", metric_name])
        )
        df = pd.concat([df, temp_df], axis = 0)

    return df


def integrate_data(data_path, parameters, local_proxy_port):
    for instance, value in parameters.items():
        df = pd.DataFrame({
            "ts": pd.date_range(unix2time(value["from_timestamp"] / 1000), unix2time(value["to_timestamp"] / 1000), freq = instance.split("_")[-1])
        })
        for metric in tqdm(value["metrics"]):
            # 数据请求
            data = query_data(
                url_domain = value["url_domain"],
                project_scope = value["project_scope"],
                cookie = value["cookie"],
                local_proxy_port = local_proxy_port,
                geo = value["geo"],
                metric = metric,
                from_timestamp = value["from_timestamp"],
                to_timestamp = value["to_timestamp"],
                resolution = value["resolution"],
            )
            # 数据解析
            temp_df = parse_data(data)
            temp_df["ts"] = pd.to_datetime(temp_df["ts"])
            # 数据合并
            df = df.merge(temp_df, how = "left", on = "ts")
        # 数据保存
        df.to_csv(f'{data_path}{instance}-{int(time.time())}.csv', index = False)


def data_download(project_config_dir, 
                  project_data_dir, 
                  url_domain, 
                  scope_project, 
                  cookie, 
                  from_timestamp, 
                  to_timestamp,
                  class_download,
                  local_proxy_port):
    # 配置文件地址
    config_root_path = "config/"
    if not os.path.exists(config_root_path):
        os.mkdir(config_root_path)

    # 下载数据文件地址
    data_root_path = "result/"
    if not os.path.exists(data_root_path):
        os.mkdir(data_root_path)
    
    # 参数及数据下载路径配置
    config_path = os.path.join(config_root_path, f"{project_config_dir}/")
    data_path = os.path.join(data_root_path, f"{project_data_dir}/")
    
    # 生成下载数据配置参数
    parameters = generate_config(
        config_path,
        url_domain,
        scope_project,
        cookie,
        from_timestamp,
        to_timestamp,
        class_download
    )
    # 下载数据
    integrate_data(
        data_path, 
        parameters, 
        local_proxy_port,
    )


# 测试代码 main 函数
def downloading(project_config, class_download, use_proxy = False):
    """
    数据下载

    Args:
        project_config (_type_): _description_
        is_gt_1day (bool, optional): _description_. Defaults to True.
    """
    # 下载数据天数
    download_days = (project_config["end_date"] - project_config["start_date"]) / 1000 / 3600 / 24
    download_days = 1 if download_days == 0 else int(download_days)
    for i in range(download_days):
        # 开始、结束时间戳
        start_date = project_config["start_date"] + i * 24 * 3600 * 1000
        end_date = project_config["start_date"] + (i + 1) * 24 * 3600 * 1000
        # 开始数据下载
        data_download(
            project_config_dir = project_config["config_dir"],
            project_data_dir = project_config["result_dir"],
            url_domain = project_config["url_domain"],
            scope_project = project_config["scope_project"],
            cookie = project_config["cookie"],
            from_timestamp = start_date,
            to_timestamp = end_date,
            class_download = class_download,
            local_proxy_port = 6000 if use_proxy else None
        )




def main():
    project_config = {
        "config_dir": "nilong_config",
        "result_dir": "nilong_data",
        "start_date": 1666022400000,
        "end_date": 1666108800000,
        "url_domain": "210.76.9.81",
        "scope_project": "chp/common",
        "cookie": "thingswise.web.proxy.session_id=s%3AwkUT1CIunnMCcl3qKa9fUO4OBypmKh23.PKDyqgLYPEYE%2B30ihMXjRkf90dtnHMi%2BGOrK6QZMzJc;",
    }
    class_download = [
        "CFBoiler",
        "Turbine",
    ]
    # print(project_config)
    downloading(project_config, class_download)


if __name__ == "__main__":
    main()

