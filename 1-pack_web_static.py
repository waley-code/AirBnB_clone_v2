#!/usr/bin/python3
"""Creates a .tgz archive compressing its contents web_static folder."""
from fabric.api import local
import time


def do_pack():
    """Creates a .tgz archive compressing its contents web_static folder"""
    try:
        local("mkdir -p versions")
        strap_time = time.strftime("%Y%m%d%H%M%S")
        p_name = f"web_static_{strap_time}.tgz"
        tar_cmd = f"tar -cvzf versions/{p_name} web_static"
        local(tar_cmd)
        return "versions/{}".format(p_name)
    except:
        return None