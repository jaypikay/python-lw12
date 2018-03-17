#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Julian Knauer <jpk+lw12dev@goatpr0n.de>
#
# Distributed under terms of the MIT license.

from setuptools import setup, find_packages


setup(
    name='lw12',
    version='0.9.0',
    description='Library to control the Lagute LW-12 WiFi LED controller.',
    url='https://github.com/jaypikay/python-lw12',
    author='Julian Knauer',
    author_email='jpk+lw12dev@goatpr0n.de',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Smart Home',
        'Topic :: Software Development :: Home Automation',
        'Topic :: Software Development :: Light',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='smarthome homeautomation lw12 lagute led light development',
    py_modules=['lw12'],
    project_urls={
        'Issue Tracker': 'https://github.com/jaypikay/python-lw12/issues',
        'Source': 'https://github.com/jaypikay/python-lw12',
    },
)
