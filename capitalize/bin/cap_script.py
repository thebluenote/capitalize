#!/usr/bin/env python

"""
A really simple script just to demonstrate packaging
    Usage:
        cap_script_2.py INFILENAME [OUTFILENAME]

"""

import sys, os
from capitalize import capital_mod
import docopt


def main(infile, outfile):
    """
    startup function for running a capitalize as a script
    """

    
    # do the real work:
    print("Capitalizing: %s and storing it in %s"%(infilename, outfilename))
    
    capital_mod.capitalize(infilename, outfilename)
    
    print("I'm done")

def get_arg_dict(): 
    return docopt.docopt(__doc__)

if __name__ == "__main__":
    
    infilename, outfilename = get_arg_dict().values()
        
    if not outfilename:
        root, ext = os.path.splitext(infilename)
        outfilename = root + "_cap" + ext
    
    main(infilename, outfilename)    
