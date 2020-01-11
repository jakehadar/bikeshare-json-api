from pkg_resources import resource_string
from setuptools import setup, find_packages

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
    install_requires=resource_string(__name__, 'requirements.txt').decode('utf-8'),
    license=resource_string(__name__, 'LICENSE.txt').decode('utf-8'),
    tests_require=['pytest'],
    long_description=resource_string(__name__, 'README.md').decode('utf-8'),
    long_description_content_type='text/markdown'
)
