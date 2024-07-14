#!/usr/bin/python3
"""
distributes an archive to your web servers,
"""

from fabric.api import env, local, sudo, put
import os
from datetime import datetime

env.hosts = ['18.207.1.248', '100.25.194.205']
env.user = 'ubuntu'


def do_deploy(archive_path):
    '''Deploy archive to web server'''
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, '/tmp/')
        archive_filename = archive_path.split('/')[-1]
        archive_name_no_ext = archive_filename.split('.')[0]
        release_path = '/data/web_static/releases/{}'.format(
            archive_name_no_ext
            )
        sudo('mkdir -p {}'.format(release_path))
        sudo('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))
        sudo('rm /tmp/{}'.format(archive_filename))
        sudo('mv {}/web_static/* {}/'.format(release_path, release_path))
        sudo('rm -rf {}/web_static'.format(release_path))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {} /data/web_static/current'.format(release_path))
        print("New version deployed!")
        return True
    except Exception as e:
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
    if os.path.exists(archive_path) is False:
        return False

    result = do_deploy(archive_path)
    return result
