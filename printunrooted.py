#!/usr/bin/python

# printunrooted.py
# Use mechanize to visit Phylodendron and produce a .gif file for an inputted
# phylogenetic tree in newick format.

# sys.argv[1] -- newick tree

import sys, os, commands, re, mechanize

# Extract the newick tree
f = open( sys.argv[1], 'r' )
newick = f.read()
f.close()

# Connect to phylodendron
br = mechanize.Browser()
br.set_handle_robots(False)
response = br.open("http://iubio.bio.indiana.edu/treeapp/treeprint-form.html")

# Get the form
br.form = list(br.forms())[0]

# Enter all the proper info

# Set treestyle to traditional unrooted (radio)
control = br.form.find_control("gTreeStyles=fStyle")
control.value = ["0"]

# Set output format to .gif (select)
control = br.form.find_control("TREEAPP_OUTPUT_FORMAT")
control.value = ["image/gif"]

# Set width of .gif (text)
control = br.form.find_control("TreeDoc.width")
control.value = "1280"

# Set height of .gif (text)
control = br.form.find_control("TreeDoc.width")
control.value = "720"

# Set tree data to the newick data (text)
control = br.form.find_control("TREEAPP_STRING_DATA")
control.value = newick

# Submit the form
response = br.submit()

# Save the returned .gif
f = open( sys.argv[1]+'.gif', 'w' )
f.write( response.read() )
f.close()
