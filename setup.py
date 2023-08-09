#!/usr/bin/env python
from setuptools import setup



with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='simpar-cli',
    version='0.0.1',
    packages=['simpar'],
    install_requires=[
        'numpy', 'argparser', 'matplotlib', 'scikit-image', 'opencv_python'
    ],
    license='MIT license',
    description="simple cli for paragraphe recognition",
    long_description= long_description,
    long_description_content_type="text/markdown",

    
    url='https://github.com/darixsamani/simpar-cli',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],    
    python_requires='>=3.6',                
    py_modules=["simpar_cli"],             
    package_dir={'':'./src'},     
    install_requires=open('requirement.txt').read().split()                 
)
