try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
  name='XmlTestRunner',
  version='0.3',
  author='Sebastian Rittau',
  author_email='',
  url='https://github.com/srittau/xmltestrunner',
  py_modules=['xmlrunner']
)
