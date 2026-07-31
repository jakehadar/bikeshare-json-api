import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def read(filename):
    with open(os.path.join(HERE, filename), encoding='utf-8') as f:
        return f.read()


VERSION = '0.0.1'

setup(
    name='bikeshare-json-api',
    version=VERSION,
    author='Jake Hadar',
    author_email='jakehadar.dev@gmail.com',
    description='A json api for polling live Bikeshare feeds, demonstrating a simple gbfs-client (library) use-case.',
    url='https://github.com/jakehadar/bikeshare-json-api',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read('requirements.txt').splitlines(),
    license=read('LICENSE.txt'),
    tests_require=['pytest'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown'
)
