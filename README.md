# plant


### Simplified Package Management for Python

Plant is a simplified package manager for your Python projects.

Programmers have routinely complained about `pip` not being as elegant as
`npm` when it comes to installing dependencies. For example, with `pip`, one
has to always specify a `requirements.txt` file for installing the packages
needed for a project. This is an inconvenience, especially when compared to
`npm`, which has an elegant command `npm install` to install all the
dependencies mentioned in the project's `package.json` by default.

With `plant`, Python programmers, especially the lazy ones (i.e. the good
ones) don't have to face this inconvenience. This packages boils all of the
hassle down to `$ pip-plant`, which simply installs all the dependencies
mentioned in your project's `requirements.txt`.


## Usage

    $ pip-plant
    Requirements detected!
    Found 10 dependencies. Please wait, Installing!
    Installed!!

That's basically it.

## Installation

    $ pip install pip-plant


This isn't the only problem `plant` solves. More features coming soon include
automatic requirements file updation, dependency stats (i.e. dependency usage
proportions measurement in your project) and much more!
