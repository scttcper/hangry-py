import re

from setuptools import setup
from setuptools.command.test import test


# use pytest instead
def run_tests(self):
    pyc = re.compile(r'\.pyc|\$py\.class')
    test_file = pyc.sub('.py', __import__(self.test_suite).__file__)
    raise SystemExit(__import__('pytest').main(['-xv', test_file]))
test.run_tests = run_tests


setup(
    name='hangrypy',
    packages=['hangrypy'],
    version='0.1',
    description='Parse recipies from microformats similar to the hangry gem',
    author='Scott Cooper',
    author_email='scttcper@gmail.com',
    url='https://github.com/scttcper/hangry-py',
    download_url='https://github.com/scttcper/hangry-py/tarball/0.1',
    keywords=['hangry', 'recipe', 'parser', 'isodate'],
    install_requires=[
        'beautifulsoup4',
        'requests',
        'isodate',
    ],
    tests_require=['pytest'],
    test_suite='hangrytest',
    classifiers=[],
)
