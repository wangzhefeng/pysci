
Python 科学计算
========================

1. Python 数据处理
------------------------






2. Python 数据建模
------------------------







3. Python 科学计算工具包
------------------------

-  `SciPy <https://www.scipy.org/>`__

   -  core packages:

      -  `Python <https://www.python.org/>`__

      -  `Numpy <https://numpy.org/>`__

      -  `Scipy library <https://www.scipy.org/index.html>`__

      -  `Matplotlib <https://matplotlib.org/users/installing.html>`__

   -  Productivity and high-performance computing:

      -  `IPython <>`__

         -  `pyzmq <>`__

         -  `tornado <>`__

      -  `Jupyter <https://jupyter.org/>`__

      -  `Cython <http://docs.cython.org/en/latest/index.html>`__

      -  `Dask <>`__

      -  `Joblib <>`__

      -  `IPyParallel <>`__

   -  Data and computation:

      -  `pandas <>`__

      -  `SymPy <>`__

      -  `scikit-image <>`__

      -  `scikit-learn <>`__

      -  `h5py <>`__

      -  `PyTables <>`__

   -  Quality assurance

      -  `nose <>`__

      -  `pytest <>`__

      -  `numpydoc <>`__

-  Date & Time

   -  `time <>`__

   -  `datetime <>`__

   -  `pytz <>`__

   -  `dateutil <>`__

-  Models

   -  `tsfresh <>`__

   -  `tslearn <>`__


安装命令
~~~~~~~~~~~~~~~~~~~~~~~~~


Scipy:


.. code-block:: shell

   python -m pip install [--user] numpy scipy matplotlib ipython jupyter pandas sympy nose


Numpy:

.. code-block:: shell

   $ pip install numpy

Pandas:

.. code-block:: shell

   $ pip install pandas

matplotlib:

.. code-block:: shell

   python -m pip install -U pip
   python -m pip install -U Matplotlib

sklearn:

.. code-block:: shell

   pip install -U scikit-learn
   pip3 install -U scikit-learn

.. code-block:: shell

   $ python -m pip show scikit-learn # to see which version and where scikit-learn is installed
   $ python -m pip freeze # to see all packages installed in the active virtualenv
   $ python -c "import sklearn; sklearn.show_versions()"

   $ python3 -m pip show scikit-learn # to see which version and where scikit-learn is installed
   $ python3 -m pip freeze # to see all packages installed in the active virtualenv
   $ python3 -c "import sklearn; sklearn.show_versions()"


scipy:

.. code:: shell

   pip install scipy


seaborn:

.. code:: shell

   pip install seaborn

Jupyter:

.. code-block:: shell

    $ python -m pip install jupyter

Jupyter Notebook:

.. code-block:: shell

    $ pip install notebook

Jupyter Lab:

.. code-block:: shell

    $ pip install jupyterlab

Voila:

.. code-block:: shell

    $ pip install voila
