from distutils.core import setup
setup(
    name='hangrypy',
    packages=['hangrypy'],
    version='0.1',
    description='A random test lib',
    author='Scott Cooper',
    author_email='scttcper@gmail.com',
    url='https://github.com/scttcper/hangry-py',
    download_url='https://github.com/scttcper/hangry-py/tarball/0.1',
    keywords=['hangry', 'recipe', 'parser', 'isodate'],
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
    classifiers=[],
)
