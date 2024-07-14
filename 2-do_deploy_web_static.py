#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import *
import os
from fabric.contrib.files import exists


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
        release_path = '/data/web_static/releases/{}'.format(archive_name_no_ext)
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
