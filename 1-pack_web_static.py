#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    generates a .tgz archive
    from the contents of the web_static
    folder of your AirBnB Clone repo
    """
    if not os.path.exists('versions'):
        os.makedirs('versions')

    # Create the name of the archive file based on current timestamp
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    # Create the .tgz archive using tar command
    result = local("tar -cvzf {} web_static".format(archive_path))

    # Check if tar command was successful
    if result.failed:
        return None
    else:
        return archive_path
