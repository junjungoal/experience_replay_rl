# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Experience Replay Library for RL',
    long_description=readme,
    author='Jun Yamada',
    author_email='sample@sample.com',
    install_requires=['numpy'],
    url='https://github.com/junjungoal/experience_replay_rl',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

