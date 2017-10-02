#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "git@github.com:ricky89sg/ricky89.git" 

env.user = 'ubuntu'
env.password = 'Zhang0725!'

# 填写你自己的主机对应的域名
env.hosts = ['13.58.186.200']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/home/ubuntu/website/ricky89'
    #run('cd %s ' % source_folder)
    run('cd /home/ubuntu/website/ricky89 && git reset --hard && git pull')
    #run('pwd')
    #run('cd website/ricky89')
    #run('pwd')
    #run('ls')
    #run('git reset --hard')
    #run('git pull')
    run("python website/ricky89/manage.py collectstatic --noinput")
    #run("yes | my_command")
    run("python website/ricky89/manage.py migrate")
    sudo('restart gunicorn-ricky89')
    sudo('service nginx reload')
