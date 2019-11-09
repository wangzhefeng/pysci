

## 新建一个 Python 项目


### 项目结构(GitHub)

* root
	- `scripts`
	- `.gitignore`
	- `REAMDE.md`
	- `requirements.txt`
	- `setup.py`

### 1. requirements

```shell
# 生成 requirements.txt
pip freeze > requirements.txt

# 安装 requirements.txt
pip install -r requirements.txt
```


```python
pip install pipreqs
pipreqs ./ encoding=utf8
```