'''
---loots---

This file prepare the files in case -R
is used

@author(s): Romain Thomas
@year(s):  2019
@First version: 19.1.1
@Current version: 19.1.1
@Documentation url:
@Licence: GPL
@Testable: Yes
@Test data place (if any required): N.A.
'''


##standard library
import os

def prepare(inputfiles):
    '''
    This function return all the files found in inputfiles
    and all the files in the directory found in input files

    Parameters
    ----------
    inputfiles  :   list
                    of str (files and/or directory names)
    Returns
    -------
    allfiles    :   list
                    of str (files and files of subdirectories)                
    '''

    allfiles = []
    for i in inputfiles:
        if os.path.isfile(i):
            allfiles.append(i)

        if os.path.isdir(i):
            rec = os.listdir(i)
            for j in rec:
                if os.path.isdir(j):
                    rec2 = os.listdir(j)
                    for k in rec2:
                        allfiles.append(os.path.join(i,j,k))
                else:
                    allfiles.append(os.path.join(i,j))
    return allfiles
