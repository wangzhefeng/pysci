
# Install packages

```shell
pip install virtualenv
pip install virtualenvwrapper
```

# Configuration 

## Location of Environments and Project Directories

```shell
# sudo subl ~/.bashrc
export WORKON_HOME="$HOME/.virtualenvs"
export PORJECT_HOME="$HOME/Devel"
source /home/zfwang/anaconda3/bin/virtualenvwrapper.sh
# source ~/.bashrc
```







# Create Virtual Env

## 1.快速开始

```shell
# List the virtual env
workon

# make a virtual env
mkvirtualenv name_env

# Enter the Python or jupyter env
jypyter lab
jupyter notebook
python3

# see the new package installed
lssitepackages

# see all virtual envs
ls $WORKON_HOME

# switch between environments
workon another_env
echo $VIRTUAL_ENV

# `psotmkvirtualenv`
(env1)$ echo 'cd $VIRTUAL_ENV' >> $WORKON_HOME/postactivate
(env1)$ workon env2
(env2)$ pwd

(env2)$ echo 'pip install django' >> $WORKON_HOME/postactivate
(env3)$ mkvirtualenv env3 
```



# Command Reference

* Managing Env
    - mkvirtualenv
    - mktmpenv
    - lsvirtualenv
    - showvirtualenv
    - rmvirtualenv
    - cpvirtualenv
    - allvirtualenv
* Controlling Active Env
    - workon
    - deactivate
* Navigating to an Env
    - cdvirtualenv
    - cdsitepackages
    - lssitepackages
* Path Management
    - add2virtualenv
    - toggleglobalsitepackages
* Project Directory Management
    - mkproject
    - setvirtualenvproject
    - cdproject
* Managing Installed Packages
    - wipeenv
* Others
    - virtualenvwrapper


## 1.Managing Env

> 1.1 Create Env in `WORKON_HOME`

```shell
$ workon
$ mkvirtualenv [-a project_path] [-i package] [-r requirements.txt] [virtualenv options] ENVNAME
```

> 1.2 Create Env in `WORKON_HOME`

```shell
$ mktmpenv [(-c|--cd)|(-n|--no-cd)] [VIRTUALENV_OPTIONS]
```

> 1.3 List all of the Env

```shell
$ lsvirtualenv [-b] [-l] [-h]
```
> 1.4 Show the Details for a single Env

```shell
$ showvirtualenv [env]
```

> 1.5 Remove an Env from `WORKON_HOME`

```shell
$rmvirtualenv ENVNAME
```

> 1.6 Duplicate an existing Env

```shell
$ cpvirtualenv ENVNAME [TARGETENVNAME]
```
> 1.7 Run a command in all ENV under `WORKON_HOME`

```shell
$ allvirtualenv command with arguments
```

```shell
$ allvirtualenv pip install -U pip
```

## Controlling Active Env

> 2.1 List or Change working Env

```shell
$ workon [(-c|--cd)|(-n|--no-cd)] [environment_name|"."]
```

> 2.2 Deactivate

```shell
$ deactivate
```

## Navigating to an Env

> 3.1 Change the CWD to `$VIRTUAL_ENV`

```shell
cdvirtualenv [subdir]
```

> 3.2 Change the CWD to `site-packages` for `$VIRTUAL_ENV`

```shell
cdsitepackages [subdir]
```

> 3.3 Show the content of the `site-package` of the CAV(current-active virtualenv)

```shell
lssitepackages
```

## Path Management

> 4.1 Adds the specified directories to the Python path for the currently-active virtualenv.

```shell
$ add2virtualenv directory1 directory2 ...
```

> 4.2 Controls whether the active virtualenv will access the packages in the global Python site-packages directory.

```shell
$ toggleglobalsitepackages [-q]
```


## 5.Project Directory Management

> 5.1 Create a Env in `WORKON_HOME` and Pro in `PROJECT_HOME`

```shell
mkproject [-f|--force] [-t template] [virtualenv_options] ENVNAME
```

> 5.2 Bind an existing Env to an existing Proj

```shell
$ cd /home/zfwang/Documents/ml
$ workon
$ workon mlenv
(mlenv)$ setvirtualenvproject [virtualenv_path project_path]
(mlenv)$ setvirtualenvproject mlenv mlproj
(mlenv)$ cd mlproj
```

> 5.3 Change the CWD to one specified as the ProjDir for the active Virtual

```shell
$ cdproject
```

## 6.Managing Installed Packages

> 6.1 Remove all of the installed third-party packages in the current virtualenv

```shell
$ wipeenv
```

## 7.Others

```shell
$ virtualenvwrapper
```