#!/usr/bin/env python

from bottle import route, run, request, view

import parser

@route('/')
@view('index')
def index():
    return {}


@route('/result', method="POST")
@view('result')
def template_result():
    star_file = request.POST.get('starfile').file
    star = parser.parse_star(star_file)
    
    context = {}
    context['name'] = star.name
    context['sections'] = star.sections
    return context


run(host='localhost', port=8080)

