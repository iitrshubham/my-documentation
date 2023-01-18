Introduction
^^^^^^^^^^^^^

This project is intended to demonstrate the standard python project work-flow that is being followed at `Computational Mechanics lab <https://computationalmechanics.in/>`_. By presenting the basic folder structure, this project focuses of documentation of source code for easy collaborations. to presenting in a website through Sphinx documentation tool.

To demonstrate the entire workflow, this projects considered simple maths.py file containing two classes that stores two numbers and performs addition, subtraction, multiplication, and division operations on them. The python code presented is containing properly formatted docstrings, which is mandatory for better representation in final document.

Before starting, look a few open source projects documentation that generated using Sphinx and familiarize yourself with what we are going to finally make.

* `NURBS Python <https://nurbs-python.readthedocs.io/en/5.x/>`_
* `HDF5 for Python <https://docs.h5py.org/en/stable/>`_
* `SimPy <https://simpy.readthedocs.io/en/latest/>`_
* `Conda <https://conda.io/en/latest/>`_

Prerequisites
=============
To follow along with the examples, you need to install below packages into your system. 

*Note: If have installed updated versions of below packages, please ignore the following steps.*

* `Anaconda <https://www.anaconda.com/>`_, A python distributor
* `GitHub <https://desktop.github.com/>`__, A code management tool between local remote repositories.
* `Sublime <https://www.sublimetext.com/>`_, A code editing tool.
* `Mark Text <https://marktext.app/>`_, A markdown editor.


Anaconda Installation
---------------------

After downloading the Anaconda, follow `Anaconda Install <https://docs.anaconda.com/anaconda/install/>`_ instruction based on your system configuration. 

**Important:** *While installing the anaconda, make sure below boxes are checked.*

.. image:: https://user-images.githubusercontent.com/33441778/161914017-3b8b8a4b-79be-4cfc-aa12-bb36811cc2b1.png
    :width: 400

Sphinx Installation
-------------------

Open command prompt as administrator and use below command to install sphinx in your machine.

.. code-block:: console

    pip install -U sphinx


**Note:** *If you are not able to execute above command through command prompt, open anaconda prompt as administrator to execute the commands.*

``sphinx-build --version`` Use this command to check sphinx version.

Sphinx offers flexibility in changing the webpage format.  **read_docs**  is the most popular theme. In order to install it use this command  

.. code-block:: console

    pip install sphinx_rtd_theme

GitHub
-------

After downloading the GitHub desktop into your system, install it with default options and link your GitHub account to it. If you don not have GitHub account, create one on `GitHub <https://github.com/>`__ Publishing the online version of documentation is possible only through version control systems like GitHub. Please acquire basic working knowledge of git. 

Sublime
--------

Sublime is one of the  light weight text/code editors. Install it with default options.

Mark Text
----------

Mark down is a text formatting language, which is being widely in online articles. Mark Text is a mark down editor. This renders the text beautifully according to corresponding markdown format while typing it. Install it with default options.


So far, we installed all the required modules that necessary to develop documentation. Please refer to ``Sphinx Documentation`` section.

