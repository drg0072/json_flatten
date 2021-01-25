from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='json_python_flatten',
    packages=find_packages(include=['json_python_flatten']),
    version='0.1.3',
    description='Flatten JSON objects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Dheeraj Gupta',
    author_email='drg0072@gmail.com',
    url='https://github.com/drg0072/json_flatten',
    keywords=['json', 'flatten'],
    classifiers=[],
    entry_points={},
    install_requires=[]
)
