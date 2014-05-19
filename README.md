# Docker registry tools (a.k.a. "DoctoR Tools")

This is a collection of [docker-registry](https://github.com/dotcloud/docker-registry/) helper tools, meant to ease the development, test and maintainance of backend drivers and other docker-registry related code.

[![PyPI version][pypi-image]][pypi-url]
[![Build Status][travis-image]][travis-url]

## Installation

`pip install docker-registry-tools`

You may then alias `docker-registry-tools` in your .bashrc / .zshrc / .profile (say, as `alias drt=docker-registry-tools`).

## Usage

If you want to create a new storage driver for docker-registry:

`drt driver --new`

If you want to run sanity checks on an existing driver

`drt driver --audit`

## License

This is licensed under the Apache license.

[pypi-url]: https://pypi.python.org/pypi/docker-registry-tools
[pypi-image]: https://badge.fury.io/py/docker-registry-tools.svg

[travis-url]: http://travis-ci.org/dmp42/docker-registry-tools
[travis-image]: https://secure.travis-ci.org/dmp42/docker-registry-tools.png?branch=master



