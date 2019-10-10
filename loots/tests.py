'''
This file organises the tests of the library
'''

#testing
import unittest

#local imports
from . import cli

def test():
    '''
    This function calls the test of each module and run them
    '''
    ###test the command line interface
    print('\n\033[1m---UnitTest the command interface\033[0;0m')
    suite = unittest.TestLoader().loadTestsFromModule(cli)
    unittest.TextTestRunner(verbosity=2).run(suite)
