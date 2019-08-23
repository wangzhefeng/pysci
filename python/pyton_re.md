---
title: Python正则表达式
date: 2019-03-04 16:00:35
tags:
- python
---

# Python正则表达式


```python
import re
```


```python
import json

string = '[{"requestid": "b9a9b0f264a44ec28f7d20ed4826c691", "content": "前台Ennma 退房很快"阮冬琴开发票也很快"两个人配合不错"}]'

# 正则表达式
# res = "".join([i for i in string if u'\u4e00' <= i <= u'\u9fff'])
# print(res)


# Json解析
while True:
	try:
		res = json.loads(string)[0]["content"]
		print(res)
		break
	except json.JSONDecodeError as e:
		str_index = int(str(e).split(" ")[-1][:-1])
		
```