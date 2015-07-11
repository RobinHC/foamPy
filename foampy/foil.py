"""
Module for working with foil data.
"""
from __future__ import division, print_function
import os

class FoilData(object):
    """
    Object that represents a foil characteristic database.
    """
    def __init__(self):
        self.alpha = []
        self.cl = []
        self.cd = []
        self.cm = []

    def read(self, fpath, startline=None, endline=None):
        """
        Reads foil data from file. Format is detected automatically, but
        column order is not.
        """
        in_block = False
        with open(fpath, "r") as f:
            for n, line in enumerate(f.readlines()):
                if startline is not None and n+1 < startline:
                    pass
                elif endline is not None and n+1 > endline:
                    pass
                else:
                    try:
                        a = [float(n) for n in line.replace(",", " ").split()]
                        self.alpha.append(a[0])
                        self.cl.append(a[1])
                        self.cd.append(a[2])
                        if len(a) > 3:
                            self.cm.append(a[3])
                        in_block = True
                    except (ValueError, IndexError):
                        if in_block:
                            break

    def write(self, fpath):
        """
        Write foil data to file in OpenFOAM format.
        """
        with open(fpath, "w") as f:
            f.write("// Reformatted with foamPy\n")
            f.write("// (alpha_deg cl cd)\n" )
            for a, cl, cd in zip(self.alpha, self.cl, self.cd):
                f.write("({} {} {})\n".format(a, cl, cd))


def reformat_foildata(input_path, output_path, startline=None, endline=None):
    """
    Reformats foil data file into a list of 3-element OpenFOAM lists.
    """
    fd = FoilData()
    fd.read(input_path, startline, endline)
    fd.write(output_path)

def test_reformat_foildata():
    """
    Tests the `foampy.foil.reformat_foildata` function.
    """
    ifp = "test/NACA_0021.dat"
    ofp = "test/NACA_0021.txt"
    ofp2 = "test/NACA_0021_2.txt"
    ofp3 = "test/NACA_0021_3.txt"
    if os.path.isfile(ofp):
        os.remove(ofp)
    reformat_foildata(ifp, ofp)
    if os.path.isfile(ofp2):
        os.remove(ofp2)
    reformat_foildata(ifp, ofp2, startline=118)
    if os.path.isfile(ofp3):
        os.remove(ofp3)
    reformat_foildata(ifp, ofp3, startline=118, endline=119)
