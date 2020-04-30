xrcalc
==========
xarray command-line calculation tool

**xrcalc** reads command-line arguments as Python statements and executes them on Python interpreter. The argument is quite similar to "the code cell of Jupyter notebook" while the arguments resides on a shell instead of "notebook". Especially **xrcalc** is specialised to support xarray calculation by pre-loading xarray and related modules.

The goal of "command-line as Python statement" approach is to achieve an immediate response with minimal effort. Thanks to the nautre of terminal user interface, the command-action-response cycle is simple, intuitive, and fast.


installation
--------------------

**xrcalc** supports Python 3.5 or later.

The best way to install **xrcalc** is to use pip3 Python package installer::

    >>> pip install xrcalc --user --upgrade

If you prefer to try the latest version of **xrcalc**, you can clone this repository and install it by using setup.py::

    >>> git clone https://github.com/grnydawn/xrcalc
    >>> python setup.py install --user


**xrcalc** command-line syntax
-------------------------------

This tool is invoked by a super-command of "microapp", which is installed with **xrcalc**. ::

        usage: microapp-xrcalc [-h] [--forward expr] [--share expr] [--downcast expr]
                               [--import IMPORT] [--assert-in expr]
                               [--assert-out expr] [--version] [-d DOC] [-s SHOW]
                               [-p PLOT]
                               [calc [calc ...]]

        positional arguments:
          calc                  Python statement 

        optional arguments:
          -h, --help            show this help message and exit
          ...
          -d DOC, --doc DOC     display xarray object documentation
          -s SHOW, --show SHOW  show xarray object content
          -p PLOT, --plot PLOT  plot xarray object

        This app may feed-forward following data to next app:
          data (type=typing.Any)    namelist dictionary object


         >>> microapp xrcalc 'x = xr.DataArray([1,2,3])' -s x
         <xarray.DataArray (dim_0: 3)>
         array([1, 2, 3])
         Dimensions without coordinates: dim_0


**xrcalc** basic usage 
-------------------------------

The following command create a list and display it on screen. The option "-s" or "--show" uses Python "print" function.::

    >>> microapp xrcalc 'x = [1,2,3]' -s x
    [1, 2, 3]

The following command domenstrates that each argument is a Python statement.::

    >>> microapp xrcalc 'x = [1,2,3]' 'y = x + [4]'  -s y
    [1, 2, 3, 4]

By using "-d" or "--doc" option, a short description of the data type can be displayed.::

    >>> microapp xrcalc 'x = [1,2,3]' 'y = x + [4]'  -d y
    'y' documentation
    ============================
    list() -> new empty list
    list(iterable) -> new list initialized from iterable's items
    list of y members:
    append                        clear                         copy
    count                         extend                        index
    insert                        pop                           remove

**xrcalc** xarray usage 
-------------------------------

**xrcalc** is equipped with xarray.::

    >>> microapp xrcalc 'x = xr.DataArray([1,2,3])' -s x
    <xarray.DataArray (dim_0: 3)>
    array([1, 2, 3])
    Dimensions without coordinates: dim_0

By using plotting feature of **xrcalc**, a plot can be created easily using "-p" or "--plot" option::

    >>> microapp xrcalc 'x = xr.DataArray([1,2,3])' -p x

"-d" option produces documentation of the data type of  the variable "x", which DataArray of xarray.::

    >>> microapp xrcalc 'x = xr.DataArray([1,2,3])' -d x

        'x' documentation
        ============================
        N-dimensional array with labeled coordinates and dimensions.

            DataArray provides a wrapper around numpy ndarrays that uses labeled
            dimensions and coordinates to support metadata aware operations. The API is
            similar to that for the pandas Series or DataFrame, but DataArray objects
            can have any number of dimensions, and their contents have fixed data
            types.
        ...
        list of x members:
        T                             all                           any
        argmax                        argmin                        argsort
        assign_attrs                  assign_coords                 astype
        attrs                         bfill                         broadcast_equals
        ...
        to_series                     to_unstacked_dataset          transpose
        unify_chunks                  unstack                       values
        var                           variable                      weighted


Let's add a dimension to the DataArray of "x"::

    >>> microapp xrcalc 'x = xr.DataArray([1,2,3], dims=("x",))' -s x
    <xarray.DataArray (x: 3)>
    array([1, 2, 3])
    Dimensions without coordinates: x


