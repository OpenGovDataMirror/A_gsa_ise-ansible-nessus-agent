# -*- coding: utf-8 -*-

import os
import json

dir_tests = os.path.dirname(os.path.abspath(__file__))
dir_project_root = os.path.dirname(dir_tests)
path_vars_secrets_json_file = os.path.join(dir_tests, "vars-secrets.json")
path_vars_json_file = os.path.join(dir_tests, "vars.json")

with open(path_vars_secrets_json_file, "rb") as f:
    vars_secrets = json.loads(f.read().decode("utf-8"))

vars = {
    "role_dir": dir_project_root,
}
vars.update(vars_secrets)

with open(path_vars_json_file, "wb") as f:
    f.write(json.dumps(vars).encode("utf-8"))
