import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

long_description = read('README.md')

install_requires = [
    'biopython >= 1.79',
]

def read_version():
    for line in open(os.path.join('merge_gbk_records', '__init__.py'), 'r'):
        if line.startswith('__version__'):
            return line.split('=')[-1].strip().strip("'")

setup(
    name='merge-gbk-records',
    version=read_version(),
    author='Kai Blin',
    author_email='kblin@biosustain.dtu.dk',
    description='Merge multiple GenBank files using a spacer sequence',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'merge-gbk-records=merge_gbk_records.__main__:main',
        ],
    },
    packages=['merge_gbk_records'],
    url='https://github.com/kblin/merge-gbk-records/',
    license='Apache Software License',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
