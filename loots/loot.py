'''
---loots---

This file organises the command line interface (and unit test it)

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

##third party
import numpy

##testing
import unittest

class LOOT():
    '''
    This class is the main object of loots. It looks for all the files
    and the files
    '''
    def __init__(self, name):
        '''
        Class initialization
        Parameter
        ---------
        name    :   str
                    name of the file
        '''
        self.top_dep = []
        self.bottom_dep = []
        self.name = name
        self.basename = os.path.basename(self.name)[:-3]
        self.all_imports = []
        self.all_files = []
        if self.name[-3:] == '.py' and self.basename != '__init__.py' and \
                os.path.isdir(self.name) is False:
            self.process = True
        else:
            self.process = False


    def extract_lines(self):
        '''
        Method that extracts, from the current file, all the lines 
        containing imports
        '''
        with open(self.name, 'r') as F:
            all_imports = []
            all_from = []
            for i in F.readlines():
                line = i.strip()
                if len(line)>0 and line[0] != '#':
                    ###check imports
                    if line[:7] == 'import ':
                        all_imports.append(line)
                    if line[:5] == 'from ':
                        all_from.append(line)
        return all_imports, all_from

    def read_imports(self, imports):
        '''
        Method that extract the direct imports like
        'import sys' will get back 'sys'
        Parameters
        ----------
        imports     :   list
                        list of lines with direct imports
        '''
        all_imports = []
        for line in imports:
            ####check id there is a 'as' in the line
            if ' as ' in line:  
                line = self.remove_as(line) 
            ###remove the import and get 
            ###all the import names
            imports = line[7:].split(',')

            ###strip the name
            for i in range(len(imports)):
                imports[i] = imports[i].strip() 
                all_imports.append(imports[i])

        return all_imports 

    def read_from(self, froms, allfiles):
        '''
        Method that extract the undirect imports like
        'from X import Y' will get you back 'Y' or
        'from . import Z' will get you back 'Z' or
        'from .source_file import submodule' will get you back 'source_file'
        'from .source_directory import code_file' will get you back 'code_file'
        Parameters
        ----------
        froms       :   list
                        list of lines with undirect imports
        allfiles    :   list
                        list of all other files we look for
        '''
        local_files = []
        local_dir = []
        other_imports = []

        for line in froms:
            ###check id there is a 'as' in the line
            if ' as ' in line:  
                line = self.remove_as(line) 

            ##remove the from
            split = line[5:].split()

            ###get if we are looking in the local
            ###directory
            if (split[0] == '.' and len(split[0]) == 1) or \
               (split[0] == '..' and len(split[0]) == 2) or \
               (split[0] == '...' and len(split[0]) == 3):
                importline = self.remove_from(line)
                loc = self.read_imports([importline])
                for p in loc:
                    local_files.append(p)
                continue

            ### get if we take a local file or in a directory
            elif (split[0][0] == '.' and len(split[0]) != 1) or \
               (split[0][0:2] == '..' and len(split[0]) != 2) or \
               (split[0][0:3] == '...' and len(split[0]) != 3) :
                localname = split[0].strip('.')
                if localname+'.py' in [os.path.basename(i) for i in allfiles]:
                    local_files.append(localname)
                else:
                    localdir = localname
                    importline = self.remove_from(line)

                    for p in self.read_imports([importline]):
                        local_dir.append(p)
                continue

            else: 
                ###type from installed package import module
                l = self.remove_import(line)[5:]
                other_imports.append(l)

        return other_imports, local_dir, local_files 

    def remove_as(self, line):
        '''
        This method remove the 'as ...' in an import
        like import numpy as
        Parameter
        ---------
        line    :   str
                    line containing the 'as' word
        Return
        ------
        new_l   :   str
                    first part of the line truncated
                    at 'as'
        
        '''
        new_line = line.split(' ')
        index = numpy.where(numpy.array(new_line) == 'as')
        new_l = ' '.join(new_line[:index[0][0]])
        return new_l 

    def remove_from(self, line):
        '''
        This method remove the 'from ...' in an import
        like 'from x import y'
        Parameter
        ---------
        line    :   str
                    line containing the 'as' word
        Return
        ------
        new_l   :   str
                    first part of the line truncated
                    at 'as'
        
        '''
        new_line = line.split(' ')
        index = numpy.where(numpy.array(new_line) == 'import')
        new_l = ' '.join(new_line[index[0][0]:])
        return new_l 

    def remove_import(self, line):

        '''
        This method remove the 'import ...' in an import
        like 'from x import y'
        Parameter
        ---------
        line    :   str
                    line containing the 'as' word
        Return
        ------
        new_l   :   str
                    first part of the line truncated
                    at 'as'
        
        '''
        new_line = line.split(' ')
        index = numpy.where(numpy.array(new_line) == 'import')
        new_l = ' '.join(new_line[:index[0][0]])
        return new_l 


