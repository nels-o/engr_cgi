#!/usr/bin/python

import sys, os

# Must instantiate settings module before importing 
# any .egg dependencies. This invokes the egg loader. 
from settings import PROJECT_ROOT, STATIC_ROOT, CONTROL_ROOT

from bottle import route, run, template, response, request, static_file, TEMPLATE_PATH, view, redirect

TEMPLATE_PATH.insert(0,os.path.join(PROJECT_ROOT, 'views'))

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root=STATIC_ROOT)

@route('/')
@view('index')
def prototype():
    return {}

run(server="cgi")