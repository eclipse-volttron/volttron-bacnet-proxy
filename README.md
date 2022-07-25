# volttron-bacnet-proxy

![Passing?](https://github.com/VOLTTRON/volttron-bacnet-proxy/actions/workflows/run_tests.yml/badge.svg)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://VOLTTRON.github.io/volttron-bacnet-proxy/)
[![pypi version](https://img.shields.io/pypi/v/volttron-bacnet-proxy.svg)](https://pypi.org/project/volttron-bacnet-proxy/)


# BACnet Proxy Agent

Communication with a BACnet device on a network happens via a single virtual BACnet device. In VOLTTRON driver framework,
we use a separate agent specifically for communicating with BACnet devices and managing the virtual BACnet device.

## Agent Configuration

```
    {
        "device_address": "10.0.2.15",
        "max_apdu_length": 1024,
        "object_id": 599,
        "object_name": "Volttron BACnet driver",
        "vendor_id": 15,
        "segmentation_supported": "segmentedBoth"
    }
```
1. device_address - Address bound to the network port over which BACnet communication will happen on the computer
running VOLTTRON. This is NOT the address of any target device.
2. object_id - ID of the Device object of the virtual BACnet device. Defaults to 599. Only needs to be changed if there
is a conflicting BACnet device ID on your network.
3. max_apdu_length - Maximum size message the device can handle
4. object_name - Name of the object. Defaults to “Volttron BACnet driver”. (Optional)
5. vendor_id - Vendor ID of the virtual BACnet device. Defaults to 15. (Optional)
6. segmentation_supported -  Segmentation allows larger messages to be broken up into segments and spliced back together.
Possible setting are “segmentedBoth” (default), “segmentedTransmit”, “segmentedReceive”, or “noSegmentation” (Optional)


## Prerequisites

* Python 3.8
* Poetry

### Python
volttron-bacnet-proxy requires Python 3.8 or above.


To install Python 3.8, we recommend using [pyenv](https://github.com/pyenv/pyenv).

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv ~/.pyenv

# setup pyenv (you should also put these three lines in .bashrc or similar)
export PATH="${HOME}/.pyenv/bin:${PATH}"
export PYENV_ROOT="${HOME}/.pyenv"
eval "$(pyenv init -)"

# install Python 3.8
pyenv install 3.8.10

# make it available globally
pyenv global system 3.8.10
```

### Poetry

This project uses `poetry` to install and manage dependencies. To install poetry,
follow these [instructions](https://python-poetry.org/docs/master/#installation).



## Installation and Virtual Environment Setup

Set the environment to be in your project directory:

```poetry config virtualenvs.in-project true```

If you want to install all your dependencies, including dependencies to help with developing your agent, run this command:

```poetry install```

If you want to install only the dependencies needed to run your agent, run this command:

```poetry install --no-dev```

Activate the virtual environment:

```poetry shell```


## Git Setup

1. To use git to manage version control, create a new git repository in your local agent project.

```
git init
```

2. Then create a new repo in your Github or Gitlab account. Copy the URL that points to that new repo in
your Github or Gitlab account. This will be known as our 'remote'.

3. Add the remote (i.e. the new repo URL from your Github or Gitlab account) to your local repository. Run the following command:

```git remote add origin <my github/gitlab URL>```

When you push to your repo, note that the default branch is called 'main'.

## Publishing to PyPi

Publishing your Agent module to PyPi is automated through the continuous integration workflow provided in `~/.github/workflows/publish_to_pypi.yml`.
You can update that Github Workflow with your credentials to ensure that publishing to PyPi will succeed. The default behavior of
that workflow is to publish to PyPi when a release has been published. If you want to change this behavior, you can modify the
workflow to publish to PyPi based on whatever desired event; see [Github Workflows docs](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow)
on how to change the events that trigger a workflow.

## Optional Configurations

### Precommit

Install pre-commit hooks:

```pre-commit install```

To run pre-commit on all your files, run this command:

```pre-commit run --all-files```

If you have precommit installed and you want to ignore running the commit hooks
every time you run a commit, include the `--no-verify` flag in your commit. The following
is an example:

```git commit -m "Some message" --no-verify```

# Documentation

To build the docs, navigate to the 'docs' directory and build the documentation:

```shell
cd docs
make html
```

After the documentation is built, view the documentation in html form in your browser.
The html files will be located in `~<path to agent project directory>/docs/build/html`.

**PROTIP: To open the landing page of your documentation directly from the command line, run the following command:**

```shell
open <path to agent project directory>/docs/build/html/index.html
```

This will open the documentation landing page in your default browsert (e.g. Chrome, Firefox).
