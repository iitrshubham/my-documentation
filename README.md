# documentation
This project is intended to demonstrate the standard python project work-flow that is being followed at [Computational Mechanics lab](https://computationalmechanics.in/). By presenting the basic folder structure, this project focuses of documentation of the project and source code. These documentations makes a coding packages easy accessible and collaborative. Sphinx documentation tool is used to generate web version of the project.

To demonstrate the entire workflow, this projects considered simple maths.py file containing two classes that stores two numbers and performs addition, subtraction, multiplication, and division operations on them. The presented python code is containing properly formatted docstrings, which are mandatory for better documentations.

Before starting, look a few open source projects documentation that generated using Sphinx and familiarize yourself with what we are going to finally make.

* [NURBS Python](https://nurbs-python.readthedocs.io/en/5.x/)
* [HDF5 for Python](https://docs.h5py.org/en/stable/)
* [SimPy](https://simpy.readthedocs.io/en/latest/)
* [Conda](https://conda.io/en/latest/)

 ## Getting Started & Prerequisites

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

To follow along with the examples, you need to download and install below packages into your system. 

*Note: If have installed updated versions of below packages, please ignore the following steps.*

* [Anaconda](https://www.anaconda.com/), A python distributor.
* [GitHub](https://desktop.github.com/), A code management tool between local remote repositories.
* [Sublime](https://www.sublimetext.com/), A code editing tool.
* [Mark Text](https://marktext.app/), A markdown editor.

#### Anaconda Installation

After downloading the Anaconda, follow [Anaconda Install](https://docs.anaconda.com/anaconda/install/) instruction based on your system configuration. 

**Important: While installing the anaconda, make sure below boxes are checked.**

![Anaconda](https://user-images.githubusercontent.com/33441778/161914017-3b8b8a4b-79be-4cfc-aa12-bb36811cc2b1.png)


#### Sphinx Installation

Open command prompt as administrator and use below command to install sphinx in your machine.

```
pip install -U sphinx
```

*Note: If you are not able to execute above command through command prompt, open **anaconda prompt** as administrator to execute the commands.*

`sphinx-build --version` Use this command to check sphinx version.

Sphinx offers flexibility in changing the webpage format.  *read_docs*  is the most popular theme. In order to install it use this command  

```pip install sphinx_rtd_theme```

So far, we installed all the required modules that necessary to develop documentation. Please refer to _doc/README.md for documentation process using Sphinx.

#### GitHub

After downloading the GitHub desktop into your system, install it with default options and link your GitHub account to it. If you don not have GitHub account, create one on [GitHub](https://github.com/) Publishing the online version of documentation is possible only through version control systems like GitHub. Please acquire basic working knowledge of git. 

#### Sublime

Sublime is one of the  light weight text/code editors. Install it with default options.

#### Mark Text

Mark down is a text formatting language, which is being widely in online articles. Mark Text is a mark down editor. This renders the text beautifully according to corresponding markdown format while typing it. Install it with default options.

## Note:

After installing all the prerequisite tools, visit `_doc/README.md` for project documentation instructions. 

## Folder Structure


```bash
.
├── _data
├── _demo
├── _doc
├── _docker
├── _flats
├── _src
├── _scripts
├── _test
└── setup.py
```



An overview of what each of these does:

| File/Directory | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| `_data`        | This directory contains the data that will be used for test scripts. These will be mesh files created in gmsh |
| `_demo`        | This directory will contain the demos supplied with the package |
| `_doc`         | This directory will contain the documentation for the package. This will be automatically generated from python files |
| `_docker`      | This directory will contain the DockerFile to build the docker image for this project |
| `_flats`       | This directory will contain the flat programs based on which modules will be developed |
| `_src`         | `This is the main directory for the source code of the package |
| `_scripts`     | This directory will contain scripts to generate documentation |
| `_test`        | This directory will contain the unit tests                   |
| `setup.py`     | This file will help to install the package with `pip`        |


## Authors
- [Abhinav Gupta](abhigupta.io)
- [Bhagath Mamindlapelly](https://github.com/bhagath555)
