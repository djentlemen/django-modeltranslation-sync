# coding: utf-8
from __future__ import unicode_literals

from setuptools import setup, find_packages


setup(
    name='django_trans_sync',
    version='0.1',
    license='MIT',

    author='Martin Hořák',
    author_email='horak@styrax.info',

    description='',
    long_description=open('README.md').read(),
    url='https://github.com/djentlemen/django-trans-sync',

    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django',
    ],

    classifiers=(
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
)
