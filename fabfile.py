#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Kun Jia
# date: 05/02/17
# email: me@jarrekk.com
from __future__ import unicode_literals

from fabric.api import run, roles, cd, local
from fabric.context_managers import env
from fabric.contrib.project import rsync_project

code_dir = '/jalpc'
html_dir = '/usr/share/nginx/html'
exclude = ('.DS_Store', '*pyc', '.git', '.idea', '*sqlite3', 'migrations', 'node_modules', 'readme_files')

env.roledefs = {
    'vps': ['root@vps.jarrekk.com']
}


@roles('vps')
def front():
    local('cd ./ztool-frontend && npm install ; npm run build ; cd -')
    rsync_project(local_dir='./ztool-frontend/', remote_dir=''.join(code_dir, '/ztool-frontend'), exclude=exclude)


@roles('vps')
def flask():
    rsync_project(local_dir='./ztool-backhend-mongo/', remote_dir=''.join([code_dir, '/ztool-backhend-mongo']), exclude=exclude)
    with cd(code_dir):
        run('docker-compose restart flask')

@roles('vps')
def rebuild():
    local('cd ztool-frontend && npm install ; npm run build ; cd -')
    rsync_project(local_dir='.', remote_dir=code_dir, exclude=exclude)
    with cd(code_dir):
        run('docker-compose down ; docker-compose build')

@roles('vps')
def up():
    with cd(code_dir):
        run('docker-compose up -d')
