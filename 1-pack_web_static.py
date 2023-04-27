#!/usr/bin/python3

"""Fabric script to generate a .tgz archive of web_static."""

from fabric.api import local
from datetime import datetime


def do_pack():

    """Create a .tgz archive from the contents of web_static folder."""

    m_date = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_path = "versions/web_static_{}.tgz".format(m_date)
    try:
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(file_path))
        return file_path
    except:
        return none
