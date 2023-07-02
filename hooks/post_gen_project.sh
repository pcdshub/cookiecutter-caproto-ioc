#!/bin/bash
{% if cookiecutter.auto_gitlab_setup == "yes" %}
git init
git add -A
git remote add {{ cookiecutter.git_remote_name }} git@git.aps.anl.gov:{{ cookiecutter.gitlab_repo_group }}/{{ cookiecutter.repo_name }}.git
{% endif %}
