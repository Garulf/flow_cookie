#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import uuid
import json

PLUGIN_FILE = "plugin.json"
PLUGIN_PATH = os.path.join(os.getcwd(), PLUGIN_FILE)

def read_manifest():
    with open(PLUGIN_PATH, "r") as f:
        return json.load(f)
    
def write_manifest(content):
    with open(PLUGIN_PATH, "w") as f:
        json.dump(content, f, indent=4)
    return content

def run_cmd(cmd):
    process = subprocess.Popen(cmd)
    process.wait()

def clone_repo(repo, dir):
    
    path = os.path.join(os.getcwd(), *dir)
    cmd = ["git", "clone", repo, path]

    run_cmd(cmd)

def generate_uuid():
    return str(uuid.uuid4()).replace('-', '').upper()

def add_uuid(plugin_manifest):
    plugin_manifest['ID'] = generate_uuid()
    write_manifest(plugin_manifest)
    # print(f"Changed version to: {plugin['Version']}")
    
def update_description(desc):
    with open(os.path.join(os.getcwd(), ".git", "description"), "w") as f:
        f.write(desc)

if __name__ == "__main__":
    plugin_manifest = read_manifest()
    clone_repo("https://github.com/Garulf/flow_commands", ["bin"])

    clone_repo("https://github.com/Garulf/flow_workflows", [".github", "workflows"])

    add_uuid(plugin_manifest)

    run_cmd(["pip", "install", "--target=./lib", "-r", "requirements.txt"])

    run_cmd(["git", "init"])
         
    update_description(plugin_manifest["Description"])
         

