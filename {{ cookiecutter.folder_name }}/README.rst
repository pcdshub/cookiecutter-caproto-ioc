===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_repo_group }}/{{ cookiecutter.repo_name }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_repo_group }}/{{ cookiecutter.repo_name }}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}


{{ cookiecutter.description }}

Documentation
-------------

Sphinx-generated documentation for this project can be found here:
https://{{ cookiecutter.github_repo_group }}.github.io/{{ cookiecutter.repo_name}}/

Requirements
------------

Describe the project requirements (i.e. Python version, packages and how to install them)

Installation
------------

..

    pip install git+https://github.com/{{ cookiecutter.github_repo_group }}/{{ cookiecutter.repo_name }}


Running the Tests
-----------------
::

  $ pip install -r dev-requirements.txt
  $ pytest -vv
