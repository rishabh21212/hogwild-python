#!/usr/bin/env python
import os
from setuptools import setup, find_packages

# Check if we are in a Docker environment
use_docker = os.getenv('USE_DOCKER', 'false').lower() == 'true'

# Set dependencies based on the environment
if use_docker:
    install_requires = [
        'pytest>=7.0.0',
        'grpcio>=1.54.0',
        'grpcio-tools>=1.54.0',
        'numpy>=1.24.0'
    ]
else:
    install_requires = [
        'pytest==2.9.2',
        'grpcio==1.10.1',
        'grpcio-tools==1.10.1',
        'numpy==1.14.2'
    ]

setup(
    name='hogwild',
    url='',
    author='',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    version='0.0.1',
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False
)
