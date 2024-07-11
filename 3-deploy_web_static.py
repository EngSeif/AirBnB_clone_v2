#!/usr/bin/python3
"""
distributes an archive to your web servers,
"""

from fabric.api import env, local, sudo, put, cd
import os
from datetime import datetime
from fabric.contrib.files import exists

env.hosts = ['18.207.1.248', '100.25.194.205']
env.user = 'ubuntu'

def do_deploy(archive_path):
    '''Deploy archive to web server'''
    if not archive_path:
        return False

    if not os.path.exists(archive_path):
        print('Archive path does not exist:', archive_path)
        return False

    file_name = os.path.basename(archive_path)
    file_name_no_ext = os.path.splitext(file_name)[0]
    target_path = '/data/web_static/releases/{}'.format(file_name_no_ext)

    # Upload the archive to the remote server
    put(archive_path, '/tmp/', use_sudo=True)

    # Create the target directory
    if not exists(target_path):
        sudo('mkdir -p {}'.format(target_path))

    # Extract the archive into the target directory
    with cd(target_path):
        sudo('tar -xzf /tmp/{} -C {}'.format(file_name, target_path))

    # Remove the uploaded archive from the remote server
    sudo('rm /tmp/{}'.format(file_name))

    # Move the contents of the extracted archive to the target directory
    sudo('mv {}/web_static/* {}/'.format(target_path, target_path))

    # Remove the web_static directory from the target directory
    sudo('rm -rf {}/web_static'.format(target_path))

    # Remove the current symlink if it exists
    sudo('rm -rf /data/web_static/current')

    # Create a new symlink to the latest release
    sudo('ln -s {} /data/web_static/current'.format(target_path))

    print('New version deployed!')
    return True

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