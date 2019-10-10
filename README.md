What is loots?
==============
loots is a simple tool that was created to look at interdependcies between internal modules of a single python project. Given a file (passed with one of the argument), it will list all the imported modules and where this file is used in the project.


Interface
=========

	usage: loots [-h] [-f FILE] [-d [D [D ...]]] [-nR] [--tests] [--version]

	LOOTS: List python imports, version 19.9.1
	Licence: GPL 
	Example>> loots -f hardcoded.py -d *

	optional arguments:
	  -h, --help            show this help message and exit
	  -f FILE, --file FILE  a file name
	  -d [D [D ...]]        a file, a list of file separated by comain unix system, 
				the star [*] is accepted as well
	  -nR                   Unactivate recursive if -d return directories, Default=False
	  --tests               Start testing
	  --version             show program's version number and exit


Output
======

    [LOOTS File --> generic_tools/make_OB.py]
	---------------------------------------------------------------------------
	---      Depends on       ------          Is dependency of           
	---------------------------------------------------------------------------
	-->          os            ----->     generic_tools/make_night.py     
	-->       datetime         ----->              tests.py               
	-->       unittest         ----->                                     
	-->        numpy           ----->                                     
	-->     ephemerides        ----->                                     
	-->       catscii          ----->                                     
	-->         misc           ----->                                     
	-->      hardcoded         ----->                                     
	---------------------------------------------------------------------------


Installation?
=============

The last loots version is v20.1.1 and is available in the pypi repository. To install it::

     pip install loots [--user]

Using this command will allow you not to have to install any other package. Pip will install what is missing for you.


----


**Copyright**

loots is a free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software Foundation,
version 3 of the License.

loots is distributed without any warranty; without even the implied warranty of merchantability
or fitness for a particular purpose.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with the program.
If not, see http://www.gnu.org/licenses/ .

----
