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
import argparse

##testing
import unittest

def command_line(args):
    '''
    This function defines the command line interface of the program.
    It is used only if dfitspy is used as an executable

    Parameters
    -----------
    None

    Returns
    -------
    args    Namespace with arguments
    '''

    ##create parser object
    parser = argparse.ArgumentParser(description='LOOTS: List python imports, version 19.9.1'+\
            '\nLicence: GPL \nExample>> loots -f hardcoded.py -d *', formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-f', '--file', help='a file name')
    parser.add_argument('-d', nargs='*', help='a file, a list of file separated by coma'+\
                                              'in unix system, the star [*] is accepted '+\
                                              'as well')
    parser.add_argument('-nR', help='Unactivate recursive if -d return directories, Default=False', \
            action='store_false')
    parser.add_argument('--tests', help='Start testing', action='store_true')
    parser.add_argument('--version', action='version', version='LOOTS v19.9.1')
    return parser.parse_args(args)


class Interfacetest(unittest.TestCase):
    '''
    Class that define the test for the command line interface
    '''
    def test_cli(self):
        '''
        This method tests the command line interface
        The principle is that we send some argument configuration
        and see what the interface is giving back
        '''
        dir_path = os.path.dirname(os.path.realpath(__file__))
        allfiles = os.listdir(dir_path)

        options = command_line(['--tests'])
        self.assertEqual(options.tests, True)

        options2 = command_line(['-f', allfiles])
        self.assertEqual(options2.tests, False)
        self.assertEqual(options2.file, allfiles)
