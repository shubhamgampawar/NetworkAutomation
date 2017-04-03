#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import re
from bracket_expansion import *

import os
os.system('clear')

ENV = Environment(loader=FileSystemLoader('.'),trim_blocks='True',lstrip_blocks='True')
ENV.filters['bracket_expansion'] = bracket_expansion

filename_j2=sys.argv[1]
filename = re.sub("\.j2","",sys.argv[1])
filename_yml= '../vars/' + filename + '.yml'

with open(filename_yml) as temp:
   Input = temp.read()

print ('*****Reading YAML file '+filename_yml+'****')
print Input

def convert(filename):
    with open(filename) as temp:
        return yaml.load(temp)

Output_Dict=convert(filename_yml);

print ('\n****Rendering Jinja2 template '+filename_j2+' ****') 
template = ENV.get_template(filename_j2)
print(template.render(**Output_Dict))
