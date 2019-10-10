from setuptools import setup

__version__ = '19.10.1'
__credits__ = "Romain Thomas"
__license__ = "GNU GPL v3"
__maintainer__ = "Romain Thomas"
__email__ = "the.spartan.proj@gmail.com"
__status__ = "released"

setup(
   name = 'loots',
   version = __version__,
   author = __credits__,
   packages = ['loots'],
   entry_points = {'gui_scripts': ['loots = loots.__main__:main',],},
   description = 'LOOTS: List pythOn impOrTS',
   license = __license__,
   #url = __website__,
   python_requires = '>=3.6',
   install_requires = [
       "numpy >= 1.14.3",
       "fitsio == 0.9.11",
   ],
   include_package_data=True,
)
