#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print 'Usage: convert_stary.py filename'
    sys.exit(1)
    
filename = sys.argv[1]

star_file = open(filename)
output_filename = filename + '-pretty.html'
output_file = open(output_filename, 'w')

output_file.write(
"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
""")

output_file.write(
"""
    <title>%s</title>
""" % output_filename)

output_file.write(
"""
</head>
<body>
""")

lines = star_file.readlines()

output_file.write(
"""</body>
</html>
""")
