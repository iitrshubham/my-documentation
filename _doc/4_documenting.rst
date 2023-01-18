Sphinx Documentation
^^^^^^^^^^^^^^^^^^^^

This directory contains the documentation for the package. This will be automatically generated from python files through Sphinx documentation tool.


What is Sphinx?
===============

Well, As mentioned earlier, It is a python project documentation tool. It reads the docstrings in python code and converts  them in to easily readable html format. Sphinx is also capable of converting the documentation into LaTeX format(PDF). The underlaying file format in this documentation is reStructuredText (RST) format, which is a markup language. It is necessary to write proper sphinx-readable docstrings to generate better documentation. See the files in  **_src** directory for standard docstring format.

reStructuredText:
-----------------

It is generally uses for textual data in the python documentation. It has it own syntax to define headings, subheadings, bold and italic letters, weblinks, and code blocks. This syntax will be read by sphinx engine and it regenerates beautiful web documents. 

It is important to follow correct syntax, indentation, and space between the commands in rst files and docstrings. There are few .rst files in this directory so please feel free to have a glance at the syntax. After making the web documentation out of this files, you will understand how to use them for your own projects.

Documentation:
==============

* Since the current projects has already dedicated this folder(_doc) for the documentation, open command prompt and change working directory to _doc folder. 

* ``sphinx-quickstart`` use this command to start the documentation.

* Provide information such as ``project name``, ``author name``, and ``release version``. For the remaining details, continue with default options by pressing **Enter** button.

* It is observed that ``Linux`` user have more details to add. Apart from above mentions options, procced with the default options for all the information.

* Successful execution of the commands creates few file and folder in **_doc** directory. 

* Now, we have to modify **conf.py** file according to the our project file structure. 

* Open **conf.py**

  * Uncomment the lines 13th-15th (for windows users) and replace the line ``sys.path.insert(0, os.path.abspath('.'))`` with command ``sys.path.insert(0, os.path.abspath('../_src'))``. 
  * In **extension list** add ``'sphinx.ext.autodoc'``. ( at line no. 33 for windows users.).
  * Also, change **html theme** from ``'alabaster'`` to ``'sphinx_rtd_theme'`` (line no. 50, again, in windows).

* Lets go back to the command prompt.  Use  ``sphinx-apidoc -o . ../_src`` to generate *.rst* for source code available in **_src** folder. This command reads the *.py* files in **_src** directory and creates relevant *.rst* files in current working directory.

* Above command creates multiple *.rst* file along with **index.rst** and **modules.rst**

* **index.rst** file defines the contents of developed web-page. we have to add few details to this file so open **index.rst**  and update the file with below content.

.. code-block:: rst
    :linenos:

    Project_name Documentation
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
    Write Project description here.
  
    This documentation is organized into a couple sections:
  
    * :ref:`intro`
    * :ref:`install`
    * :ref:`modules`
  
    .. _intro:
  
    .. toctree::
       :maxdepth: 2
       :caption: Introduction:
  
       1_introduction
       4_documenting
       2_contact
      
     
    .. _install:
  
    .. toctree::
       :maxdepth: 2
       :caption: Installation:
  
       3_install
  
    .. _modules:
  
    .. toctree::
       :maxdepth: 2
       :caption: Modules:  
  
       modules
  
    Indices and tables
    ==================
  
    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`


* Please don't mind this syntax. You get complete idea of it, after generating the final web documentation.

Generating HTML files in local directory
========================================

* This process generates the html files in **_build/html** directory. These HTML files are capable of generating website locally.

* In command prompt use command, ``make html`` . This creates multiple html files in **_build/html** directory if the docstrings and *.rst* file are in correct format. Otherwise, it returns error in command prompt.

* After executing all the commands correctly, Open **index.html** in *_build/html* directory to see the project documentation.

* These files are not necessary to make online available website. Sphinx's has an other way to generate online website of the project so It is  better to add **_build** directory to *gitignore* list. 

Publishing the website
======================

* After making all the necessary modifications to the *.rst* files. We can commit and push all the generated files to GitHub. To publish the projects *.rst* as website, please create an account in `Read the docs web <https://readthedocs.org/>`, if you haven't have one already. 

* Log-in to the website and direct to `rtd_projects <https://readthedocs.org/dashboard/>`_ then ``Import a project`` > ``Import manually``. 

* Provide the information like Name, Repository URL, Repository type, and default branch.

* You can check or uncheck the advanced options box. If have checked it, press ``next`` and provide necessary information and press ``finish``. if haven't checked the advanced options box, pressing ``next`` directs to final page. In this page, press ``Build version`` to build the project website. It takes a moment to complete and generate website link as ``view doc`` in the same page.

* There you go!! By pressing ``view doc`` we can see the beautiful web page of the project.

* Any changes that are being made to *.rst* and docstring in *.py* files will reflect in website only after rebuilding in `rtd_projects <https://readthedocs.org/dashboard/>`_.

Final notes:
============

The above mentioned procedure is best suitable for the file structure of this project. To develop the documentation of different type of file structure, few modifications need to be added to **conf.py** and **index.rst**  based on the respective file structure. 

To learn reStructuredText formatting, read the *.rst* files in projects like NURBS-Pytohn, 

Existing file description:
==========================

* ``1_introduction.rst`` :  contains the information of the project
* ``2_contact.rst``: Contact information of contributors.
* ``3_install.rst`` : Package installation procedure. 
* ``3_documenting`` : Documentation procedure.

Resources
^^^^^^^^^

* `Read the docs <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/>`__
* `Sphinx <Sphinx documentation>`__
* `reStructuredText formatting <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`__
* `reStructuredText formatting <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__