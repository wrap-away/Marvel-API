from setuptools import setup, find_packages
from codecs import open
from os import path


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list


file_path = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(file_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='marvel',

    version='0.1.0',

    description='An API Wrapper For Marvel API: https://developer.marvel.com',
    long_description=long_description,

    url='https://github.com/wrap-away/Marvel',

    author='Wrap-Away',
    author_email='wrap_away@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Environment :: Web Environment',

        'Operating System :: OS Independent',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='marvel marvel-api spiderman marvel-wrapper marvel-sdk marvel-python',

    packages=find_packages(exclude=['sample']),

    install_requires=requirements(),
)
