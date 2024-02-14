===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://img.shields.io/travis/{{ cookiecutter.gitlab_repo_group }}/{{ cookiecutter.repo_name }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.gitlab_repo_group }}/{{ cookiecutter.repo_name }}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}


{{ cookiecutter.description }}

Documentation
-------------

Sphinx-generated documentation for this project can be found here:
https://{{ cookiecutter.gitlab_repo_group }}.github.io/{{ cookiecutter.repo_name}}/

Requirements
------------

Describe the project requirements (i.e. Python version, packages and how to install them)

Installation
------------

The following will download the IOC, and configure it for management using systemd.

.. code-block:: bash

    git clone https://github.com/{{ cookiecutter.gitlab_repo_group }}/{{ cookiecutter.repo_name }}
    pip install -e {{ cookiecutter.repo_name }}
    ln -s `pwd`/{{ cookiecutter.repo_name }}/{{ cookiecutter.systemd_service }}.service ~/.config/systemd/user/
    systemctl --user daemon-reload

Starting the IOC (Testing)
--------------------------

This command will run the IOC in the current shell, useful for testing and debugging.

.. code-block:: bash

    start_{{ cookiecutter.import_name }} --list-pvs


Controlling the IOC (Production)
--------------------------------

Running the IOC locally is useful for testing, but cumbersome in practice.

An easier choice is to let systemd control the IOC:

- Start: ``systemctl --user start {{ cookiecutter.systemd_service }}``
- Stop: ``systemctl --user stop {{ cookiecutter.systemd_service }}``
- Restart: ``systemctl --user restart {{ cookiecutter.systemd_service }}``
- Status: ``systemctl --user status {{ cookiecutter.systemd_service }}``
- View log: ``journalctl -xef --user-unit {{ cookiecutter.systemd_service }}``

Running the Tests
-----------------
::

  $ pip install -e .
  $ pytest -vv
