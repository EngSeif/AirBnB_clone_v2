#!/usr/bin/python3
"""
distributes an archive to your web servers,
"""

from fabric.api import env, put, run, sudo
import os

env.hosts = ['18.207.1.248', '100.25.194.205']

def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    try:
        if not os.path.exists(archive_path):
            return False
        filename = os.path.basename(archive_path)
        folder_name = filename.replace('.tgz', '').split('_')[2]
        release_path = '/data/web_static/releases/{}/'.format(folder_name)
        sudo('mkdir -p {}'.format(release_path))
        sudo('tar -xzf /tmp/{} -C {}'.format(filename, release_path))
        sudo('rm /tmp/{}'.format(filename))
        sudo('mv {}web_static/* {}'.format(release_path, release_path))
        sudo('rm -rf {}web_static'.format(release_path))
        current_link = '/data/web_static/current'
        if sudo('test -d {}'.format(current_link)).failed:
            sudo('rm {}'.format(current_link))
        sudo('ln -s {} {}'.format(release_path, current_link))
        return True
    except Exception as e:
        return False   
