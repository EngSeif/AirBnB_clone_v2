#!/usr/bin/python3
"""
distributes an archive to your web servers,
"""

from fabric.api import env, local, sudo, put
import os
from datetime import datetime

env.hosts = ['18.207.1.248', '100.25.194.205']

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers and deploys it
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<archive filename without extension>
        filename = os.path.basename(archive_path)
        folder_name = filename.replace('.tgz', '').split('_')[2]  # Extracting folder name
        release_path = '/data/web_static/releases/{}/'.format(folder_name)
        sudo('mkdir -p {}'.format(release_path))
        sudo('tar -xzf /tmp/{} -C {}'.format(filename, release_path))
        sudo('rm /tmp/{}'.format(filename))

        # Move contents to a new folder without version number
        sudo('mv {}web_static/* {}'.format(release_path, release_path))
        sudo('rm -rf {}web_static'.format(release_path))

        # Delete the symbolic link /data/web_static/current if exists
        current_link = '/data/web_static/current'
        if sudo('test -d {}'.format(current_link)).failed:
            sudo('rm {}'.format(current_link))

        # Create a new symbolic link /data/web_static/current
        sudo('ln -s {} {}'.format(release_path, current_link))
        print("New version deployed!")

        return True

    except Exception as e:
        print(e)
        return False

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

def deploy():
    """
    creates and distributes an archive to your web servers 
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)