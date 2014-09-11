#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'scnparse',
    version = '0.1',
    description = 'Parser of MaSzyna Simulator scenery files',
    author = 'Zbigniew Mandziejewicz',
    author_email = 'shaxbee@gmail.com',
    packages = ['grammar', 'parser'],
    install_requires = ['pyparsing>=1.5.0'],
    setup_requires = ['nose']
);        
