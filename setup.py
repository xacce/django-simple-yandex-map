__author__ = 'winzard'
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_ymap',
    version='1.1',
    packages=['django_ymap'],
    include_package_data=True,
    url='https://github.com/xacce/django-simple-yandex-map/',
    license='MIT License',
    author='DveBukvy',
    author_email='mail@dvebukvy.ru',
    description='several useful tools for any django-project',
    long_description=README,
    install_requires=[]

)