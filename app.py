#!/usr/bin/env python

from bottle import route, run, request, view
from StringIO import StringIO

import parser

@route('/')
@view('index')
def index():
    return {}

@route('/result', method="POST")
@view('result')
def template_result():
    if request.POST.get('startext'):
        star_file = StringIO(request.POST.get('startext'))
    else:    
        star_file = request.POST.get('starfile').file
    
    star = parser.parse_star(star_file)
    
    context = {}
    context['name'] = star.name
    context['sections'] = star.sections
    return context
    

run(host='localhost', port=8080)

