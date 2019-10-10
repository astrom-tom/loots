'''
---loots---
main file

@author(s): Romain Thomas
@year(s):  ex 2018
@First version: 19.9-0
@Current version: 19.9-0
@Telescope(s): ALL
@Instrument(s): ALL
@Documentation url:
@Licence: GPL
@Testable: Yes
@Test data place (if any required): inside the package
'''


###Python standard library
import os
import sys


###local imports
from . import cli
from .loot import LOOT
#from . import tests
from . import misc

def main():
    '''
    This is the main function of the program.
    '''
    ###first we load the command line interface
    args = cli.command_line(sys.argv[1:])
    if not args.tests and args.file is None:
        print('You did not ask LOOTS anything, please use --help....exit...')
        sys.exit()

    ##start the tests if required
    #if args.tests:
    #    tests.test()
        ###exit code
    #    sys.exit()

    else:
        ###do something
        F = LOOT(args.file)
        ##if we can process it then we go
        depend_from = []
        if args.d and args.nR:
            allfiles = misc.prepare(args.d)
        elif args.d and not args.nR:
            allfiles = args.d
        else:
            allfiles = []

    
        if F.process == True:
            print('\n\033[1m[LOOTS File --> %s]\033[0;0m'%F.name)
            ##we extract the lines
            all_imports, all_from = F.extract_lines()
            ###then the direct imports
            all_imports = F.read_imports(all_imports)
            ###then the ones with 'from'
            other_imports, local_dir, local_files = F.read_from(all_from, allfiles)
            ###if other files were given we analyse them as well
            if args.d:
                for j in allfiles:
                    if j != args.file:
                        D = LOOT(j)
                        if D.process:
                            all_impots_D, all_from_D = D.extract_lines()
                            other_imports_D, local_dir_D, local_files_D = F.read_from(all_from_D, allfiles)
                            ###if the current file we analyse (-f) is inside one of the other
                            ###files the we catch it
                            if F.basename in other_imports or F.basename in local_dir_D or \
                                    F.basename in local_files_D:
                                depend_from.append(j)

            depend_on = all_imports + other_imports + local_dir + local_files
            final_depend_from = []
            final_depend_on = []

            if len(depend_on) > len(depend_from):
                for k in enumerate(depend_on):
                    final_depend_on.append(depend_on[k[0]])
                    if k[0]<len(depend_from):
                        final_depend_from.append(depend_from[k[0]])
                    else:
                        final_depend_from.append('')

            elif len(depend_on) < len(depend_from):
                for k in enumerate(depend_from):
                    final_depend_from.append(depend_from[k[0]])
                    if k[0]<len(depend_on):
                        final_depend_on.append(depend_on[k[0]])
                    else:
                        final_depend_on.append('')
            else:
                final_depend_on = depend_on
                final_depend_from = depend_from

            #######DISPLAY
            ##red line
            print('\t\033[1m\033[91m'+75*'-'+'\033[0m')
            ##header
            print('\033[1m\033[94m'+"\t--- {:^20s}  ------ {:^35s} ".format('Depends on', \
                    'Is dependency of')+'\033[0m')
            ##red line
            print('\t\033[1m\033[91m'+75*'-'+'\033[0m')
            ###results
            for i,j in zip(final_depend_on, final_depend_from): 
                line = "\t--> {:^20s} \033[94m \033[0m -----> {:^35s} ".format(str(i), str(j))
                print(line)
            ##redline
            print('\t\033[1m\033[91m'+75*'-'+'\033[0m\n')

if __name__ == "__main__":
    main()
