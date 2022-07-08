# Python 开发






# 设置 pip 软件源

## windows

1. 打开 `C:\Users\username\AppData\Roaming\`
2. 在上述目录下新建文件夹 `pip`
3. 在 `pip` 文件夹中新建 `pip.ini` 文件
4. 在 `pip.ini` 文件中添加如下内容

```ini
[global]
timeout=6000
index-url=https://pypi.tuna.tsinghua.edu.cn/simple/
trusted-host=pypi.tuna.tsinghua.edu.cn
```

## Linux/macOS

1. 进入 `~` 目录

```bash
$ cd ~
```

2. 在 `~` 目录下新建 `.pip` 文件夹

```bash
$ mkdir .pip
```

3. 进入 `.pip` 文件夹

```bash
$ cd .pip
```

4. 创建文件 `pip.conf`

```bash
$ touch pip.conf
```

5. 在 `pip.conf` 中添加如下内容

```ini
[global]
timeout=6000
index-url=https://pypi.tuna.tsinghua.edu.cn/simple/
[install]
trusted-host=pypi.tuna.tsinghua.edu.cn
```

