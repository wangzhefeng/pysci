# -*- coding: utf-8 -*-
# @Date    : 2019-01-30 18:46:34
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""
* 生成项目文件目录
* 目录构成: 
    - root\
        - data
        - scripts
        - jupyternotebook_doc
        - submission
"""

import sys
import os
sys.path.append('E:/DataScience/mltool/')

def mkdir(project):
    cur_path = os.getcwd()
    os.chdir(cur_path)

    os.mkdir(project)
    path = cur_path + project
    os.chdir(path)

    dirname = ["data", "scripts", "jupyternotebook_doc", "submission"]

    for d in dirname:
        os.mkdir(d)


def main():
    mkdir()

if __name__ == "__main__":
    main()