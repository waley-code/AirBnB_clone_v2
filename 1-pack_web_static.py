#!/usr/bin/python3
"""Creates a .tgz archive compressing web_static folder"""
# Import Fabric's API module
from datetime import datetime
from fabric.api import local


# Creates a comperessed_static folder
def do_pack():
    """Creates a .tgz archive compressing web_static folder"""
    
    local("mkdir -p versions")
    strap_time = datetime.now().strftime("%Y%m%d%H%M%S")
    p_name = f"web_static_{strap_time}.tgz"
    tar_cmd = f"tar -cvzf versions/{p_name} web_static"
    response = local(tar_cmd)
    if response.failed:
        return None
    else:
        return "versions/{}".format(p_name)
