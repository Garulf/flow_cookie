#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import uuid
import json

def run_cmd(cmd):
    process = subprocess.Popen(cmd)
    process.wait()

def clone_repo(repo, dir):
    
    path = os.path.join(os.getcwd(), *dir)
    cmd = ["git", "clone", repo, path]

    run_cmd(cmd)

def generate_uuid():
    return str(uuid.uuid4()).replace('-', '').upper()

def add_uuid():
    path = os.path.join(os.getcwd(), "plugin.json")
    with open(path, 'r') as f:
        plugin = json.load(f)
    plugin['ID'] = generate_uuid()
    with open(path, 'w') as f:
        f.write(json.dumps(plugin, indent=4))
    # print(f"Changed version to: {plugin['Version']}")

clone_repo("https://github.com/Garulf/flow_commands", ["bin"])

clone_repo("https://github.com/Garulf/flow_workflows", [".github", "workflows"])

add_uuid()

run_cmd(["pip", "install", "--target=./lib", "-r", "requirements.txt"])

run_cmd(["git", "init])
