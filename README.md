# Docker registry tools (a.k.a. "DoctoR Tools")

This is a collection of [docker-registry](https://github.com/dotcloud/docker-registry/) helper tools, meant to ease the development, test and maintainance of backend drivers and other docker-registry related code.

[![PyPI version][pypi-image]][pypi-url]
[![Build Status][travis-image]][travis-url]
[![Coverage Status][coveralls-image]][coveralls-url]

## Installation

`pip install docker-python-dev`

You may then alias `docker-python-dev` in your .bashrc / .zshrc / .profile (say, as `alias drt=docker-python-dev`).

## Usage

If you want to create a new storage driver for docker-registry:

`drt driver --new`

If you want to run sanity checks on an existing driver

`drt driver --audit`

## License

This is licensed under the Apache license.

[pypi-url]: https://pypi.python.org/pypi/docker-python-dev
[pypi-image]: https://badge.fury.io/py/docker-python-dev.svg

[travis-url]: http://travis-ci.org/dmp42/docker-python-dev
[travis-image]: https://secure.travis-ci.org/dmp42/docker-python-dev.png?branch=master

[coveralls-url]: https://coveralls.io/r/dmp42/docker-python-dev
[coveralls-image]: https://coveralls.io/repos/dmp42/docker-python-dev/badge.png?branch=master

