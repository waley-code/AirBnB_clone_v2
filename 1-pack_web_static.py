#!/usr/bin/python3
"""Creates an archive compressing web_static folder
        Returns:
            returns none if the file wasn't created and the created
            archive path if true
    """

from datetime import datetime
from fabric.api import local


def do_pack():
    """Creates an archive compressing web_static folder
        Returns:
            returns none if the file wasn't created and the created
            archive path if true
    """

    local("mkdir -p versions")
    strap_time = datetime.now().strftime("%Y%m%d%H%M%S")
    p_name = f"web_static_{strap_time}.tgz"
    tar_cmd = f"tar -cvzf versions/{p_name} web_static"
    response = local(tar_cmd)
    if response.failed:
        return None
    else:
        return "versions/{}".format(p_name)
