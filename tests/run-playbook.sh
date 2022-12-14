#!/bin/bash

dir_here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
dir_repo_root="$( dirname ${dir_here} )"
path_prepare_vars_python_script="${dir_here}/prepare_vars.py"

python ${path_prepare_vars_python_script}
ansible-playbook ${dir_here}/playbook.yml --extra-vars "@${dir_here}/vars.json"
