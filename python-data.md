



## Python 数据结构


## Python 字符串




## Python 字典

### 1.字典中的键映射多个值

普通做法：

```python
c = {
	"a": [1, 2, 3],
	"b": [4, 5]
}

d = {
	"a": (1, 2, 3),
	"b": (4, 5)
}

e = {
	"a": {1, 2, 3},
	"b": {4, 5}
}
```

defaultdict:

```python
from collections import defaultdict

c = defaultdict(list)
c["a"].append(1)
c["a"].append(2)
c["a"].append(3)
c["b"].append(4)
c["b"].append(5)

d = defaultdict(set)
d["a"].add(1)
d["a"].add(2)
d["a"].add(3)
d["b"].add(4)
d["b"].add(5)

e = {}
e.setdefault("a", []).append(1)
e.setdefault("a", []).append(2)
e.setdefault("b", []).append(4)
```

比较：

```python
# 普通做法
d = {}
for key, value in pairs:
	if key not in d:
		d[key] = []
	d[key].append(value)

# defaultdict
d = defaultdict(list)
for key, value in pairs:
	d[key].append(value)
```









## Python 文件