#!/usr/bin/python3
"""Creates a comperessed_static folder"""
import os
from datetime import datetime
from fabric.api import local, run, put, env
env.hosts = ['54.174.243.255', '54.208.245.251']

# Creates a comperessed_static folder
def do_pack():
    """Creates a comperessed_static folder
    """
    local("mkdir -p versions")
    strap_time = datetime.now().strftime("%Y%m%d%H%M%S")
    p_name = f"web_static_{strap_time}.tgz"
    tar_cmd = f"tar -cvzf versions/{p_name}. web_static"
    response = local(tar_cmd)
    if response.failed:
        return None
    else:
        return "versions/{}".format(p_name)


# distributes an archive to web servers
def do_deploy(archive_path):
    """ that distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1]
        file_name_no_ext = file_name.split(".")[0]
        run("sudo mkdir -p /data/web_static/releases/{}/".format(file_name_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, file_name_no_ext))

        run("rm /tmp/{}".format(file_name))

        run("rm -rf /data/web_static/current")

        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name_no_ext))

        return True
    except:
        return False
