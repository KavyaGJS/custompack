from setuptools import setup

setup(
    name='custompack',  
    version='0.0.1',  
    description='A Python package for NLP tasks and utilities',
    url='https://github.com/KavyaGJS/nlppack',  
    author='KavyaGJS', 
    author_email='kavyamujk@gmail.com',  
    packages=['custompack'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
