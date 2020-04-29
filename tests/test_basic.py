from microapp import MicroappProject

import os

here = os.path.dirname(os.path.abspath(__file__))
#namelist = os.path.join(here, "data.nl")
#jsondata = os.path.join(here, "data.txt")

def test_basic():

    prj = MicroappProject()

    cmd = ["xrcalc"]
    cmd.append("data = xr.DataArray(np.random.randn(2, 3), dims=('x', 'y'), coords={'x': [10, 20]})")
    cmd.append("temp = xr.DataArray(pd.Series(range(3), index=list('abc'), name='foo'))")
    cmd.append("-s")
    cmd.append("temp")

    ret = prj.main(" ".join(["\"%s\"" % c for c in cmd]))

    assert ret == 0
    #assert os.path.exists(jsondata)

    #os.remove(jsondata)
