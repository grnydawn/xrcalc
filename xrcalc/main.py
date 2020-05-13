"Microapp xarray caculator module"

import os.path, pkgutil, importlib

import xarray
import numpy
import pandas
import matplotlib
import matplotlib.pyplot

from typing import Any
from microapp import App, funcargseval


mods = {}
members = {}
pkgpath = os.path.dirname(xarray.__file__)

for x, modname, y in pkgutil.walk_packages([pkgpath]):
    if modname.startswith("_"):
        continue

    mods[modname] = {}

    #print("************** in module %s ********************" % modname)

    try:
        mod = importlib.import_module('.' + modname, package='xarray')

        for member in dir(mod):
            if not member.startswith("_"):
                #print("    %s" % member)
                obj = getattr(mod, member)

                mname = member.lower()
                mods[modname][mname] = obj

                if mname in members:
                    if all([obj is not o for o in  members[mname]]):
                        members[mname].append(obj)
                else:
                    members[mname] = [obj]

    except ImportError:
        pass


class XarrayCalculator(App):

    _name_ = "xrcalc"
    _version_ = "0.1.6"
    _description_ = "Microapp xarray calculator"
    _long_description_ = "Microapp xarray calculator"
    _author_ = "Youngsung Kim"
    _author_email_ = "youngsung.kim.act2@gmail.com"
    _url_ = "https://github.com/grnydawn/xrcalc"

    def __init__(self, mgr):

        self.add_argument("calc", nargs="*", help="namelist file")
        self.add_argument("-d", "--doc", action="append",
                help="display xarray object documentation")
        self.add_argument("-s", "--show", action="append",
                help="show xarray object content")
        self.add_argument("-p", "--plot", action="append",
                help="plot xarray object")

        self.register_forward("data", type=Any, help="namelist dictionary object")

    def perform(self, mgr, args):

        data = []

        for calc in args.calc:
            data.append(calc["_"])

        val = None
        lenv = {"xarray": xarray, "xr": xarray,
                "numpy": numpy, "np": numpy,
                "pandas": pandas, "pd": pandas,
                "matplotlib": matplotlib, "mpl": matplotlib,
                "pyplot": matplotlib.pyplot, "plt": matplotlib.pyplot,
               }

        try:
            exec("\n".join(data), self._env, lenv)

        except Exception as err:
            print(err)
            return

        if args.doc:
            for darg in args.doc:
                objpath = darg["_"].split(".")
                objname = objpath[0].lower() 

                if objname in members:
                    obj = members[objname][0]

                elif objname in lenv:
                    obj = lenv[objname]

                else:
                    print("'%s' is not found." % objpath[0])
                    return

                objorgname = getattr(obj, "__name__", objname)

                if len(objpath) > 1:
                    subobj = getattr(obj, objpath[1], None)
                    if subobj:

                        print("'%s' of '%s' documentation" % (objpath[1], objorgname))
                        print("======================================")
                        print(getattr(subobj, "__doc__", "member"))

                else:
                    print("'%s' documentation" % objorgname)
                    print("============================")
                    print(getattr(obj, "__doc__", "Can not find '%s' in xarray" % objname))

                    print("list of %s members:" % getattr(obj, "__name__", objname))

                    o = []
                    for attr in dir(obj):
                        if not attr.startswith("_"):
                            o.append(attr)

                    for a,b,c in zip(o[::3],o[1::3],o[2::3]):
                        print('{:<30}{:<30}{:<}'.format(a,b,c))

        if args.show:
            for parg in args.show:
                val = parg["_"]
                exec("print(%s)" % val, self._env, lenv)

        if args.plot:
            for parg in args.plot:
                val = parg["_"]
                sout = val.split(",", 1)
                if len(sout) > 1:
                    plotdata, rem = sout
                else:
                    plotdata, rem = val, ""

                (vargs, kwargs), out = funcargseval(rem, self._env)

                if hasattr(lenv[plotdata, "plot"):
                    lenv[plotdata].plot(*vargs, **kwargs)
                    matplotlib.pyplot.show()

                else:
                    print("'%s' does not support plotting: %s" % lenv[plotdata])

        del lenv["xarray"]
        del lenv["xr"]
        del lenv["numpy"]
        del lenv["np"]
        del lenv["matplotlib"]
        del lenv["mpl"]
        del lenv["pyplot"]
        del lenv["plt"]

        for a in lenv:
            if a.startswith("_"):
                del lenv[a]

        self.add_forward(data=lenv)
