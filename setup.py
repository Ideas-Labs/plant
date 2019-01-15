"""
pip-plant installs your dependencies.
"""

from distutils.core import setup

setup(
  name = 'pip-plant',
  packages = ['plant'],
  version = '0.1',
  license='MIT',
  description = 'Plant simplifies Python package management for your projects.',
  author = 'Ideas Labs',
  author_email = 'saurabh.chaturvedi63@gmail.com',
  url = 'https://github.com/Ideas-Labs/plant',
  scripts=['plant/pip-plant'],
  install_requires=[
    'envoy',
    ],
  # download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['pip', 'packaging', 'python'],
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