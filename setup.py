"""
pip-plant installs your dependencies.
"""

from setuptools import setup

with open('README.md') as readme:
    long_description = readme.read()

setup(
  name='pip-plant',
  packages=['plant'],
  version='0.3.3',
  license='MIT',
  description='Plant simplifies Python package management for your projects.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Ideas Labs',
  author_email='saurabh.chaturvedi63@gmail.com',
  url='https://github.com/Ideas-Labs/plant',
  scripts=['plant/pip-plant'],
  install_requires=['envoy'],
  keywords=['pip', 'packaging', 'python'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)