**Attention: This is still an early version just for testing, do not use it in production yet.**

# Dwork

Dwork is a Python toolkit for anonymous data science & analytics. It leverages modern privacy concepts like differential privacy (DP) to anonymize sensitive and personal data on the fly while making it (hopefully) easy to work with this data. Dwork can be freely used, it is released under the BSD-3 license.

## Installing

You can install the latest Dwork version using pip:

    pip install dwork

Alternatively, you can download this repository and install Dwork directly from the main directory of the repository:

    pip install .

## Examples

To learn more about how to use Dwork for anonymous data science, please have a look at the `examples` directory.

# Information For Developers

If you want to work on Dwork itself, you can install the package in development mode, which will not copy files but instead link them to your virtual environment so that you can edit them and see changes immediately:

    pip install -e .

If you want to run tests, please also install test dependencies and a virtual environment:

    make setup

The following sections are only relevant for developers of Dwork, if you are a user you can disregard them.

## Running tests

Dwork comes with automated code formatting via black, static type analysis via mypy and testing via py.test / unittest. You can run all of the above with a single make command:

    make

To only run tests, simply run

    make test

You can also pass arguments to py.test via the `testargs` parameter:

    make test testargs="-x -k TestDatapoints"

## Upgrading packages

You can use the fabulous `pur` tool to upgrade packages in the requirements files:

    # will update normal requirements
    pur -v -r requirements.txt
    # will update test requirements
    pur -v -r requirements-test.txt

## Building Wheels

We install all packages from local wheels if possible (for security reasons), to generate these wheels simply use the following commands:

    pip wheel --wheel-dir wheels -r requirements.txt
    pip wheel --wheel-dir wheels -r requirements-test.txt

## Making a New Release

To release a new version of Dwork, follow these steps:

* Make sure all tests pass for the new release.
* Update `setup.py` with the new version number. We follow the
  [semantic versioning](https://semver.org/) standard for our version
  numbers.
* Add a changelog entry in the `README.md`.
* Commit the updated `setup.py` and `README.md` files to the repository.
* Create a new tag with the version number (which is required for CI integration):

      git tag -a v0.1.4 -m "v0.1.4"
* Push the tag to the main repository together with the commit

      git push origin master --tags
* Gitlab/Travis will pick up the version tag and make the release for us.
* Alternatively, you can create the distribution packages using `setup.py`:

      python setup.py sdist bdist_wheel
* You can also manually publish the packages to PyPi via Twine (not recommended):
  
      twine upload dist/*
