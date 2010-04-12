#!/usr/bin/env python

class Section:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents  

    # maps dictionary accesses to attributes: section['name'] -> section.name
    def __getitem__(self, index):
        return getattr(self, index)

class Star:
    def __init__(self):
        self.sections = []
        self.name = ''

    def add_section(self, name, body):
        self.sections.append(Section(name, body))


def cleanup_name(name):
    last, first = name.split(',')
    return first + ' ' + last

def parse_star(star_file):
    lines = star_file.readlines()
    
    star = Star()
    
    star.name = cleanup_name(lines[1])
    
    star.add_section("Section One", "Contentz")
    star.add_section("Section Two", "Contentzz")
    
    return star
