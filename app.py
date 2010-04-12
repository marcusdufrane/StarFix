#!/usr/bin/env python

from bottle import route, run, view

@route('/')
def index():
    return 'Hello World!'

@route('/result')
@view('result')
def template_result():
    context = {}
    context['title'] = "Asdf Asdf"
    context['sections'] = []
    context['sections'].append({'name':'Requirements', 'contents':'Blah blah blah'})
    return context


run(host='localhost', port=8080)

