import sys
import os

plugindir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(plugindir)
sys.path.append(os.path.join(plugindir, "lib"))
sys.path.append(os.path.join(plugindir, "plugin"))

from plugin.main import {{cookiecutter.__plugin_snake}}

if __name__ == "__main__":
    {{cookiecutter.__plugin_snake}}()